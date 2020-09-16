import os
from pathlib import Path

_LIB_NAME = "toiro"

_HOME_DIR = str(Path.home())
_RESOURCE_DIR = os.getenv(
    f"{_LIB_NAME}", os.path.join(_HOME_DIR, f'{_LIB_NAME}_resources')
)

# A dataset list
_CORPORA_DICT = {
    "livedoor_news_corpus": {
        "url": "https://www.rondhuit.com/download/ldcc-20140209.tar.gz",
        "filename": "ldcc-20140209.tar.gz"
    },
    "yahoo_movie_reviews":
        {
            "url": "https://media.githubusercontent.com/media/dennybritz/sentiment-analysis/master/data/yahoo-movie-reviews.json.tar.gz",
            "filename": "yahoo-movie-reviews.json.tar.gz"
        },

    "amazon_reviews":
        {
            "url": "https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_JP_v1_00.tsv.gz",
            "filename": "amazon_reviews_multilingual_JP_v1_00.tsv.gz"
        },
    "chABSA_dataset":
        {
            "url": "https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/chABSA-dataset.zip",
            "filename": "chABSA-dataset.zip"
        }
}


def get_resource_dir():
    """
    Return the path of the toiro directory.

    The dataset directory of this tool is created
    as toiro_resources in your home directory.

    Returns
    -------
    _RESOURCE_DIR : str
        The toiro directory in your execution environment.

    Examples
    --------
    >>> toiro.get_resource_dir()
    '~/toiro_resources'

    """
    return _RESOURCE_DIR


def get_corpora_dict():
    """
    Return the dataset information in toiro.

    Returns
    -------
    _CORPORA_DICT : dict
        The information of the avaibale corpus in this tool.

    Examples
    --------
    >>> toiro.get_corpora_dict()

    """
    return _CORPORA_DICT
