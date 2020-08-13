import nagisa


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
    words = nagisa.wakati(text)
    return words


def original_usage(text):
    """
    Return the analysis results by nagisa.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : nagisa.tagger.Tagger._Token
        The analysis results by nagisa
    """
    tokens = nagisa.tagging(text)
    return tokens
