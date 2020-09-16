import os
import csv
import json
import glob
import gzip
import random
import tarfile
import zipfile

import pandas as pd

from .downloader_utils import get_corpora_dict
from .downloader_utils import get_resource_dir


def _extract_tarfile(filename, target_dir):
    with tarfile.open(filename, 'r:*') as tar:
        tar.extractall(target_dir)


def _shuffle_data(is_shuffle, data):
    if is_shuffle:
        random.shuffle(data)


def _max_count_data(max_count, data):
    return data[:max_count]


def _split_train_dev_test(data, train_data=0.8, dev_data=0.1, test_data=0.1):
    total = train_data+dev_data+test_data
    if not total == 1.0:
        err_msg = f"The total of train/dev/test data: {total} must be 1."
        raise Exception(err_msg)

    num_train = int(len(data) * train_data)
    num_dev = int(len(data) * dev_data)
    num_test = int(len(data) * test_data)

    train = pd.DataFrame(data[:num_train])
    dev = pd.DataFrame(data[num_train:num_train+num_dev])
    test = pd.DataFrame(data[num_train+num_dev:num_train+num_dev+num_test])
    return train, dev, test


def _check_correct_corpus_type(corpus_type, corpus_types):
    if corpus_type not in corpus_types:
        err_msg = f"{corpus_type} is not available. Choose from {corpus_types}"
        raise Exception(err_msg)


def load_corpus(corpus, n=None, is_shuffle=True, corpus_type=None,
                train_data=0.8, dev_data=0.1, test_data=0.1, random_seed=1234):
    """
    Dataloader for selected corpus.

    The data is pre-processed and split into training data,
    development data and test data.

    Parameters
    ----------
    corpus : str
        The corpus

    n : int
        The number of datasets

    is_shuffle : bool
        If true, shuffle the dataset

    train_data : float
        Percentage of training data

    dev_data : float
        Percentage of development data

    test_data : float
        Percentage of test data

    random_seed : int
        Random seed for shuffle datasets

    Returns
    -------
    train_df : pandas.core.frame.DataFrame
        The training data

    dev_df : pandas.core.frame.DataFrame
        The development data

    test_df : pandas.core.frame.DataFrame
        The test data

    Examples
    --------
    >>> train_df, dev_df, test_df = datadownloader.load_corpus('livedoor_news_corpus')

    """

    if corpus == "amazon_reviews":
        return load_amazon_reviews(
            n=n, is_shuffle=is_shuffle,
            train_data=train_data, dev_data=dev_data, test_data=test_data,
            random_seed=random_seed)
    elif corpus == "yahoo_movie_reviews":
        if corpus_type is None:
            corpus_type = "binary"
        return load_yahoo_movie_reviews(
            n=n, is_shuffle=is_shuffle, corpus_type=corpus_type,
            train_data=train_data, dev_data=dev_data, test_data=test_data,
            random_seed=random_seed)
    elif corpus == "livedoor_news_corpus":
        if corpus_type is None:
            corpus_type = "title"
        return load_livedoor_news_corpus(
            n=n, is_shuffle=is_shuffle, corpus_type=corpus_type,
            train_data=train_data, dev_data=dev_data, test_data=test_data,
            random_seed=random_seed)
    elif corpus == "chABSA_dataset":
        return load_chABSA_dataset(
            n=n, is_shuffle=is_shuffle,
            train_data=train_data, dev_data=dev_data, test_data=test_data,
            random_seed=random_seed)
    else:
        err_msg = " ".join(
            [f"{corpus} does not exist.",
            f"Use datadownloader.download_corpus('{corpus}') ."]
        )
        raise Exception(err_msg)


def __count_polarity(opinions):
    posinega = {"positive": 1, "negative": -1}
    scores = [posinega.get(opinion["polarity"], 0) for opinion in opinions]
    score = sum(scores)

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


