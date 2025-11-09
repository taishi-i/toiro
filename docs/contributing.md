# 開発・貢献ガイド

toiro プロジェクトへの貢献を歓迎します！バグ報告、機能要望、プルリクエストなど、あらゆる形での貢献をお待ちしています。

## 行動規範とガイドライン

- **行動規範**: [CODE_OF_CONDUCT.md](https://github.com/taishi-i/toiro/blob/master/CODE_OF_CONDUCT.md)
- **コントリビュートガイド**: [CONTRIBUTING.md](https://github.com/taishi-i/toiro/blob/master/CONTRIBUTING.md)

## 開発環境のセットアップ

### 1. リポジトリのクローン
```bash
git clone https://github.com/taishi-i/toiro.git
cd toiro
```

### 2. 仮想環境の作成とアクティベート
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. 開発用パッケージのインストール
```bash
pip install -U pip
pip install -e .
pip install -e ".[all_tokenizers]"  # 全トークナイザをインストール（オプション）
```

### 4. テストの実行
```bash
pytest -q  # または: python -m pytest
```

テストファイルは `test/` ディレクトリに配置されています：
- `test_tokenizers.py` - トークナイザのテスト
- `test_datadownloader.py` - データダウンローダのテスト
- `test_classifiers.py` - 分類器のテスト

## 貢献の方法

### バグ報告
[GitHub Issues](https://github.com/taishi-i/toiro/issues) でバグを報告してください。以下の情報を含めると助かります：
- Python バージョン
- toiro バージョン
- 再現手順
- エラーメッセージ

### 機能要望
新機能のアイデアがある場合は、[GitHub Issues](https://github.com/taishi-i/toiro/issues) で提案してください。

### プルリクエスト
1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/your-feature`)
3. 変更をコミット (`git commit -am 'Add some feature'`)
4. ブランチにプッシュ (`git push origin feature/your-feature`)
5. プルリクエストを作成

## トークナイザの追加

新しいトークナイザを追加する場合：

1. `toiro/tokenizers/` に新しいファイルを作成（例: `tokenizer_newone.py`）
2. `tokenize()` 関数を実装
3. `tokenizer_utils.py` に可用性チェック関数を追加
4. `__init__.py` を更新して新しいトークナイザをインポート
5. テストを `test/test_tokenizers.py` に追加

## ドキュメントの更新

ドキュメントは `docs/` ディレクトリにあります。MkDocs を使用してローカルでプレビューできます：

```bash
pip install mkdocs-material mkdocs-static-i18n mkdocstrings[python]
mkdocs serve
```

ブラウザで `http://127.0.0.1:8000` を開いてプレビューを確認できます。

## 質問やサポート

質問がある場合は、[GitHub Discussions](https://github.com/taishi-i/toiro/discussions) または [Issues](https://github.com/taishi-i/toiro/issues) でお気軽にお尋ねください。
