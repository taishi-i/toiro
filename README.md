<p align="center"><img width="50%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.png" /></p>

toiro
-----

[![Build Status](https://travis-ci.org/taishi-i/toiro.svg?branch=master)](https://travis-ci.org/taishi-i/toiro)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/taishii/toiro)](https://hub.docker.com/r/taishii/toiro)
![Python Package](https://github.com/taishi-i/toiro/workflows/Upload%20Python%20Package/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/toiro)](https://pypi.python.org/pypi/toiro)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/toiro)


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
---------------------------

If you want to add a tokenizer to toiro, please install it individually.
This is an example of adding [SudachiPy](https://github.com/WorksApplications/SudachiPy) and [nagisa](https://github.com/taishi-i/nagisa) to toiro.

```bash
pip install sudachipy sudachidict_core
pip install nagisa
```

<details>
<summary> How to install other tokenizers </summary>
<p>

[mecab-python3](https://github.com/SamuraiT/mecab-python3)
```
pip install mecab-python3==0.996.5
```

[GiNZA](https://github.com/megagonlabs/ginza)
```
pip install spacy ginza
```

[spaCy](https://github.com/explosion/spaCy)
```
pip install spacy[ja]
```

[KyTea](https://github.com/neubig/kytea)

You need to install KyTea. Please refer to [here](http://www.phontron.com/kytea/index-ja.html).

```
pip install kytea
```

[Juman++ v2](https://github.com/ku-nlp/jumanpp)

You need to install Juman++ v2. Please refer to [here](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++).

```
pip install pyknp
```

[SentencePiece](https://github.com/google/sentencepiece)
```
pip install sentencepiece
```

[fugashi-ipadic](https://github.com/polm/fugashi)
```
pip install fugashi ipadic
```

[fugashi-unidic](https://github.com/polm/fugashi)
```
pip install fugashi unidic-lite
```

[tinysegmenter](https://github.com/SamuraiT/tinysegmenter)
```
pip install tinysegmenter3
```


</p>
</details>

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

Toiro supports 12 different Japanese tokonizers. This is an example of adding SudachiPy and nagisa.
```python
{'nagisa': {'is_available': True, 'version': '0.2.7'},
 'janome': {'is_available': True, 'version': '0.3.10'},
 'mecab-python3': {'is_available': False, 'version': False},
 'sudachipy': {'is_available': True, 'version': '0.4.9'},
 'spacy': {'is_available': False, 'version': False},
 'ginza': {'is_available': False, 'version': False},
 'kytea': {'is_available': False, 'version': False},
 'jumanpp': {'is_available': False, 'version': False},
 'sentencepiece': {'is_available': False, 'version': False},
 'fugashi-ipadic': {'is_available': False, 'version': False},
 'fugashi-unidic': {'is_available': False, 'version': False},
 'tinysegmenter': {'is_available': False, 'version': False}}
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

# Compare the words segmented in tokenizers
text = "都庁所在地は新宿区。"
tokenizers.print_words(text, delimiter="|")
#=>        janome: 都庁|所在地|は|新宿|区|。
#=>        nagisa: 都庁|所在|地|は|新宿|区|。
#=>     sudachipy: 都庁|所在地|は|新宿区|。
```

Run toiro in Docker
-------------------

You can use all tokenizers by building a docker container from Docker Hub.

```bash
docker run --rm -it taishii/toiro /bin/bash
```

<details>
<summary> How to run the Python interpreter in the Docker container </summary>
<p>

Run the Python interpreter.
```
root@cdd2ad2d7092:/workspace# python3
```

Compare the words segmented in tokenizers
```python
>>> from toiro import tokenizers
>>> text = "都庁所在地は新宿区。"
>>> tokenizers.print_words(text, delimiter="|")
 mecab-python3: 都庁|所在地|は|新宿|区|。
        janome: 都庁|所在地|は|新宿|区|。
        nagisa: 都庁|所在|地|は|新宿|区|。
     sudachipy: 都庁|所在地|は|新宿区|。
         spacy: 都庁|所在|地|は|新宿|区|。
         ginza: 都庁|所在地|は|新宿区|。
         kytea: 都庁|所在|地|は|新宿|区|。
       jumanpp: 都庁|所在|地|は|新宿|区|。
 sentencepiece: ▁|都|庁|所在地|は|新宿|区|。
fugashi-ipadic: 都庁|所在地|は|新宿|区|。
fugashi-unidic: 都庁|所在|地|は|新宿|区|。
 tinysegmenter: 都庁所|在地|は|新宿|区|。
```

</p>
</details>

Get more information about toiro
--------------------------------

The slides at PyCon JP 2020
- [Speaker Deck](https://speakerdeck.com/taishii/pycon-jp-2020)
- [PyConJP2020_Online.ipynb](https://github.com/taishi-i/toiro/blob/master/PyConJP2020/PyConJP2020_Online.ipynb)

Tutorials in Japanese
- [01_getting_started_ja.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/01_getting_started_ja.ipynb)
- [05_svm_vs_bert_benchmarking_application_tasks_ja.ipynb](https://github.com/taishi-i/toiro/blob/master/examples/05_svm_vs_bert_benchmarking_application_tasks_ja.ipynb)


Contributing
------------

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
