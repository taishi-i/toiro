import imp
import pkg_resources

imp.reload(pkg_resources)


try:
    import nagisa
    _nagisa_available = True
    _nagisa_version = nagisa.__version__
except:
    _nagisa_available = False
    _nagisa_version = False


try:
    from janome import version
    _janome_available = True
    _janome_version = version.JANOME_VERSION
except:
    _janome_available = False
    _janome_version = False


try:
    import MeCab
    _mecab_available = True
    _mecab_version = MeCab.VERSION
except:
    _mecab_available = False
    _mecab_version = False


try:
    import sudachipy
    from sudachipy import tokenizer
    from sudachipy import dictionary

    _sudachipy_available = True
    _sudachipy_version = sudachipy.__version__
except:
    _sudachipy_available = False
    _sudachipy_version = False


try:
    import spacy
    from spacy.lang.ja import Japanese
    nlp = Japanese()
    _spacy_available = True
    _spacy_version = spacy.__version__
except:
    _spacy_available = False
    _spacy_version = False


try:
    import spacy
    nlp = spacy.load('ja_ginza')
    _ginza_available = True

    _ginza_version = spacy.__version__
except:
    _ginza_available = False
    _ginza_version = False


try:
    import Mykytea
    mk = Mykytea.Mykytea("")
    _kytea_available = True
    _kytea_version = "0.1.5"
except:
    _kytea_available = False
    _kytea_version = False


try:
    from pyknp import Juman
    jumanpp = Juman()
    _jumanpp_available = True
    _jumanpp_version = "0.4.1"
except:
    _jumanpp_available = False
    _jumanpp_version = False


try:
    import sentencepiece as spm
    _sentencepiece_available = True
    _sentencepiece_version = "0.1.91"
except:
    _sentencepiece_available = False
    _sentencepiece_version = False


try:
    import ipadic
    import fugashi
    _fugashi_ipadic_available = True
    _fugashi_ipadic_version = "1.0.4"
except:
    _fugashi_ipadic_available = False
    _fugashi_ipadic_version = False


try:
    import tinysegmenter
    _tinysegmenter_available = True
    _tinysegmenter_version = "0.1.0"
except:
    _tinysegmenter_available = False
    _tinysegmenter_version = False


try:
    import fugashi
    import unidic_lite
    _fugashi_unidic_available = True
    _fugashi_unidic_version = "1.0.4"
except:
    _fugashi_unidic_available = False
    _fugashi_unidic_version = False


def is_mecab_available():
    """
    Check if the library is available.

    This function checks if mecab-python3 is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _mecab_available : bool
        If True, mecab is available in your environment.

    Examples
    --------
    >>> tokenizers.is_mecab_available()
    True

    """
    return _mecab_available


def is_nagisa_available():
    """
    Check if the library is available.

    This function checks if nagisa is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _nagisa_available : bool
        If True, nagisa is available in your environment.

    Examples
    --------
    >>> tokenizers.is_nagisa_available()
    True

    """
    return _nagisa_available


def is_janome_available():
    """
    Check if the library is available.

    This function checks if Janome is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _janome_available : bool
        If True, janome is available in your environment.

    Examples
    --------
    >>> tokenizers.is_janome_available()
    True

    """
    return _janome_available


def is_sudachipy_available():
    """
    Check if the library is available.

    This function checks if Janome is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _sudachipy_available : bool
        If True, sudachipy is available in your environment.

    Examples
    --------
    >>> tokenizers.is_sudachipy_available()
    True

    """
    return _sudachipy_available


def is_spacy_available():
    """
    Check if the library is available.

    This function checks if spacy is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _spacy_available : bool
        If True, spacy is available in your environment.

    Examples
    --------
    >>> tokenizers.is_spacy_available()
    True

    """
    return _spacy_available


def is_ginza_available():
    """
    Check if the library is available.

    This function checks if spacy is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _ginza_available : bool
        If True, ginza is available in your environment.

    Examples
    --------
    >>> tokenizers.is_ginza_available()
    True

    """
    return _ginza_available


def is_kytea_available():
    """
    Check if the library is available.

    This function checks if kytea is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _kytea_available : bool
        If True, kytea is available in your environment.

    Examples
    --------
    >>> tokenizers.is_kytea_available()
    True

    """
    return _kytea_available


def is_jumanpp_available():
    """
    Check if the library is available.

    This function checks if jumanpp is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _jumanpp_available : bool
        If True, Juman++ is available in your environment.

    Examples
    --------
    >>> tokenizers.is_jumanpp_available()
    True

    """
    return _jumanpp_available


def is_sentencepiece_available():
    """
    Check if the library is available.

    This function checks if sentencepiece is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _sentencepiece_available : bool
        If True, sentencepiece is available in your environment.

    Examples
    --------
    >>> tokenizers.is_sentencepiece_available()
    True

    """
    return _sentencepiece_available


def is_fugashi_ipadic_available():
    """
    Check if the library is available.

    This function checks if sentencepiece is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _fugashi_ipadic_available : bool
        If True, fugashi wiht ipadic is available in your environment.

    Examples
    --------
    >>> tokenizers.is_fugashi_ipadic_available()
    True

    """

    return _fugashi_ipadic_available


def is_tinysegmenter_available():
    """
    Check if the library is available.

    This function checks if tinysegmenter is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _tinysegmenter_available : bool
        If True, tinysegmenter is available in your environment.

    Examples
    --------
    >>> tokenizers.is_tinysegmenter_available()
    True

    """

    return _tinysegmenter_available


def is_fugashi_unidic_available():
    """
    Check if the library is available.

    This function checks if sentencepiece is available in your environment
    and returns the result as a bool value.

    Returns
    -------
    _fugashi_unidic_available : bool
        If True, fugashi wiht unidic is available in your environment.

    Examples
    --------
    >>> tokenizers.is_fugashi_unidic_available()
    True

    """

    return _fugashi_unidic_available


def available_tokenizers():
    """
    Return a list of available libraries.

    This function returns a list of the libraries supported by this library.

    Returns
    -------
    available_tokenizers_dict : bool
         A list of available libraries as dictionary

    Examples
    --------
    >>> tokenizers.available_tokenizers()
    """
    available_tokenizers_dict = {
        "nagisa": {
            "is_available": is_nagisa_available(),
            "version": _nagisa_version
        },
        "janome": {
            "is_available": is_janome_available(),
            "version": _janome_version
        },
        "mecab-python3": {
            "is_available": is_mecab_available(),
            "version": _mecab_version
        },
        "sudachipy": {
            "is_available": is_sudachipy_available(),
            "version": _sudachipy_version
        },
        "spacy": {
            "is_available": is_spacy_available(),
            "version": _spacy_version
        },
        "ginza": {
            "is_available": is_ginza_available(),
            "version": _ginza_version
        },
        "kytea": {
            "is_available": is_kytea_available(),
            "version": _kytea_version
        },
        "jumanpp": {
            "is_available": is_jumanpp_available(),
            "version": _jumanpp_version
        },
        "sentencepiece": {
            "is_available": is_sentencepiece_available(),
            "version": _sentencepiece_version
        },
        "fugashi-ipadic": {
            "is_available": is_fugashi_ipadic_available(),
            "version": _fugashi_ipadic_version
        },
        "tinysegmenter": {
            "is_available": is_tinysegmenter_available(),
            "version": _tinysegmenter_version
        },
        "fugashi-unidic": {
            "is_available": is_fugashi_unidic_available(),
            "version": _fugashi_unidic_version
        }
    }
    return available_tokenizers_dict
