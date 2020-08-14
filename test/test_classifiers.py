from toiro import classifiers
from toiro import datadownloader


def test_classifier_svm():
    # Download the livedoor news corpus and load it as pandas.DataFrame
    corpora = datadownloader.available_corpus()
    livedoor_corpus = corpora[0]
    datadownloader.download_corpus(livedoor_corpus)
    train_df, dev_df, test_df = datadownloader.load_corpus(
        corpus=livedoor_corpus
    )

    model = classifiers.SVMClassificationModel()
    model.fit(train_df, dev_df)
    eval_result = model.eval(test_df)
    print(eval_result)
    print(eval_result['accuracy_score'])
    print(eval_result['elapsed_time'])

    model.save(f"{livedoor_corpus}.pkl")
    model = classifiers.SVMClassificationModel(
        model_file=f"{livedoor_corpus}.pkl"
    )

    text = "Python で前処理を"
    pred_y = model.predict(text)

    expected = "dokujo-tsushin"
    assert pred_y == expected


def test_classifier_bert():
    if classifiers.is_bert_available():
        train_df = classifiers.read_file(
            datadownloader.sample_datasets.sample_train
        )

        dev_df = classifiers.read_file(
            datadownloader.sample_datasets.sample_dev
        )

        # test_df = classifiers.read_file(
        #     datadownloader.sample_datasets.sample_test
        # )

        model = classifiers.BERTClassificationModel()
        model.fit(train_df, dev_df)

        text = "Python で前処理を"
        pred_y = model.predict(text)
    else:
        assert classifiers.is_bert_available() is False
