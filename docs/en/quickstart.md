# Quickstart

## Check available tokenizers
```python
from toiro import tokenizers

available = tokenizers.available_tokenizers()
print(available)
```

## Download and load a corpus
```python
from toiro import datadownloader

corpora = datadownloader.available_corpus()
print(corpora)  # e.g. ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']

corpus = corpora[0]
datadownloader.download_corpus(corpus)
train_df, dev_df, test_df = datadownloader.load_corpus(corpus)
texts = train_df[1].tolist()
```

## Run a speed benchmark
```python
from toiro import tokenizers

report = tokenizers.compare(texts)
print(report)
```
