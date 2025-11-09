# インストール

## 必須環境
- Python 3.10 以上

## 基本インストール
```bash
pip install toiro
```

`toiro` は最小構成でインストールされ、デフォルトでは **[Janome](https://github.com/mocobeta/janome)** が利用可能です。

## 追加トークナイザの導入

次のように個別にインストールしてください（例: SudachiPy と nagisa を追加）。

```bash
pip install sudachipy sudachidict_core
pip install nagisa
```

### その他のトークナイザ

```bash
# MeCab (mecab-python3)
pip install mecab-python3

# GiNZA / spaCy 日本語
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

# tiktoken（GPT-4o / GPT-5 用 BPE）
pip install tiktoken
```

!!! tip "すべてまとめてインストール"
    すべてのトークナイザを一度に試したい場合:
    ```bash
    pip install "toiro[all_tokenizers]"
    ```

!!! note "システムレベルのインストールが必要なツール"
    KyTea と Juman++ は、Python パッケージをインストールする前にシステムレベルでのインストールが必要です。詳細は各プロジェクトの公式ドキュメントを参照してください。

## Docker を使う

すべてのトークナイザがプリインストールされた Docker イメージも利用できます：

```bash
docker run --rm -it taishii/toiro /bin/bash
```

詳細は [Docker Hub](https://hub.docker.com/r/taishii/toiro) を参照してください。

## 分類器の追加（オプション）

BERT ベースのテキスト分類器を使いたい場合:

```bash
pip install "toiro[all_classifiers]"
```

または個別に:

```bash
pip install torch transformers catalyst
```
