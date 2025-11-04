# Benchmarks

toiro offers utilities to compare tokenizers from the following perspectives:

1. **Speed** (tokenize a fixed amount of text and measure throughput)
2. **Segmentation output** (diff token sequences from different tokenizers)
3. **Application performance** (e.g., accuracy of text classifiers such as SVM/BERT)

## Example (speed)
```python
from toiro import tokenizers
tokens_report = tokenizers.compare(texts)  # texts is a list of strings
```

## Example (segmentation comparison)
```python
from toiro import tokenizers
tokens_by_model = tokenizers.tokenize_all("今日は良い天気です。")
for name, tokens in tokens_by_model.items():
    print(name, tokens[:10])
```

> Actual API names may vary by version. Check docstrings in `toiro/tokenizers`.
