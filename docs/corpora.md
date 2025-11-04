# コーパスとデータ

`toiro.datadownloader` が提供する利用可能コーパスの例:

- `livedoor_news_corpus`
- `yahoo_movie_reviews`
- `amazon_reviews`

## 使い方
```python
from toiro import datadownloader

print(datadownloader.available_corpus())
datadownloader.download_corpus("livedoor_news_corpus")
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")
```
