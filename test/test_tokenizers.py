import toiro

from toiro import tokenizers
from toiro import datadownloader


text = "Python で前処理を"


def test_janome():
    if tokenizers.is_janome_available():
        expected = ['Python', ' ', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_janome(text)
        assert words == expected

        tokens = tokenizers.original_janome(text)
        assert type(tokens) == list
    else:
        assert tokenizers.is_janome_available() is False


def test_nagisa():
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
    if tokenizers.is_sudachipy_available():
        expected = ['Python', ' ', 'で', '前処理', 'を']
        words = tokenizers.tokenize_sudachipy(text)
        assert words == expected

        tokens = tokenizers.original_sudachipy(text)
        assert str(type(tokens)) == "<class 'sudachipy.morphemelist.MorphemeList'>"
    else:
        assert tokenizers.is_sudachipy_available() is False


def test_mecab():
    if tokenizers.is_mecab_available():
        expected = ['Python', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_mecab(text)
        assert words == expected

        tokens = tokenizers.original_mecab(text)
        assert type(tokens) == str
    else:
        assert tokenizers.is_mecab_available() is False


def test_spacy():
    if tokenizers.is_spacy_available():
        expected = ['Python', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_spacy(text)
        assert words == expected

        tokens = tokenizers.original_spacy(text)
        assert str(type(tokens)) == "<class 'spacy.tokens.doc.Doc'>"
    else:
        assert tokenizers.is_spacy_available() is False


def test_ginza():
    if tokenizers.is_ginza_available():
        expected = ['Python', 'で', '前処理', 'を']
        words = tokenizers.tokenize_ginza(text)
        assert words == expected

        tokens = tokenizers.original_ginza(text)
        assert str(type(tokens)) == "<class 'spacy.tokens.doc.Doc'>"
    else:
        assert tokenizers.is_ginza_available() is False


def test_kytea():
    if tokenizers.is_kytea_available():
        expected = ['Python', ' ', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_kytea(text)

        tokenizers.original_kytea(text)
        assert words == expected
    else:
        assert tokenizers.is_kytea_available() is False


def test_jumanpp():
    if tokenizers.is_jumanpp_available():
        expected = ['Python', '\u3000', 'で', '前', '処理', 'を']
        words = tokenizers.tokenize_jumanpp(text)
        assert words == expected

        tokens = tokenizers.original_jumanpp(text)
        assert str(type(tokens)) == "<class 'pyknp.juman.mlist.MList'>"
    else:
        assert tokenizers.is_jumanpp_available() is False


def test_sentencepiece():
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


def test_compare():
    texts = [text]
    report = tokenizers.compare(texts)
    assert type(report) == dict


def test_compare_from_file():
    filename = datadownloader.sample_datasets.sample_txt
    report = tokenizers.compare_from_file(filename)
    print(report)
    assert type(report) == dict


def test_compare_from_file_with_disable_tokenizers():
    filename = datadownloader.sample_datasets.sample_txt
    report = tokenizers.compare_from_file(
        filename, disable_tokenizers=["nagisa"]
    )
    print(report)
    assert type(report) == dict


def test_print_words():
    tokenizers.print_words(text)


def test_print_words_with_disable_tokenizers():
    tokenizers.print_words(text, disable_tokenizers=["nagisa"])
