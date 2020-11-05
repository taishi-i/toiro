from toiro import tokenizers
from toiro import datadownloader

text = "Python で前処理を"


def test_janome():
    """
    Tokenizes the tokenizer isjan.

    Args:
    """
    if tokenizers.is_janome_available():
        expected = ['Python', ' ', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_janome(text)
        assert words == expected

        tokens = tokenizers.original_janome(text)
        assert type(tokens) == list
    else:
        assert tokenizers.is_janome_available() is False


def test_nagisa():
    """
    Tokenize the nagisa exists.

    Args:
    """
    if tokenizers.is_nagisa_available():
        expected = ['Python', '\u3000', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_nagisa(text)
        assert words == expected

        expected = 'Python/名詞 \u3000/空白 で/助詞 前/名詞 処理/名詞 を/助詞'
        tokens = str(tokenizers.original_nagisa(text))
        assert tokens == expected
    else:
        assert tokenizers.is_nagisa_available() is False


def test_sudachipy():
    """
    Test if the test token is a test.

    Args:
    """
    if tokenizers.is_sudachipy_available():
        expected = ['Python', ' ', 'で', '前処理', 'を']
        words = tokenizers.tokenize_sudachipy(text)
        assert words == expected

        tokens = tokenizers.original_sudachipy(text)
        expected = "<class 'sudachipy.morphemelist.MorphemeList'>"
        assert str(type(tokens)) == expected
    else:
        assert tokenizers.is_sudachipy_available() is False


def test_mecab():
    """
    Tokenize the mecab.

    Args:
    """
    if tokenizers.is_mecab_available():
        expected = ['Python', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_mecab(text)
        assert words == expected

        tokens = tokenizers.original_mecab(text)
        assert type(tokens) == str
    else:
        assert tokenizers.is_mecab_available() is False


def test_spacy():
    """
    Test if spacy spacy spacy.

    Args:
    """
    if tokenizers.is_spacy_available():
        expected = ['Python', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_spacy(text)
        assert words == expected

        tokens = tokenizers.original_spacy(text)
        assert str(type(tokens)) == "<class 'spacy.tokens.doc.Doc'>"
    else:
        assert tokenizers.is_spacy_available() is False


def test_ginza():
    """
    Check if the test tokenizer.

    Args:
    """
    if tokenizers.is_ginza_available():
        expected = ['Python', 'で', '前処理', 'を']
        words = tokenizers.tokenize_ginza(text)
        assert words == expected

        tokens = tokenizers.original_ginza(text)
        assert str(type(tokens)) == "<class 'spacy.tokens.doc.Doc'>"
    else:
        assert tokenizers.is_ginza_available() is False


def test_kytea():
    """
    Test if the tetea exists.

    Args:
    """
    if tokenizers.is_kytea_available():
        expected = ['Python', ' ', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_kytea(text)

        tokenizers.original_kytea(text)
        assert words == expected
    else:
        assert tokenizers.is_kytea_available() is False


def test_jumanpp():
    """
    Test if the juman token.

    Args:
    """
    if tokenizers.is_jumanpp_available():
        expected = ['Python', '\u3000', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_jumanpp(text)
        assert words == expected

        tokens = tokenizers.original_jumanpp(text)
        assert str(type(tokens)) == "<class 'pyknp.juman.mlist.MList'>"
    else:
        assert tokenizers.is_jumanpp_available() is False


def test_sentencepiece():
    """
    Returns the sentence sentence.

    Args:
    """
    if tokenizers.is_sentencepiece_available():
        expected = ['▁', 'P', 'y', 'th', 'on', '▁', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_sentencepiece(text)
        assert words == expected

        expected = [
            ['▁', 'P', 'y', 'th', 'on', '▁', 'で', '前', '処理', 'を'],
            [5, 0, 210, 1040, 905, 5, 14, 144, 2828, 7]
        ]
        tokens = tokenizers.original_sentencepiece(text)
        assert tokens == expected
    else:
        assert tokenizers.is_sentencepiece_available() is False


def test_fugashi_ipadic():
    """
    Test if ipadic ipadic ipadic ipadic.

    Args:
    """
    if tokenizers.is_fugashi_ipadic_available():
        expected = ['Python', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_fugashi_ipadic(text)
        assert words == expected

        tokens = tokenizers.original_fugashi_ipadic(text)
        assert type(tokens) == list
    else:
        tokenizers.is_fugashi_ipadic_available() is False


def test_tinysegmenter():
    """
    Test if the next token in - wordser.

    Args:
    """
    if tokenizers.is_tinysegmenter_available():
        expected = ['Python', ' ', 'で', '前処', '理', 'を']
        words = tokenizers.tokenize_tinysegmenter(text)
        assert words == expected

        tokens = tokenizers.original_tinysegmenter(text)
        assert type(tokens) == list
    else:
        tokenizers.is_tinysegmenter_available() is False


def test_fugashi_unidic():
    """
    Decorizes unidic.

    Args:
    """
    if tokenizers.is_fugashi_unidic_available():
        expected = ['Python', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_fugashi_unidic(text)
        assert words == expected

        tokens = tokenizers.original_fugashi_unidic(text)
        assert type(tokens) == list
    else:
        tokenizers.is_fugashi_unidic_available() is False


def test_compare():
    """
    Compares the test reports.

    Args:
    """
    texts = [text]
    report = tokenizers.compare(texts)
    assert type(report) == dict


def test_compare_from_file():
    """
    Test if the test sets of the results.

    Args:
    """
    filename = datadownloader.sample_datasets.sample_txt
    report = tokenizers.compare_from_file(filename)
    print(report)
    assert type(report) == dict


def test_compare_from_file_with_disable_tokenizers():
    """
    Test if the test sets of test test set of the test.

    Args:
    """
    filename = datadownloader.sample_datasets.sample_txt
    report = tokenizers.compare_from_file(
        filename, disable_tokenizers=["nagisa"]
    )
    print(report)
    assert type(report) == dict


def test_print_words():
    """
    Print the list of the words.

    Args:
    """
    tokenizers.print_words(text)


def test_print_words_with_disable_tokenizers():
    """
    Prints out the tokenizers from the tokenizer.

    Args:
    """
    tokenizers.print_words(text, disable_tokenizers=["nagisa"])


def char_tokenize(text):
    """
    Tokenize a string.

    Args:
        text: (str): write your description
    """
    chars = list(text)
    return chars


def test_compare_with_additional_tokenizers():
    """
    Compares two texts in the document.

    Args:
    """
    texts = [text]

    additional_tokenizers = {"char": char_tokenize}

    report = tokenizers.compare(
        texts, additional_tokenizers=additional_tokenizers
    )
    assert type(report) == dict


def test_compare_from_file_with_additional_tokenizers():
    """
    Compares two sets of - dataset.

    Args:
    """
    filename = datadownloader.sample_datasets.sample_txt

    additional_tokenizers = {"char": char_tokenize}
    report = tokenizers.compare_from_file(
        filename, additional_tokenizers=additional_tokenizers
    )
    print(report)
    assert type(report) == dict


def test_print_words_with_additional_tokenizers():
    """
    Prints out a list of words in the text.

    Args:
    """
    additional_tokenizers = {"char": char_tokenize}
    tokenizers.print_words(text, additional_tokenizers=additional_tokenizers)
