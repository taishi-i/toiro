import os

import pytest

from toiro import datadownloader


def test_available_corpus():
    corpora = datadownloader.available_corpus()
    excepted = [
        'livedoor_news_corpus', 'yahoo_movie_reviews',
        'amazon_reviews', 'chABSA_dataset'
    ]
    assert corpora == excepted


def test_check_correct_corpus_type_error():
    with pytest.raises(Exception):
        corpus = ""
        datadownloader.download_corpus(corpus=corpus)


def test_download_corpus():
    available_corpus = datadownloader.available_corpus()
    for corpus in available_corpus:
        datadownloader.download_corpus(corpus)

        corpora_dict = datadownloader.get_corpora_dict()
        resource_dir = datadownloader.get_resource_dir()

        filename = corpora_dict[corpus]['filename']
        filepath = os.path.join(resource_dir, filename)
        assert os.path.exists(filepath)


def test_split_train_dev_test_error():
    corpora = datadownloader.available_corpus()
    corpus = corpora[0]
    with pytest.raises(Exception):
        train_data = 0.9
        dev_data = 0.2
        test_data = 0.1
        train_df, dev_df, test_df = datadownloader.load_corpus(
            corpus=corpus,
            train_data=train_data, dev_data=dev_data, test_data=test_data
        )


def test_load_corpus():
    available_corpus = datadownloader.available_corpus()

    num_corpus = {
        'livedoor_news_corpus': {'train': 5900, 'dev': 737, 'test': 737},
        'yahoo_movie_reviews': {'train': 72956, 'dev': 9119, 'test': 9119},
        'amazon_reviews': {'train': 209944, 'dev': 26243, 'test': 26243},
        'chABSA_dataset': {'train': 4895, 'dev': 611, 'test': 611}
    }

    for corpus in available_corpus:
        if corpus == 'livedoor_news_corpus':
            train_df, dev_df, test_df = datadownloader.load_corpus(
                corpus=corpus
            )

        elif corpus == 'yahoo_movie_reviews':
            train_df, dev_df, test_df = datadownloader.load_corpus(
                corpus=corpus, corpus_type='original'
            )

        elif corpus == 'amazon_reviews':
            train_df, dev_df, test_df = datadownloader.load_corpus(
                corpus=corpus
            )
        elif corpus == 'chABSA_dataset':
            train_df, dev_df, test_df = datadownloader.load_corpus(
                corpus=corpus
            )

        num_data = num_corpus[corpus]
        excepted_train = num_data['train']
        excepted_dev = num_data['dev']
        excepted_test = num_data['test']

        assert len(train_df) == excepted_train
        assert len(dev_df) == excepted_dev
        assert len(test_df) == excepted_test
