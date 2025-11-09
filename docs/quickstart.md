# クイックスタート

## 利用可能なトークナイザの確認

環境にインストールされているトークナイザを確認：

```python
from toiro import tokenizers

available = tokenizers.available_tokenizers()
print(available)
```

**出力例**:
```python
{
 'nagisa': {'is_available': True, 'version': '0.2.7'},
 'janome': {'is_available': True, 'version': '0.3.10'},
 'mecab-python3': {'is_available': False, 'version': False},
 'sudachipy': {'is_available': True, 'version': '0.6.8'},
 'spacy': {'is_available': False, 'version': False},
 'ginza': {'is_available': False, 'version': False},
 'kytea': {'is_available': False, 'version': False},
 'jumanpp': {'is_available': False, 'version': False},
 'sentencepiece': {'is_available': False, 'version': False},
 'fugashi-ipadic': {'is_available': False, 'version': False},
 'fugashi-unidic': {'is_available': False, 'version': False},
 'tinysegmenter': {'is_available': False, 'version': False},
 'tiktoken': {'is_available': False, 'version': False}
}
```

## 分かち書き結果の比較

同じテキストを異なるトークナイザで分割し、結果を比較：

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

## コーパスのダウンロードと読み込み

日本語テキスト分類データセットをダウンロード：

```python
from toiro import datadownloader

# 利用可能なコーパスの確認
corpora = datadownloader.available_corpus()
print(corpora)
# => ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']

# コーパスのダウンロード
corpus = corpora[0]
datadownloader.download_corpus(corpus)

# データの読み込み
train_df, dev_df, test_df = datadownloader.load_corpus(corpus)
texts = train_df[1].tolist()
```

## 速度ベンチマークの実行

複数のトークナイザで同じテキストを処理し、処理速度を比較：

```python
from toiro import tokenizers

report = tokenizers.compare(texts)
print(report)
```

**出力例**:
```
[1/3] Tokenizer: janome
100%|███████████████████| 5900/5900 [00:07<00:00, 746.21it/s]
[2/3] Tokenizer: nagisa
100%|███████████████████| 5900/5900 [00:15<00:00, 370.83it/s]
[3/3] Tokenizer: sudachipy
100%|███████████████████| 5900/5900 [00:08<00:00, 696.68it/s]

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

## 次のステップ

- [トークナイザ一覧](tokenizers.md) - 対応トークナイザの詳細
- [ベンチマーク](benchmarks.md) - より詳細な比較方法
- [API リファレンス](api.md) - 完全な API ドキュメント
