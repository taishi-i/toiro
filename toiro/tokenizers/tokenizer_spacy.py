from spacy.lang.ja import Japanese

# Load SudachiPy with split mode A (default)
nlp = Japanese()


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
    doc = nlp.make_doc(text)
    words = [w.text for w in doc]
    return words


def original_usage(text):
    """
    Return the analysis results by spacy.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : spacy.tokens.doc.Doc
        The analysis results by spacy
    """
    tokens = nlp(text)
    return tokens
