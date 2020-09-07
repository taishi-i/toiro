import os

import ipadic
import fugashi

dic_dir = ipadic.DICDIR
mecabrc = os.path.join(dic_dir, "mecabrc")
mecab_option = f"-d {dic_dir} -r {mecabrc}"
tagger = fugashi.GenericTagger(mecab_option)


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

    words = [word.surface for word in tagger(text)]
    return words


def original_usage(text):
    """
    Return the analysis results by fugashi with ipadic.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        A list of fugashi.fugashi.Node
    """
    tokens = tokenize(text)
    return tokens
