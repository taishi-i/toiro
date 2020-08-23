from janome.tokenizer import Tokenizer

# Initialize Janome
t = Tokenizer()


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
    words = list(t.tokenize(text, wakati=True))
    return words


def original_usage(text):
    """
    Return the analysis results by Janome.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        The analysis results by Janome
    """
    tokens = list(t.tokenize(text))
    return tokens
