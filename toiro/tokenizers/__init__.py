from .tokenizer_utils import (
    is_nagisa_available,
    is_janome_available,
    is_mecab_available,
    is_sudachipy_available,
    is_spacy_available,
    is_ginza_available,
    is_kytea_available,
    is_jumanpp_available,
    is_sentencepiece_available,
    is_fugashi_ipadic_available,
    is_tinysegmenter_available,
    is_fugashi_unidic_available,
    available_tokenizers
)


if is_nagisa_available():
    from .tokenizer_nagisa import tokenize as tokenize_nagisa
    from .tokenizer_nagisa import original_usage as original_nagisa


if is_janome_available():
    from .tokenizer_janome import tokenize as tokenize_janome
    from .tokenizer_janome import original_usage as original_janome


if is_mecab_available():
    from .tokenizer_mecab_python3 import tokenize as tokenize_mecab
    from .tokenizer_mecab_python3 import original_usage as original_mecab


if is_sudachipy_available():
    from .tokenizer_sudachipy import tokenize as tokenize_sudachipy
    from .tokenizer_sudachipy import original_usage as original_sudachipy


if is_spacy_available():
    from .tokenizer_spacy import tokenize as tokenize_spacy
    from .tokenizer_spacy import original_usage as original_spacy


if is_ginza_available():
    from .tokenizer_ginza import tokenize as tokenize_ginza
    from .tokenizer_ginza import original_usage as original_ginza


if is_kytea_available():
    from .tokenizer_kytea import tokenize as tokenize_kytea
    from .tokenizer_kytea import original_usage as original_kytea


if is_jumanpp_available():
    from .tokenizer_jumanpp import tokenize as tokenize_jumanpp
    from .tokenizer_jumanpp import original_usage as original_jumanpp


if is_sentencepiece_available():
    from .tokenizer_sentencepiece import tokenize as tokenize_sentencepiece
    from .tokenizer_sentencepiece import original_usage as original_sentencepiece


if is_fugashi_ipadic_available():
    from .tokenizer_fugashi_ipadic import tokenize as tokenize_fugashi_ipadic
    from .tokenizer_fugashi_ipadic import original_usage as original_fugashi_ipadic


if is_tinysegmenter_available():
    from .tokenizer_tinysegmenter import tokenize as tokenize_tinysegmenter
    from .tokenizer_tinysegmenter import original_usage as original_tinysegmenter


if is_fugashi_unidic_available():
    from .tokenizer_fugashi_unidic import tokenize as tokenize_fugashi_unidic
    from .tokenizer_fugashi_unidic import original_usage as original_fugashi_unidic


from .tokenizer_report import (
    compare,
    compare_from_file,
    print_words,
    SelectTokenizer,
    get_avaiable_tokenizers
)
