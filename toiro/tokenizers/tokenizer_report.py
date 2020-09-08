import time

from tqdm import tqdm
from cpuinfo import get_cpu_info

import numpy as np
from toiro import tokenizers


def get_avaiable_tokenizers(disable_tokenizers=None):
    if disable_tokenizers is None:
        disable_tokenizers = []

    _tokenizers = {}
    if tokenizers.is_mecab_available():
        _mecab_python3 = 'mecab-python3'
        if _mecab_python3 not in disable_tokenizers:
            _tokenizers[_mecab_python3] = tokenizers.tokenize_mecab

    if tokenizers.is_janome_available():
        _janome = 'janome'
        if _janome not in disable_tokenizers:
            _tokenizers[_janome] = tokenizers.tokenize_janome

    if tokenizers.is_nagisa_available():
        _nagisa = 'nagisa'
        if _nagisa not in disable_tokenizers:
            _tokenizers[_nagisa] = tokenizers.tokenize_nagisa

    if tokenizers.is_sudachipy_available():
        _sudachipy = 'sudachipy'
        if _sudachipy not in disable_tokenizers:
            _tokenizers[_sudachipy] = tokenizers.tokenize_sudachipy

    if tokenizers.is_spacy_available():
        _spacy = 'spacy'
        if _spacy not in disable_tokenizers:
            _tokenizers[_spacy] = tokenizers.tokenize_spacy

    if tokenizers.is_ginza_available():
        _ginza = 'ginza'
        if _ginza not in disable_tokenizers:
            _tokenizers[_ginza] = tokenizers.tokenize_ginza

    if tokenizers.is_kytea_available():
        _kytea = 'kytea'
        if _kytea not in disable_tokenizers:
            _tokenizers[_kytea] = tokenizers.tokenize_kytea

    if tokenizers.is_jumanpp_available():
        _jumanpp = 'jumanpp'
        if _jumanpp not in disable_tokenizers:
            _tokenizers[_jumanpp] = tokenizers.tokenize_jumanpp

    if tokenizers.is_sentencepiece_available():
        _sentencepiece = 'sentencepiece'
        if _sentencepiece not in disable_tokenizers:
            _tokenizers[_sentencepiece] = tokenizers.tokenize_sentencepiece

    if tokenizers.is_fugashi_ipadic_available():
        _fugashi_ipadic = 'fugashi-ipadic'
        if _fugashi_ipadic not in disable_tokenizers:
            _tokenizers[_fugashi_ipadic] = tokenizers.tokenize_fugashi_ipadic

    if tokenizers.is_fugashi_unidic_available():
        _fugashi_unidic = 'fugashi-unidic'
        if _fugashi_unidic not in disable_tokenizers:
            _tokenizers[_fugashi_unidic] = tokenizers.tokenize_fugashi_unidic

    if tokenizers.is_tinysegmenter_available():
        _tinysegmenter = 'tinysegmenter'
        if _tinysegmenter not in disable_tokenizers:
            _tokenizers[_tinysegmenter] = tokenizers.tokenize_tinysegmenter

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


def compare_from_file(filename, disable_tokenizers=None, verbose=True,
                      additional_tokenizers=None):
    """
    Method to compare the tokenizers from an input text.

    This function outputs information about the execution environment
    and data and comparison results.

    Parameters
    ----------
    filename : str
        An input file

    disable_tokenizers : list
        A list of non-comparative tokenizers

    verbose : bool
        If True, show the process

    additional_tokenizers: dict
        A list of tokenizers to be added to the comparison is
        in dictionary form,
        where the keys are names and the values are functions.

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
    report = compare(
        texts, disable_tokenizers=disable_tokenizers, verbose=verbose,
        additional_tokenizers=additional_tokenizers
    )
    return report


def compare(texts, disable_tokenizers=None, verbose=True,
            additional_tokenizers=None):
    """
    Method to compare the tokenizers for a list of input text.

    This function outputs information about the execution environment
    and data and comparison results.

    Parameters
    ----------
    texts : list
        A list of input text

    disable_tokenizers : list
        A list of non-comparative tokenizers

    verbose : bool
        If True, show the process

    additional_tokenizers: dict
        A list of tokenizers to be added to the comparison is
        in dictionary form,
        where the keys are names and the values are functions.

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
    tokenizers = get_avaiable_tokenizers(disable_tokenizers)
    if additional_tokenizers:
        tokenizers.update(additional_tokenizers)

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


def print_words(text, disable_tokenizers=None, delimiter=" ",
                additional_tokenizers=None):
    """
    Method to compare the segmented words.

    Print the results of the compared word segmentation.

    Parameters
    ----------
    texts : str
        An input text

    disable_tokenizers : list
        A list of non-comparative tokenizers

    delimiter : str
        A delimiter of words

    additional_tokenizers: dict
        A list of tokenizers to be added to the comparison is
        in dictionary form,
        where the keys are names and the values are functions.

    Examples
    --------
    >>> text = "単語分割の結果を比較します"
    >>> tokenizers.print_words(text, delimiter="|")
           nagisa: 単語|分割|の|結果|を|比較|し|ます
           janome: 単語|分割|の|結果|を|比較|し|ます
    mecab_python3: 単語|分割|の|結果|を|比較|し|ます
    """
    tokenizers = get_avaiable_tokenizers(disable_tokenizers=disable_tokenizers)
    if additional_tokenizers:
        tokenizers.update(additional_tokenizers)

    for tokenizer_name, tokenize in tokenizers.items():
        words = tokenize(text)
        words = delimiter.join(words)
        print(f"{tokenizer_name:>14}: {words}")
