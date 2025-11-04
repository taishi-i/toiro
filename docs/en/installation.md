# Installation

## Requirements
- Python 3.10+

## Basic install
```bash
pip install toiro
```

`toiro` ships with a minimal setup, and **Janome** is available by default.

## Add extra tokenizers

Install additional tokenizers individually, e.g., SudachiPy and nagisa:

```bash
pip install sudachipy sudachidict_core
pip install nagisa
```

More examples:

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

# BPE: tiktoken
pip install tiktoken
```

Try many at once:

```bash
pip install "toiro[all_tokenizers]"
```
