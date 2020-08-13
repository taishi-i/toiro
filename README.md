<p align="center"><img width="50%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.png" /></p>

toiro
-----

[![Build Status](https://travis-ci.org/taishi-i/toiro.svg?branch=master)](https://travis-ci.org/taishi-i/toiro)
[![PyPI](https://img.shields.io/pypi/v/toiro)](https://pypi.python.org/pypi/toiro)


Toiro is a comparison tool of Japanese tokenizers.
- Compare the processing speed of tokenizers
- Compare the words segmented in tokenizers
- Compare the performance of tokenizers by benchmarking application tasks (e.g., text classification)

It also provides useful functions for natural language processing in Japanese.
- Data downloader for Japanese text corpora
- Preprocessor of these corpora
- Text classifier for Japanese text (e.g., SVM, BERT)

<p align="center"><img width="90%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.gif" /></p>


Installation
------------

Python 3.6+ is required. You can install toiro with the following command.
[Janome](https://github.com/mocobeta/janome) is included in the default installation.
```bash
pip install toiro
```

Adding a tokenizer to toiro
------------------------

If you want to add a tokenizer to toiro, please install it individually.
This is an example of adding [SudachiPy](https://github.com/WorksApplications/SudachiPy) and [nagisa](https://github.com/taishi-i/nagisa) to toiro.

```bash
pip install sudachipy sudachidict_core
pip install nagisa
```

If you want to install all the tokonizers at once, please use the following command.
```bash
pip install toiro[all_tokenizers]
```

Getting started
---------------

You can check the available tokonizers in your Python environment.
```python
from toiro import tokenizers

available_tokenizers = tokenizers.available_tokenizers()
print(available_tokenizers)
```

Toiro supports 9 different Japanese tokonizers. This is an example of adding SudachiPy and nagisa.
```python
{'nagisa': {'is_available': True, 'version': '0.2.7'},
 'janome': {'is_available': True, 'version': '0.3.10'},
 'mecab-python3': {'is_available': False, 'version': False},
 'sudachipy': {'is_available': True, 'version': '0.4.9'},
 'spacy': {'is_available': False, 'version': False},
 'ginza': {'is_available': False, 'version': False},
 'kytea': {'is_available': False, 'version': False},
 'jumanpp': {'is_available': False, 'version': False},
 'sentencepiece': {'is_available': False, 'version': False}}
```

Download the livedoor news corpus and compare the processing speed of tokenizers.
```python
from toiro import tokenizers
from toiro import datadownloader

# A list of avaliable corpora in toiro
corpora = datadownloader.available_corpus()
print(corpora)
#=> ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']

# Download the livedoor news corpus and load it as pandas.DataFrame
corpus = corpora[0]
datadownloader.download_corpus(corpus)
train_df, dev_df, test_df = datadownloader.load_corpus(corpus)
texts = train_df[1]

# Compare the processing speed of tokenizers
report = tokenizers.compare(texts)
#=> [1/3] Tokenizer: janome
#=> 100%|███████████████████| 5900/5900 [00:07<00:00, 746.21it/s]
#=> [2/3] Tokenizer: nagisa
#=> 100%|███████████████████| 5900/5900 [00:15<00:00, 370.83it/s]
#=> [3/3] Tokenizer: sudachipy
#=> 100%|███████████████████| 5900/5900 [00:08<00:00, 696.68it/s]
print(report)
{'execution_environment': {'python_version': '3.7.8.final.0 (64 bit)',
  'arch': 'X86_64',
  'brand_raw': 'Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz',
  'count': 8},
 'data': {'number_of_sentences': 5900, 'average_length': 37.69593220338983},
 'janome': {'elapsed_time': 9.114670515060425},
 'nagisa': {'elapsed_time': 15.873093605041504},
 'sudachipy': {'elapsed_time': 9.05256724357605}}

# Compare the words segmented in each tokenizer
text = "都庁所在地は新宿区。"
tokenizers.print_words(text, delimiter="|")
#=>        janome: 都庁|所在地|は|新宿|区|。
#=>        nagisa: 都庁|所在|地|は|新宿|区|。
#=>     sudachipy: 都庁|所在地|は|新宿区|。
```

Run toiro in Docker
-------------------

Build a docker container
```bash
git clone https://github.com/taishi-i/toiro
cd toiro
docker build -t taishi-i/toiro -f docker/cpu/Dockerfile .
```

Run the docker container
```bash
docker run --rm -i -t taishi-i/toiro /bin/bash
```

Get more information about toiro
--------------------------------

Tutorials
- [01_getting_started.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/01_getting_started.ipynb)
- [02_tutorial_tokenizers.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/02_tutorial_tokenizers.ipynb)
- [03_compare_tokenizers_with_downsteam_tasks.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/03_compare_tokenizers_with_downsteam_tasks.ipynb)
- [04_tutorial_datadownloader.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/04_tutorial_datadownloader.ipynb)
- [05_svm_vs_bert_benchmarking_application_tasks.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/05_svm_vs_bert_benchmarking_application_tasks.ipynb)
