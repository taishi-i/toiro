# Quickstart

## Check available tokenizers

Check which tokenizers are installed in your environment:

```python
from toiro import tokenizers

available = tokenizers.available_tokenizers()
print(available)
```

**Example output**:
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

## Compare segmentation outputs

Tokenize the same text with different tokenizers and compare results:

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

## Download and load a corpus

Download a Japanese text classification dataset:

```python
from toiro import datadownloader

# Check available corpora
corpora = datadownloader.available_corpus()
print(corpora)
# => ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']

# Download a corpus
corpus = corpora[0]
datadownloader.download_corpus(corpus)

# Load the data
train_df, dev_df, test_df = datadownloader.load_corpus(corpus)
texts = train_df[1].tolist()
```

## Run a speed benchmark

Process the same texts with multiple tokenizers and compare their speed:

```python
from toiro import tokenizers

report = tokenizers.compare(texts)
print(report)
```

**Example output**:
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

## Next steps

- [Tokenizers](tokenizers.md) - Details about supported tokenizers
- [Benchmarks](benchmarks.md) - More detailed comparison methods
- [API Reference](api.md) - Complete API documentation
