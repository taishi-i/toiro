# ベンチマーク

toiro は以下の3つの観点でトークナイザを比較するユーティリティを提供します。

## 1. 処理速度の比較

複数のトークナイザで同じテキストを処理し、実行時間を計測します。

```python
from toiro import tokenizers
from toiro import datadownloader

# コーパスをダウンロード
datadownloader.download_corpus("livedoor_news_corpus")
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")
texts = train_df[1].tolist()

# 速度比較を実行
report = tokenizers.compare(texts)
print(report)
```

**出力例**:
```python
{
  'execution_environment': {
    'python_version': '3.10.0',
    'arch': 'X86_64',
    'brand_raw': 'Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz',
    'count': 8
  },
  'data': {
    'number_of_sentences': 5900,
    'average_length': 37.69
  },
  'janome': {'elapsed_time': 9.11},
  'nagisa': {'elapsed_time': 15.87},
  'sudachipy': {'elapsed_time': 9.05}
}
```

## 2. 分割結果の比較

同一テキストに対して各トークナイザがどのように分割するかを視覚的に比較します。

```python
from toiro import tokenizers

text = "都庁所在地は新宿区。"
tokenizers.print_words(text, delimiter="|")
```

**出力例**:
```
       janome: 都庁|所在地|は|新宿|区|。
       nagisa: 都庁|所在|地|は|新宿|区|。
    sudachipy: 都庁|所在地|は|新宿区|。
```

### より詳細な比較

特定のトークナイザを選択して、詳細な分析を行うことも可能です：

```python
from toiro.tokenizers import SelectTokenizer

# 特定のトークナイザを選択
tokenizer = SelectTokenizer("sudachipy")
tokens = tokenizer.tokenize("都庁所在地は新宿区。")
print(tokens)
```

## 3. アプリケーションタスクでの性能比較

実際のアプリケーションタスク（例: テキスト分類）でトークナイザの性能を評価します。

### SVM を使った分類

```python
from toiro import tokenizers, datadownloader
from toiro.classifiers import SVMClassificationModel

# データの準備
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")

# トークナイザを選択
tokenizer = tokenizers.SelectTokenizer("janome")

# SVM モデルで学習・評価
model = SVMClassificationModel(tokenizer)
model.train(train_df)
metrics = model.evaluate(test_df)
print(metrics)
```

### BERT を使った分類

```python
from toiro.classifiers import BERTClassificationModel

# BERT モデルで学習・評価（要: torch, transformers, catalyst）
model = BERTClassificationModel("cl-tohoku/bert-base-japanese")
model.train(train_df, dev_df, epochs=3)
metrics = model.evaluate(test_df)
print(metrics)
```

## ベンチマーク結果の保存

ファイルから直接比較することも可能です：

```python
from toiro import tokenizers

# ファイルから読み込んで比較
report = tokenizers.compare_from_file("path/to/textfile.txt")
print(report)
```

!!! tip "パフォーマンスのヒント"
    - 大量のテキストを処理する場合、MeCab、fugashi、SudachiPy が高速です
    - メモリ効率を重視する場合は Janome や TinySegmenter がおすすめです
    - 精度重視の場合は GiNZA や BERT ベースのモデルを検討してください

!!! info "詳細な例"
    より詳しい使用例は、[GitHub リポジトリの examples ディレクトリ](https://github.com/taishi-i/toiro/tree/master/examples)を参照してください。
