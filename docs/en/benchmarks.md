# Benchmarks

toiro provides utilities to compare tokenizers from three perspectives.

## 1. Speed Comparison

Process the same texts with multiple tokenizers and measure execution time.

```python
from toiro import tokenizers
from toiro import datadownloader

# Download a corpus
datadownloader.download_corpus("livedoor_news_corpus")
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")
texts = train_df[1].tolist()

# Run speed comparison
report = tokenizers.compare(texts)
print(report)
```

**Example output**:
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

## 2. Segmentation Comparison

Visually compare how each tokenizer segments the same text.

```python
from toiro import tokenizers

text = "都庁所在地は新宿区。"
tokenizers.print_words(text, delimiter="|")
```

**Example output**:
```
       janome: 都庁|所在地|は|新宿|区|。
       nagisa: 都庁|所在|地|は|新宿|区|。
    sudachipy: 都庁|所在地|は|新宿区|。
```

### Detailed Comparison

You can also select a specific tokenizer for detailed analysis:

```python
from toiro.tokenizers import SelectTokenizer

# Select a specific tokenizer
tokenizer = SelectTokenizer("sudachipy")
tokens = tokenizer.tokenize("都庁所在地は新宿区。")
print(tokens)
```

## 3. Application Task Performance

Evaluate tokenizer performance on real application tasks (e.g., text classification).

### Classification with SVM

```python
from toiro import tokenizers, datadownloader
from toiro.classifiers import SVMClassificationModel

# Prepare data
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")

# Select a tokenizer
tokenizer = tokenizers.SelectTokenizer("janome")

# Train and evaluate with SVM
model = SVMClassificationModel(tokenizer)
model.train(train_df)
metrics = model.evaluate(test_df)
print(metrics)
```

### Classification with BERT

```python
from toiro.classifiers import BERTClassificationModel

# Train and evaluate with BERT (requires: torch, transformers, catalyst)
model = BERTClassificationModel("cl-tohoku/bert-base-japanese")
model.train(train_df, dev_df, epochs=3)
metrics = model.evaluate(test_df)
print(metrics)
```

## Saving Benchmark Results

You can also compare directly from a file:

```python
from toiro import tokenizers

# Compare from file
report = tokenizers.compare_from_file("path/to/textfile.txt")
print(report)
```

!!! tip "Performance Tips"
    - For large text volumes, MeCab, fugashi, and SudachiPy are fastest
    - For memory efficiency, Janome or TinySegmenter are recommended
    - For accuracy-focused tasks, consider GiNZA or BERT-based models

!!! info "Detailed Examples"
    For more detailed usage examples, see the [examples directory on GitHub](https://github.com/taishi-i/toiro/tree/master/examples).
