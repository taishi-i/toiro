import MeCab

# Initialize mecab-python3
wakati = MeCab.Tagger("-Owakati")
tagger = MeCab.Tagger()


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
    words = wakati.parse(text).split()
    return words


def original_usage(text):
    """
    Return the analysis results by mecab-python3.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : str
        The default analysis results by mecab-python3
    """
    tokens = tagger.parse(text)
    return tokens
