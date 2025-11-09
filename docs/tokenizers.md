# トークナイザ一覧

toiro でサポートしている日本語トークナイザと BPE モデルの一覧です。

## 形態素解析ベースのトークナイザ

### [Janome](https://github.com/mocobeta/janome)
- **種類**: 形態素解析
- **辞書**: MeCab IPADIC
- **特徴**: Pure Python 実装、外部依存なし
- **デフォルト**: toiro に標準で含まれる

### [nagisa](https://github.com/taishi-i/nagisa)
- **種類**: RNN ベース
- **特徴**: 品詞タグ付けと固有表現抽出もサポート

### [mecab-python3](https://github.com/SamuraiT/mecab-python3)
- **種類**: 形態素解析
- **辞書**: MeCab IPADIC
- **特徴**: MeCab の Python バインディング

### [SudachiPy](https://github.com/WorksApplications/SudachiPy)
- **種類**: 形態素解析
- **辞書**: Sudachi 辞書
- **特徴**: 複数の分割モード（A/B/C）、同義語展開

### [spaCy](https://github.com/explosion/spaCy)
- **種類**: 統計モデルベース
- **特徴**: 固有表現認識、依存構造解析など多機能

### [GiNZA](https://github.com/megagonlabs/ginza)
- **種類**: spaCy の日本語モデル
- **特徴**: Universal Dependencies 準拠、固有表現認識

### [KyTea](https://github.com/neubig/kytea)
- **種類**: 点予測ベース
- **特徴**: 読み推定機能
- **注意**: システムレベルのインストールが必要

### [Juman++](https://github.com/ku-nlp/jumanpp)
- **種類**: 形態素解析
- **辞書**: JUMAN 辞書
- **特徴**: RNN による再順位付け
- **注意**: システムレベルのインストールが必要（pyknp 経由で使用）

### [fugashi](https://github.com/polm/fugashi)
- **種類**: MeCab の Cython ラッパー
- **辞書**: IPADIC または UniDic
- **特徴**: 高速な MeCab Python バインディング

### [TinySegmenter](https://github.com/SamuraiT/tinysegmenter)
- **種類**: コンパクトな分かち書き
- **特徴**: 軽量、辞書不要

## サブワードトークナイザ

### [SentencePiece](https://github.com/google/sentencepiece)
- **種類**: BPE / Unigram
- **特徴**: 言語非依存、ニューラル機械翻訳向け

### [tiktoken](https://github.com/openai/tiktoken)
- **種類**: BPE
- **モデル**: GPT-4o / GPT-5
- **特徴**: OpenAI モデル用トークナイザ

## トークナイザの選び方

| 用途 | おすすめ |
|------|----------|
| 手軽に始めたい | Janome（依存なし） |
| 高速処理 | MeCab, fugashi, SudachiPy |
| 固有表現認識も必要 | GiNZA, spaCy |
| ニューラル機械翻訳 | SentencePiece |
| OpenAI モデルと統合 | tiktoken |

!!! warning "システムレベルのインストールが必要"
    KyTea と Juman++ は、Python パッケージをインストールする前にシステムレベルでのインストールが必要です。詳細は各プロジェクトの公式ドキュメントを参照してください。
