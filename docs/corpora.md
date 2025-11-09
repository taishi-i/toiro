# コーパスとデータ

`toiro.datadownloader` モジュールは、日本語のテキスト分類タスク用のコーパスを簡単にダウンロードして利用できる機能を提供します。

## 利用可能なコーパス

### livedoor ニュースコーパス
- **タスク**: テキスト分類（ニュースカテゴリ分類）
- **カテゴリ数**: 9カテゴリ
- **カテゴリ**: トピックニュース、Sports Watch、ITライフハック、家電チャンネル、MOVIE ENTER、独女通信、エスマックス、livedoor HOMME、Peachy
- **提供元**: [livedoor ニュースコーパス](https://www.rondhuit.com/download.html)

### Yahoo! 映画レビュー
- **タスク**: 感情分析（ポジティブ/ネガティブ）
- **ドメイン**: 映画レビュー
- **データ形式**: レビューテキストと評価スコア

### Amazon レビュー
- **タスク**: 感情分析（ポジティブ/ネガティブ）
- **ドメイン**: 商品レビュー
- **データ形式**: レビューテキストと評価スコア

## 基本的な使い方

### コーパスの一覧を取得
```python
from toiro import datadownloader

corpora = datadownloader.available_corpus()
print(corpora)
# => ['livedoor_news_corpus', 'yahoo_movie_reviews', 'amazon_reviews']
```

### コーパスのダウンロード
```python
datadownloader.download_corpus("livedoor_news_corpus")
```

コーパスは `~/.toiro/` ディレクトリにダウンロードされます。

### コーパスの読み込み
```python
train_df, dev_df, test_df = datadownloader.load_corpus("livedoor_news_corpus")

# データの確認
print(f"Train: {len(train_df)} samples")
print(f"Dev: {len(dev_df)} samples")
print(f"Test: {len(test_df)} samples")

# データ構造（pandas DataFrame）
# カラム 0: ラベル
# カラム 1: テキスト
texts = train_df[1].tolist()
labels = train_df[0].tolist()
```

## データの前処理

ダウンロードしたコーパスは、train/dev/test に分割済みの pandas DataFrame として提供されます。

```python
# 例: トークナイザの評価用にテキストのみ抽出
texts = train_df[1].tolist()

# 例: 分類器の学習用にラベルとテキストを抽出
X_train = train_df[1].tolist()
y_train = train_df[0].tolist()
```

!!! info "データの保存場所"
    ダウンロードしたコーパスは `~/.toiro/` ディレクトリに保存されます。一度ダウンロードすれば、以降は `load_corpus()` で直接読み込めます。
