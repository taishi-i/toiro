# toiro Documentation

<p align="center"><img width="50%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.png?raw=true" /></p>

**toiro** is a Python package for **comparing Japanese tokenizers**. You can:

- **Compare processing speed** across tokenizers
- **Compare tokenization outputs** side by side
- Evaluate **downstream task performance** (e.g., text classification)
- Use helper utilities for Japanese NLP (**corpus download/preprocessing, simple classifiers**, etc.)

<p align="center"><img width="90%" src="https://github.com/taishi-i/toiro/blob/master/toiro/datadownloader/data/toiro.gif?raw=true" /></p>

## Key Features

### Supported Tokenizers
13 Japanese tokenizers and BPE models:

- janome (included by default)
- nagisa
- mecab-python3
- sudachipy
- spacy
- ginza
- kytea
- jumanpp
- sentencepiece
- fugashi (ipadic/unidic)
- tinysegmenter
- tiktoken (BPE for GPT-4o / GPT-5)

### Links

👉 **Project**: <https://github.com/taishi-i/toiro>
👉 **Demo (Hugging Face Spaces)**: <https://huggingface.co/spaces/taishi-i/Japanese-Tokenizer-Comparison>
👉 **PyPI**: <https://pypi.org/project/toiro/>

!!! tip "Supported Python Versions"
    Python 3.10 or later is recommended.

!!! info "License"
    toiro is released under the Apache License 2.0.

---

This documentation site is generated with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
