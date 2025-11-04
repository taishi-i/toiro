# クイックスタート

## 利用可能なトークナイザの確認
```python
from toiro import tokenizers

available = tokenizers.available_tokenizers()
print(available)
```

## コーパスのダウンロードと読み込み
```python
from toiro import datadownloader

corpora = datadownloader.available_corpus()
print(corpora)  # 例: ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']

corpus = corpora[0]
datadownloader.download_corpus(corpus)
train_df, dev_df, test_df = datadownloader.load_corpus(corpus)
texts = train_df[1].tolist()
```

## 速度ベンチマークの実行
```python
from toiro import tokenizers

report = tokenizers.compare(texts)
print(report)
```
