# toiro ドキュメント

<p align="center"><img width="50%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.png?raw=true" /></p>

**toiro**（といろ）は *日本語の各種トークナイザ* を比較するための Python パッケージです。
以下のことができます。

- トークナイザの **処理速度を比較**
- トークナイザごとの **分かち書き結果を比較**
- **アプリケーションタスク（例: テキスト分類）での性能比較**
- 日本語 NLP の補助機能（**コーパスのダウンロード/前処理、簡易分類器** など）

<p align="center"><img width="90%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.gif?raw=true" /></p>

## 主な機能

### 対応トークナイザ
13種類の日本語トークナイザと BPE をサポート：

- janome（デフォルト搭載）
- nagisa
- mecab-python3
- sudachipy
- spacy
- ginza
- kytea
- jumanpp
- sentencepiece
- fugashi (ipadic/unidic)
- tinysegmenter
- tiktoken (GPT-4o / GPT-5 用 BPE)

### リンク

👉 **プロジェクト本体**: <https://github.com/taishi-i/toiro>
👉 **デモ（Hugging Face Spaces）**: <https://huggingface.co/spaces/taishi-i/Japanese-Tokenizer-Comparison>
👉 **PyPI**: <https://pypi.org/project/toiro/>

!!! tip "対応 Python バージョン"
    Python 3.10 以上を推奨。

!!! info "ライセンス"
    toiro は Apache License 2.0 の下で提供されています。

---

このドキュメントサイトは [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) によって生成されています。
