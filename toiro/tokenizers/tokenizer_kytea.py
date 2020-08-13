import Mykytea

mk = Mykytea.Mykytea("")


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

    words = [word for word in mk.getWS(text)]
    return words


def original_usage(text):
    """
    Return the analysis results by kytea.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : Mykytea.TagsVector
        The analysis results by kytea
    """

    tokens = mk.getAllTags(text)
    return tokens