def load_chABSA_dataset(n=None, is_shuffle=True,
                        train_data=0.8, dev_data=0.1, test_data=0.1,
                        random_seed=1234):
    """
    Dataloader for chABSA dataset.

    The data is pre-processed and split into training data,
    development data and test data.

    Parameters
    ----------
    n : int
        The number of datasets

    is_shuffle : bool
        If true, shuffle the dataset

    train_data : float
        Percentage of training data

    dev_data : float
        Percentage of development data

    test_data : float
        Percentage of test data

    random_seed : int
        Random seed for shuffle datasets

    Returns
    -------
    train_df : pandas.core.frame.DataFrame
        The training data

    dev_df : pandas.core.frame.DataFrame
        The development data

    test_df : pandas.core.frame.DataFrame
        The test data

    """
    random.seed(random_seed)

    corpus = "chABSA_dataset"
    corpora_dict = get_corpora_dict()
    resource_dir = get_resource_dir()

    filename = corpora_dict[corpus]["filename"]
    filepath = os.path.join(resource_dir, filename)

    with zipfile.ZipFile(filepath, 'r') as f:
        f.extractall(resource_dir)

    files = glob.glob(os.path.join(resource_dir, "chABSA-dataset", "*.json"))
    data = []
    for _file in files:
        with open(_file, "r") as f:
            _data = json.load(f)
            sentences = _data["sentences"]
            for sentence in sentences:
                sent = sentence["sentence"]
                opinions = sentence["opinions"]
                label = __count_polarity(opinions)
                data.append([label, sent])

    _shuffle_data(is_shuffle, data)
    data = _max_count_data(n, data)
    train_df, dev_df, test_df = _split_train_dev_test(
        data, train_data=train_data, dev_data=dev_data, test_data=test_data
    )
    return train_df, dev_df, test_df


def load_amazon_reviews(n=None, is_shuffle=True,
                        train_data=0.8, dev_data=0.1, test_data=0.1,
                        random_seed=1234):
    """
    Dataloader for amazon reviews.

    The data is pre-processed and split into training data,
    development data and test data.

    Parameters
    ----------
    n : int
        The number of datasets

    is_shuffle : bool
        If true, shuffle the dataset

    train_data : float
        Percentage of training data

    dev_data : float
        Percentage of development data

    test_data : float
        Percentage of test data

    random_seed : int
        Random seed for shuffle datasets

    Returns
    -------
    train_df : pandas.core.frame.DataFrame
        The training data

    dev_df : pandas.core.frame.DataFrame
        The development data

    test_df : pandas.core.frame.DataFrame
        The test data

    """

    random.seed(random_seed)

    corpus = "amazon_reviews"
    corpora_dict = get_corpora_dict()
    resource_dir = get_resource_dir()

    filename = corpora_dict[corpus]["filename"]
    filepath = os.path.join(resource_dir, filename)

    data = []
    if os.path.exists(filepath):
        with gzip.open(filepath, "rt") as f:
            reader = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
            next(reader)
            for line in reader:
                rating = line[7]
                text = line[13]
                data.append([rating, text])

    _shuffle_data(is_shuffle, data)
    data = _max_count_data(n, data)
    train_df, dev_df, test_df = _split_train_dev_test(
        data, train_data=train_data, dev_data=dev_data, test_data=test_data
    )
    return train_df, dev_df, test_df


def load_yahoo_movie_reviews(n=None, is_shuffle=True, corpus_type="binary",
                             train_data=0.8, dev_data=0.1, test_data=0.1,
                             random_seed=1234):
    """
    Dataloader for yahoo_movie_reviews.

    The data is pre-processed and split into training data,
    development data and test data.

    Parameters
    ----------
    n : int
        The number of datasets

    is_shuffle : bool
        If true, shuffle the dataset

    train_data : float
        Percentage of training data

    dev_data : float
        Percentage of development data

    test_data : float
        Percentage of test data

    random_seed : int
        Random seed for shuffle datasets

    Returns
    -------
    train_df : pandas.core.frame.DataFrame
        The training data

    dev_df : pandas.core.frame.DataFrame
        The development data

    test_df : pandas.core.frame.DataFrame
        The test data

    """

    corpus_types = ["binary", "original"]
    _check_correct_corpus_type(corpus_type, corpus_types)
    random.seed(random_seed)

    corpus = "yahoo_movie_reviews"
    corpora_dict = get_corpora_dict()
    resource_dir = get_resource_dir()

    filename = corpora_dict[corpus]["filename"]
    filepath = os.path.join(resource_dir, filename)
    if os.path.exists(filepath):
        yahoo_movie_reviews_dir = os.path.join(resource_dir, "data")
        if not os.path.exists(yahoo_movie_reviews_dir):
            _extract_tarfile(filepath, resource_dir)

        yahoo_movie_reviews_json = os.path.join(
            yahoo_movie_reviews_dir, "yahoo-movie-reviews.json"
        )
        if not os.path.exists(yahoo_movie_reviews_json):
            err_msg = " ".join([
                f"{yahoo_movie_reviews_json} does not exist. ",
                f"Use datadownloader.download_corpus('{corpus}') ."
                ]
            )
            raise Exception(err_msg)

        data = []
        with open(yahoo_movie_reviews_json, "r") as f:
            json_load = json.load(f)
            for line in json_load:
                text = line["text"].replace("\n", "")
                rating = str(line["rating"])
                if corpus_type == "binary":
                    if rating in ["1", "2"]:
                        rating = 0
                        data.append([rating, text])
                    elif rating in ["4", "5"]:
                        rating = 1
                        data.append([rating, text])
                else:
                    data.append([rating, text])

        if corpus_type == "binary":
            label2texts = {}
            for line in data:
                label, text = line
                if label in label2texts:
                    label2texts[label].append(text)
                else:
                    label2texts[label] = [text]

            num_data = min(
                [len(label2texts[key]) for key in label2texts.keys()]
            )

            data = []
            for key in label2texts.keys():
                texts = label2texts[key][:num_data]
                for text in texts:
                    data.append([key, text])

        _shuffle_data(is_shuffle, data)
        data = _max_count_data(n, data)
        train_df, dev_df, test_df = _split_train_dev_test(
            data, train_data=train_data, dev_data=dev_data, test_data=test_data
        )
        return train_df, dev_df, test_df

    else:
        err_msg = " ".join(
            [f"{corpus} does not exist.",
            f"Use datadownloader.download_corpus('{corpus}') ."]
        )
        raise Exception(err_msg)


