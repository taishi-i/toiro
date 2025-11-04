# Corpora & Data

Examples of corpora provided by `toiro.datadownloader`:

- `livedoor_news_corpus`
- `yahoo_movie_reviews`
- `amazon_reviews`

## Usage
```python
from toiro import datadownloader

print(datadownloader.available_corpus())
datadownloader.download_corpus("livedoor_news_corpus")
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")
```
