# ベンチマーク

toiro は以下の観点で比較するユーティリティを提供します。

1. **処理速度**（一定量のテキストを分かち書きして計測）
2. **分割結果の比較**（同一文に対する各トークナイザのトークン列差分）
3. **アプリ性能**（例: テキスト分類器での精度比較。SVM/BERT など）

## サンプル（速度比較）
```python
from toiro import tokenizers
tokens_report = tokenizers.compare(texts)  # texts は文字列のリスト
```

## サンプル（分割結果の比較）
```python
from toiro import tokenizers
tokens_by_model = tokenizers.tokenize_all("今日は良い天気です。")
for name, tokens in tokens_by_model.items():
    print(name, tokens[:10])
```

> 実際の API 名はバージョンによって変わる可能性があります。`toiro/tokenizers` の docstring を参照してください。
