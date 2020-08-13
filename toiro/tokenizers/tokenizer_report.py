import time

from tqdm import tqdm
from cpuinfo import get_cpu_info

import numpy as np

import toiro

from toiro import tokenizers


def get_avaiable_tokenizers():

    _tokenizers = {}

    # if tokenizers.is_mecab_available():
    if tokenizers.is_mecab_available():
        _mecab_python3 = 'mecab-python3'

        _tokenizers[_mecab_python3] = tokenizers.tokenize_mecab

    if tokenizers.is_janome_available():
        _janome = 'janome'

        _tokenizers[_janome] = tokenizers.tokenize_janome

    if tokenizers.is_nagisa_available():
        _nagisa = 'nagisa'

        _tokenizers[_nagisa] = tokenizers.tokenize_nagisa

    if tokenizers.is_sudachipy_available():
        _sudachipy = 'sudachipy'

        _tokenizers[_sudachipy] = tokenizers.tokenize_sudachipy

    if tokenizers.is_spacy_available():
        _spacy = 'spacy'

        _tokenizers[_spacy] = tokenizers.tokenize_spacy

    if tokenizers.is_ginza_available():
        _ginza = 'ginza'

        _tokenizers[_ginza] = tokenizers.tokenize_ginza

    if tokenizers.is_kytea_available():
        _kytea = 'kytea'

        _tokenizers[_kytea] = tokenizers.tokenize_kytea

    if tokenizers.is_jumanpp_available():
        _jumanpp = 'jumanpp'

        _tokenizers[_jumanpp] = tokenizers.tokenize_jumanpp

    if tokenizers.is_sentencepiece_available():
        _sentencepiece = 'sentencepiece'

        _tokenizers[_sentencepiece] = tokenizers.tokenize_sentencepiece

    return _tokenizers


class SelectTokenizer:

    def __init__(self, tokenizer):
        avaiable_tokenizers = get_avaiable_tokenizers()
        self.tokenize = avaiable_tokenizers[tokenizer]


def _make_initial_report(texts):
    report = {'execution_environment': {}}
    cpu_info = get_cpu_info()
    keys = ['python_version', 'arch', 'brand_raw', 'count']
    for key in keys:
        report['execution_environment'][key] = cpu_info[key]

    report['data'] = {'number_of_sentences': len(texts)}
    average_length = np.average([len(text) for text in texts])
    report['data']['average_length'] = average_length
    return report


def compare_from_file(filename, verbose=True):
    """
    Method to compare the tokenizers from an input text.

    This function outputs information about the execution environment
    and data and comparison results.

    Parameters
    ----------
    filename : str
        An input file

    verbose : bool
        If True, show the process

    Returns
    -------
    report : dict
        Comparison results

    Examples
    --------
    >>> report = tokenizers.corpora_from_file(filename)
    >>> print(report)
    """
    with open(filename, "r") as f:
        texts = [line.strip() for line in f if len(line.strip()) > 0]
    report = compare(texts, verbose=verbose)
    return report


def compare(texts, verbose=True):
    """
    Method to compare the tokenizers for a list of input text.

    This function outputs information about the execution environment
    and data and comparison results.

    Parameters
    ----------
    texts : list
        A list of input text

    verbose : bool
        If True, show the process

    Returns
    -------
    report : dict
        Comparison results

    Examples
    --------
    >>> report = tokenizers.corpora(texts)
    >>> print(report)
    """
    report = _make_initial_report(texts)

    tokenizers = get_avaiable_tokenizers()
    num_tokenizers = len(tokenizers.items())
    for i, (tokenizer_name, tokenize) in enumerate(tokenizers.items(), 1):
        if verbose:
            print(f"[{i}/{num_tokenizers}] Tokenizer: {tokenizer_name}")
            texts = tqdm(texts)

        start = time.time()
        for text in texts:
            words = tokenize(text)
        elapsed_time = time.time() - start

        report[tokenizer_name] = {}
        report[tokenizer_name]['elapsed_time'] = elapsed_time

    return report


def print_words(text, delimiter=" "):
    """
    Method to compare the segmented words.

    Print the results of the compared word segmentation.

    Parameters
    ----------
    texts : str
        An input text

    delimiter : str
        A delimiter of words

    Examples
    --------
    >>> text = "単語分割の結果を比較します"
    >>> tokenizers.print_words(text, delimiter="|")
           nagisa: 単語|分割|の|結果|を|比較|し|ます
           janome: 単語|分割|の|結果|を|比較|し|ます
    mecab_python3: 単語|分割|の|結果|を|比較|し|ます
    """
    tokenizers = get_avaiable_tokenizers()
    for tokenizer_name, tokenize in tokenizers.items():
        words = tokenize(text)
        words = delimiter.join(words)
        print(f"{tokenizer_name:>13}: {words}")
