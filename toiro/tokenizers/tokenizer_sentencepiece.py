import os
import sys

import sentencepiece as spm

base = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base)


sp = spm.SentencePieceProcessor()

sp_model_file = base + "/data/ja.text8.txt.spm"
sp.load(f"{sp_model_file}.model")


def tokenize(text):
    """
    A method for word segmentation.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    words : list
        A list of words
    """
    words = sp.encode_as_pieces(text)
    return words


def original_usage(text):
    """
    Return the analysis results by sentencepiece.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        The analysis results by sentencepiece
    """

    pieces = sp.encode_as_pieces(text)
    ids = sp.encode_as_ids(text)
    tokens = [pieces, ids]
    return tokens
