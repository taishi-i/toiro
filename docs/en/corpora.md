# Corpora & Data

The `toiro.datadownloader` module provides easy access to Japanese text classification corpora.

## Available Corpora

### livedoor News Corpus
- **Task**: Text classification (news category)
- **Categories**: 9 categories
- **Categories**: Topic News, Sports Watch, IT Life Hack, Kaden Channel, MOVIE ENTER, Dokujo Tsushin, S-MAX, livedoor HOMME, Peachy
- **Source**: [livedoor News Corpus](https://www.rondhuit.com/download.html)

### Yahoo! Movie Reviews
- **Task**: Sentiment analysis (positive/negative)
- **Domain**: Movie reviews
- **Format**: Review text and rating scores

### Amazon Reviews
- **Task**: Sentiment analysis (positive/negative)
- **Domain**: Product reviews
- **Format**: Review text and rating scores

## Basic Usage

### List available corpora
```python
from toiro import datadownloader

corpora = datadownloader.available_corpus()
print(corpora)
# => ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']
```

### Download a corpus
```python
datadownloader.download_corpus("livedoor_news_corpus")
```

Corpora are downloaded to the `~/.toiro/` directory.

### Load a corpus
```python
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")

# Check data
print(f"Train: {len(train_df)} samples")
print(f"Dev: {len(dev_df)} samples")
print(f"Test: {len(test_df)} samples")

# Data structure (pandas DataFrame)
# Column 0: label
# Column 1: text
texts = train_df[1].tolist()
labels = train_df[0].tolist()
```

## Data Preprocessing

Downloaded corpora are provided as pandas DataFrames, pre-split into train/dev/test sets.

```python
# Example: Extract texts only for tokenizer evaluation
texts = train_df[1].tolist()

# Example: Extract labels and texts for classifier training
X_train = train_df[1].tolist()
y_train = train_df[0].tolist()
```

!!! info "Data storage location"
    Downloaded corpora are saved in the `~/.toiro/` directory. Once downloaded, you can load them directly with `load_corpus()`.
