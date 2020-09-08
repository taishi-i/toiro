import fugashi

tagger = fugashi.Tagger()


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
    Return the analysis results by fugashi with unidic-lite.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        A list of fugashi.fugashi.Node
    """

    tokens = tagger(text)
    return tokens
