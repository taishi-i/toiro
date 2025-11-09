# Installation

## Requirements
- Python 3.10 or later

## Basic install
```bash
pip install toiro
```

`toiro` ships with a minimal setup, and **[Janome](https://github.com/mocobeta/janome)** is available by default.

## Add extra tokenizers

Install additional tokenizers individually, e.g., SudachiPy and nagisa:

```bash
pip install sudachipy sudachidict_core
pip install nagisa
```

### Other tokenizers

```bash
# MeCab (mecab-python3)
pip install mecab-python3

# spaCy Japanese / GiNZA
pip install spacy ginza
pip install "spacy[ja]"

# KyTea (requires system install)
# After installing KyTea by its official instructions:
pip install kytea

# Juman++ v2 (requires system install)
# After installing Juman++ v2 by its official instructions:
pip install pyknp

# SentencePiece
pip install sentencepiece

# fugashi + IPADIC / UniDic
pip install fugashi ipadic
pip install fugashi unidic-lite

# TinySegmenter
pip install tinysegmenter3

# tiktoken (BPE for GPT-4o / GPT-5)
pip install tiktoken
```

!!! tip "Install all at once"
    To try all tokenizers at once:
    ```bash
    pip install "toiro[all_tokenizers]"
    ```

!!! note "System-level installation required"
    KyTea and Juman++ require system-level installation before installing the Python package. Please refer to their official documentation for details.

## Using Docker

A Docker image with all tokenizers pre-installed is available:

```bash
docker run --rm -it taishii/toiro /bin/bash
```

See [Docker Hub](https://hub.docker.com/r/taishii/toiro) for details.

## Add classifiers (optional)

To use BERT-based text classifiers:

```bash
pip install "toiro[all_classifiers]"
```

Or install individually:

```bash
pip install torch transformers catalyst
```
