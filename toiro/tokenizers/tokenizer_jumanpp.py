from pyknp import Juman

jumanpp = Juman()


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

    # Error avoidance for long text
    text = text[:1024]

    # Error avoidance for space
    text = text.replace(' ', '　')

    result = jumanpp.analysis(text)
    words = [mrph.midasi for mrph in result.mrph_list()]
    return words


def original_usage(text):
    """
    Return the analysis results by Juman++.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : pyknp.juman.mlist.MList
        The analysis results by Juman++
    """

    # Error avoidance for long text
    text = text[:1024]

    # Error avoidance for space
    text = text.replace(' ', '　')

    tokens = jumanpp.analysis(text)
    return tokens
