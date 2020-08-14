import time
import pickle

from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer


from toiro import tokenizers
from toiro import classifiers


class SVMClassificationModel:
    """
    Text classification model based on SVM and tf-idf.

    Attributes
    ----------
    tokenizer : str
        The word segmenter for Japanese text.
        You can choose tokenizers in tokenizers.get_avaiable_tokenizers().

    original_tokenizer : func
        An original tokenizer of your own definition.

    model_file : str
        The trained model file

    Methods
    -------
    fit(train_df, dev_df=None)
        Train a text classification model.
    eval(eval_df)
        Evaluate the trained model.
    predict(text)
        Predict a label.
    save(filename)
        Save the trained model.
    """

    def __init__(self, tokenizer="janome",
                 original_tokenizer=None, model_file=None):
        self.tokenizer = tokenizers.SelectTokenizer(tokenizer)

        if original_tokenizer:
            self.tokenize = original_tokenizer
        else:
            self.tokenize = self.tokenizer.tokenize

        if model_file is None:
            self.tfidf_extracter = TfidfVectorizer(
                ngram_range=(1, 2),
                tokenizer=self.tokenize,
                max_df=0.9,
                min_df=3,
                sublinear_tf=1
            )
            self.svm = LinearSVC()
        else:
            with open(model_file, "rb") as f:
                self.svm, self.tfidf_extracter = pickle.load(f)

        self.elapsed_time = None

    def fit(self, train_df, dev_df=None):
        start = time.time()
        train_Y = train_df[0].values
        train_X = self.tfidf_extracter.fit_transform(train_df[1])
        self.svm.fit(train_X, train_Y)
        self.elapsed_time = time.time() - start

    def eval(self, eval_df):
        test_Y = eval_df[0].values
        test_X = self.tfidf_extracter.transform(eval_df[1])

        pred_Y = self.svm.predict(test_X)
        accuracy = accuracy_score(test_Y, pred_Y)
        macro_f1 = f1_score(test_Y, pred_Y, average="macro")
        cr = classification_report(test_Y, pred_Y)
        eval_metrics = classifiers.EvaluationMetrics(
            accuracy, macro_f1, cr, self.elapsed_time
        )
        return eval_metrics

    def predict(self, text):
        text = [text]
        x = self.tfidf_extracter.transform(text)
        pred_y = self.svm.predict(x)
        pred_y = pred_y[0]
        return pred_y

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump((self.svm, self.tfidf_extracter), f)
