# Tokenizers

List of Japanese tokenizers and BPE models supported by toiro.

## Morphological Analysis Tokenizers

### [Janome](https://github.com/mocobeta/janome)
- **Type**: Morphological analyzer
- **Dictionary**: MeCab IPADIC
- **Features**: Pure Python implementation, no external dependencies
- **Default**: Included in toiro by default

### [nagisa](https://github.com/taishi-i/nagisa)
- **Type**: RNN-based
- **Features**: Supports POS tagging and named entity extraction

### [mecab-python3](https://github.com/SamuraiT/mecab-python3)
- **Type**: Morphological analyzer
- **Dictionary**: MeCab IPADIC
- **Features**: Python binding for MeCab

### [SudachiPy](https://github.com/WorksApplications/SudachiPy)
- **Type**: Morphological analyzer
- **Dictionary**: Sudachi dictionary
- **Features**: Multiple split modes (A/B/C), synonym expansion

### [spaCy](https://github.com/explosion/spaCy)
- **Type**: Statistical model-based
- **Features**: Multi-functional including NER, dependency parsing

### [GiNZA](https://github.com/megagonlabs/ginza)
- **Type**: Japanese model for spaCy
- **Features**: Universal Dependencies compliant, NER

### [KyTea](https://github.com/neubig/kytea)
- **Type**: Pointwise prediction-based
- **Features**: Pronunciation estimation
- **Note**: Requires system-level installation

### [Juman++](https://github.com/ku-nlp/jumanpp)
- **Type**: Morphological analyzer
- **Dictionary**: JUMAN dictionary
- **Features**: RNN-based re-ranking
- **Note**: Requires system-level installation (used via pyknp)

### [fugashi](https://github.com/polm/fugashi)
- **Type**: Cython wrapper for MeCab
- **Dictionary**: IPADIC or UniDic
- **Features**: Fast MeCab Python binding

### [TinySegmenter](https://github.com/SamuraiT/tinysegmenter)
- **Type**: Compact tokenizer
- **Features**: Lightweight, dictionary-free

## Subword Tokenizers

### [SentencePiece](https://github.com/google/sentencepiece)
- **Type**: BPE / Unigram
- **Features**: Language-independent, designed for neural machine translation

### [tiktoken](https://github.com/openai/tiktoken)
- **Type**: BPE
- **Models**: GPT-4o / GPT-5
- **Features**: Tokenizer for OpenAI models

## Choosing a Tokenizer

| Use Case | Recommendation |
|----------|----------------|
| Easy to start | Janome (no dependencies) |
| High-speed processing | MeCab, fugashi, SudachiPy |
| Need NER | GiNZA, spaCy |
| Neural machine translation | SentencePiece |
| Integration with OpenAI models | tiktoken |

!!! warning "System-level installation required"
    KyTea and Juman++ require system-level installation before installing the Python package. Please refer to their official documentation for details.
