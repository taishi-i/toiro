import tinysegmenter


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

    words = tinysegmenter.tokenize(text)
    return words


def original_usage(text):
    """
    Return the analysis results by tinysegmenter.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        A list of words
    """
    tokens = tinysegmenter.tokenize(text)
    return tokens
