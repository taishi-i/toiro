import os
import time
import pickle

import torch

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from transformers import AutoModel
from transformers import AutoConfig
from transformers import AutoTokenizer

from catalyst.dl import SupervisedRunner
from catalyst.dl.callbacks import AccuracyCallback

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from toiro import classifiers


class BERTBaseJapaneseModel(torch.nn.Module):
    def __init__(self, model_name, num_labels):
        super().__init__()
        config = AutoConfig.from_pretrained(model_name, num_labels=num_labels)
        self.bert = AutoModel.from_pretrained(model_name, config=config)
        self.pre_classifier = torch.nn.Linear(
            config.hidden_size, config.hidden_size
        )
        self.classifier = torch.nn.Linear(config.hidden_size, num_labels)
        seq_classification_dropout = 0.2
        self.dropout = torch.nn.Dropout(seq_classification_dropout)

    def forward(self, features, attention_mask=None, head_mask=None):
        assert attention_mask is not None, "attention mask is none"
        bert_output = self.bert(
            input_ids=features,
            attention_mask=attention_mask,
            head_mask=head_mask
        )
        hidden_state = bert_output[0]
        pooled_output = hidden_state[:, 0]
        pooled_output = self.pre_classifier(pooled_output)
        pooled_output = torch.nn.ReLU()(pooled_output)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits


class ClassificationDataset(Dataset):

    def __init__(self,
                 tokenizer, label2id, max_seq_length, texts, labels=None):
        self.tokenizer = tokenizer
        self.pad_vid = self.tokenizer.vocab["[PAD]"]
        self.label2id = label2id
        self.texts = texts
        self.labels = labels
        self.max_seq_length = max_seq_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        output_dict = self._from_text(text)
        if self.labels is not None:
            y = self.labels[index]
            y_encoded = torch.Tensor(
                [self.label2id.get(y, -1)]
            ).long().squeeze(0)
            output_dict["targets"] = y_encoded
        return output_dict

    def _from_text(self, text):
        x_encoded = self.tokenizer.encode(
            text,
            add_special_tokens=True,
            max_length=self.max_seq_length,
            return_tensors="pt",
            truncation=True
        ).squeeze(0)
        true_seq_length = x_encoded.size(0)
        pad_size = self.max_seq_length - true_seq_length
        pad_ids = torch.Tensor([self.pad_vid] * pad_size).long()
        x_tensor = torch.cat((x_encoded, pad_ids))
        mask = torch.ones_like(x_encoded, dtype=torch.int8)
        mask_pad = torch.zeros_like(pad_ids, dtype=torch.int8)
        mask = torch.cat((mask, mask_pad))
        output_dict = {"features": x_tensor, "attention_mask": mask}
        return output_dict


