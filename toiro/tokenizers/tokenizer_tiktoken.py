import tiktoken

enc_gpt4o = tiktoken.encoding_for_model("gpt-4o")
enc_gpt5 = tiktoken.encoding_for_model("gpt-5")


def token_ids_to_tokens(token_ids, enc):
    tokens = []
    for token_id in token_ids:
        try:
            token_bytes = enc.decode_bytes([token_id])
            token_str = token_bytes.decode("utf-8", errors="replace")
        except Exception:
            token_str = "<INVALID>"
        tokens.append(token_str)
    return tokens


def tokenize_gpt4o(text):
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
    token_ids = enc_gpt4o.encode(text)
    tokens = token_ids_to_tokens(token_ids, enc_gpt4o)
    return tokens


def original_usage_gpt4o(text):
    """
    Return the analysis results by tiktoken for gpt-4o.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        A list of words
    """
    tokens = tokenize_gpt4o(text)
    return tokens


def tokenize_gpt5(text):
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
    token_ids = enc_gpt5.encode(text)
    tokens = token_ids_to_tokens(token_ids, enc_gpt5)
    return tokens


def original_usage_gpt5(text):
    """
    Return the analysis results by tiktoken for gpt-5.

    Parameters
    ----------
    text : str
        An input text

    Returns
    -------
    tokens : list
        A list of words
    """
    tokens = tokenize_gpt5(text)
    return tokens