def load_livedoor_news_corpus(n=None, is_shuffle=True, corpus_type="title",
                              train_data=0.8, dev_data=0.1, test_data=0.1,
                              random_seed=1234):
    """
    Dataloader for livedoor news corpus.

    The data is pre-processed and split into training data,
    development data and test data.

    Parameters
    ----------
    n : int
        The number of datasets

    is_shuffle : bool
        If true, shuffle the dataset

    train_data : float
        Percentage of training data

    dev_data : float
        Percentage of development data

    test_data : float
        Percentage of test data

    random_seed : int
        Random seed for shuffle datasets

    Returns
    -------
    train_df : pandas.core.frame.DataFrame
        The training data

    dev_df : pandas.core.frame.DataFrame
        The development data

    test_df : pandas.core.frame.DataFrame
        The test data

    """

    corpus_types = ["title", "article"]
    _check_correct_corpus_type(corpus_type, corpus_types)

    random.seed(random_seed)
    corpus = "livedoor_news_corpus"
    label_names = [
        "dokujo-tsushin",
        "kaden-channel",
        "movie-enter",
        "smax",
        "topic-news",
        "it-life-hack",
        "livedoor-homme",
        "peachy",
        "sports-watch"
    ]

    corpora_dict = get_corpora_dict()
    resource_dir = get_resource_dir()

    filename = corpora_dict[corpus]["filename"]
    filepath = os.path.join(resource_dir, filename)

    if os.path.exists(filepath):
        livedoor_news_corpus_dir = os.path.join(resource_dir, "text")
        if not os.path.exists(livedoor_news_corpus_dir):
            _extract_tarfile(filepath, resource_dir)

        dirs = glob.glob(f"{livedoor_news_corpus_dir}/*")

        data = []
        for dir_name in dirs:
            dir_basename = os.path.basename(dir_name)
            if dir_basename in label_names:
                files = glob.glob(f"{dir_name}/*")
                for filename in files:
                    with open(filename, "r") as f:
                        article = []
                        for i, line in enumerate(f):
                            line = line.strip().replace("\t", "")
                            if corpus_type == "title":
                                if i == 2:
                                    data.append([dir_basename, line])

                            if corpus_type == "article":
                                if i > 2:
                                    article.append(line)

                    if corpus_type == "article":
                        article = "".join(article)
                        data.append([dir_basename, article])

        _shuffle_data(is_shuffle, data)
        data = _max_count_data(n, data)
        train_df, dev_df, test_df = _split_train_dev_test(
            data, train_data=train_data, dev_data=dev_data, test_data=test_data
        )
        return train_df, dev_df, test_df

    else:
        err_msg = " ".join(
            [f"{corpus} does not exist.",
            f"Use datadownloader.download_corpus('{corpus}') ."]
        )
        raise Exception(err_msg)
