# インストール

## 必須環境
- Python 3.10+

## 基本インストール
```bash
pip install toiro
```

`toiro` は最小構成でインストールされ、デフォルトでは **Janome** が利用可能です。

## 追加トークナイザの導入

次のように個別にインストールしてください（例: SudachiPy と nagisa を追加）。

```bash
pip install sudachipy sudachidict_core
pip install nagisa
```

その他の例:

```bash
# MeCab (mecab-python3)
pip install mecab-python3

# GiNZA / spaCy日本語
pip install spacy ginza
pip install "spacy[ja]"

# KyTea（本体の導入が別途必要）
# 公式手順で KyTea を入れた上で:
pip install kytea

# Juman++ v2（本体の導入が別途必要）
# 公式手順で Juman++ v2 を入れた上で:
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

すべてまとめて試したい場合は以下も便利です。

```bash
pip install "toiro[all_tokenizers]"
```
