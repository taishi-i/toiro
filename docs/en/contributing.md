# Contributing Guide

- Code of Conduct: `CODE_OF_CONDUCT.md`
- How to contribute: `CONTRIBUTING.md`
- Tests live under the `test/` directory.

## Dev environment (example)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .
pip install -r requirements-dev.txt  # if present
pytest -q  # or: python -m pytest
```
