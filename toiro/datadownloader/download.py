import os
import requests
from pathlib import Path

from tqdm import tqdm

from .downloader_utils import get_resource_dir
from .downloader_utils import get_corpora_dict


def available_corpus():
    """
    Return a list of corpora available in this tool.

    Returns
    -------
    corpora_list : list
        The available corpus list

    Examples
    --------
    >>> toiro.available_corpus()
    ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']

    """
    corpora_dict = get_corpora_dict()
    corpora_list = list(corpora_dict.keys())
    return corpora_list


def download_corpus(corpus='yahoo_movie_reviews'):
    """
    Download the corpus from the download link.

    This module is used to download the corpus of the list
    ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews'].

    Parameters
    ----------
    corpus : str
        The corpus to download


    Examples
    --------
    >>> toiro.download_corpus(corpus='yahoo_movie_reviews')

    """
    corpora_dict = get_corpora_dict()

    corpora_list = list(corpora_dict.keys())

    if corpus not in corpora_list:
        err_msg = f"{corpus} is not available. Choose from {corpora_list}"
        raise Exception(err_msg)

    resource_dir = get_resource_dir()

    Path(resource_dir).mkdir(parents=True, exist_ok=True)

    filename = corpora_dict[corpus]["filename"]
    filepath = os.path.join(resource_dir, filename)
    download_url = corpora_dict[corpus]["url"]

    # download a corpus
    if os.path.exists(filepath):
        msg = f"{corpus} ({filename}) exists in {resource_dir} ."
        print(msg)
    else:
        verbose = True
        r = requests.get(download_url, stream=True)
        with open(filepath, 'wb') as f:
            file_size = int(r.headers.get('content-length'))
            default_chunk_size = 13107
            desc = f'Downloading {filename} from {download_url}'

            with tqdm(total=file_size, unit='B', unit_scale=True,
                      disable=not verbose, desc=desc) as pbar:

                for chunk in r.iter_content(chunk_size=default_chunk_size):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        pbar.update(len(chunk))
