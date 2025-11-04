# 開発・貢献ガイド

- 行動規範: `CODE_OF_CONDUCT.md`
- コントリビュート方法: `CONTRIBUTING.md`
- テストは `test/` ディレクトリに配置されています。

## 開発環境のセットアップ（例）
```bash
python -m venv .venv
source .venv/bin/activate  # Windows は .venv\Scripts\activate
pip install -U pip
pip install -e .
pip install -r requirements-dev.txt  # ※存在する場合
pytest -q  # または python -m pytest
```
