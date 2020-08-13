from sudachipy import tokenizer
from sudachipy import dictionary

# Initialize sudachipy
tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C


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
    words = [m.surface() for m in tokenizer_obj.tokenize(text, mode)]
    return words


def original_usage(text):
    """
    Return the analysis results by SudachiPy.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : sudachipy.morphemelist.MorphemeList
        The analysis results by SudachiPy
    """
    tokens = tokenizer_obj.tokenize(text, mode)
    return tokens