class BERTClassificationModel:

    def __init__(self,
                 model_name="cl-tohoku/bert-base-japanese-whole-word-masking",
                 checkpoints_dir=None):

        """
        Text classification model based on Japanese BERT Model.

        Attributes
        ----------
        model_name : str
            The BERT model file
        checkpoints_dir : str
            The path of trained BERT model dir

        -------
        fit()
            Train a text classification model.
        eval()
            Evaluate the trained model.
        predict()
            Predict a label.
        """

        self.runner = SupervisedRunner(
            input_key=("features", "attention_mask")
        )

        if checkpoints_dir:
            config_file = f"{checkpoints_dir}/checkpoints/config.pkl"
            if os.path.exists(config_file):
                with open(config_file, "rb") as f:
                    self.label2id, self.config = pickle.load(f)
                    self.id2label = {v: k for k, v in self.label2id.items()}

                num_labels = len(self.label2id)
                self.max_seq_length = self.config["max_seq_length"]
                self.batch_size = self.config["batch_size"]
                self.model_name = self.config["model_name"]
                self.elapsed_time = self.config["elapsed_time"]
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
                self.model = BERTBaseJapaneseModel(self.model_name, num_labels)

                self.data_for_predict = ClassificationDataset(
                    tokenizer=self.tokenizer,
                    label2id=self.label2id,
                    max_seq_length=self.max_seq_length,
                    texts=["checkpoints"]
                )

                temporary_data = {
                    "temporary": DataLoader(
                        dataset=self.data_for_predict,
                        batch_size=self.batch_size,
                        shuffle=False
                    )
                }

                # Load the trained BERT model
                self.runner.infer(
                    model=self.model,
                    loaders=temporary_data,
                    resume=f"{checkpoints_dir}/checkpoints/best.pth"
                )

        else:
            self.model_name = model_name
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.pad_vid = self.tokenizer.vocab["[PAD]"]
            self.data_for_predict = None

    def fit(self,
            train_df, dev_df,
            batch_size=16, max_seq_length=256, learning_rate=5e-5,
            epochs=1, log_dir=None, verbose=False):

            start = time.time()
            config = {
                "model_name": self.model_name,
                "batch_size": batch_size,
                "max_seq_length": max_seq_length,
                "learning_rate": learning_rate,
                "epochs": epochs,
                "log_dir": log_dir
            }

            train_y = train_df[0]
            train_X = train_df[1]
            label2id = dict(
                zip(sorted(set(train_y)), range(len(set(train_y))))
            )
            self.id2label = {v: k for k, v in label2id.items()}
            num_labels = len(label2id)

            self.train_data = ClassificationDataset(
                tokenizer=self.tokenizer,
                label2id=label2id,
                max_seq_length=max_seq_length,
                texts=train_X,
                labels=train_y
            )

            dev_y = dev_df[0]
            dev_X = dev_df[1]

            self.dev_data = ClassificationDataset(
                tokenizer=self.tokenizer,
                label2id=label2id,
                max_seq_length=max_seq_length,
                texts=dev_X,
                labels=dev_y
            )

            train_dev_loaders = {
                "train": DataLoader(
                    dataset=self.train_data,
                    batch_size=batch_size,
                    shuffle=True
                ),
                "valid": DataLoader(
                    dataset=self.dev_data,
                    batch_size=batch_size,
                    shuffle=False
                )
            }

            model = BERTBaseJapaneseModel(self.model_name, num_labels)
            criterion = torch.nn.CrossEntropyLoss()
            optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
            scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer)

            self.runner.train(
                model=model,
                criterion=criterion,
                optimizer=optimizer,
                scheduler=scheduler,
                loaders=train_dev_loaders,
                callbacks=[
                    AccuracyCallback(num_classes=num_labels),
                ],
                fp16=None,
                logdir=log_dir,
                num_epochs=epochs,
                verbose=verbose
            )

            self.elapsed_time = time.time() - start
            config["elapsed_time"] = self.elapsed_time

            if os.path.exists(f"{log_dir}/checkpoints"):
                filename = f"{log_dir}/checkpoints/config.pkl"
                with open(filename, "wb") as f:
                    pickle.dump([label2id, config], f)

    def predict(self, text):
        if self.data_for_predict:
            x = self.data_for_predict._from_text(text)
        else:
            x = self.train_data._from_text(text)

        x["features"] = x["features"].reshape(1, -1)
        x["attention_mask"] = x["attention_mask"].reshape(1, -1)
        logits = self.runner.predict_batch(x)['logits']
        pred_id = logits.argmax(axis=1)
        pred_y = self.id2label[int(pred_id)]
        return pred_y

    def eval(self, test_df):
        test_Y = test_df[0]
        pred_Y = [self.predict(text) for text in test_df[1]]

        accuracy = accuracy_score(test_Y, pred_Y)
        macro_f1 = f1_score(test_Y, pred_Y, average="macro")
        cr = classification_report(test_Y, pred_Y)

        eval_metrics = classifiers.EvaluationMetrics(
            accuracy, macro_f1, cr, self.elapsed_time
        )
        return eval_metrics
