# Contributing Guide

We welcome contributions to the toiro project! Whether it's bug reports, feature requests, or pull requests, all forms of contribution are appreciated.

## Code of Conduct and Guidelines

- **Code of Conduct**: [CODE_OF_CONDUCT.md](https://github.com/taishi-i/toiro/blob/master/CODE_OF_CONDUCT.md)
- **Contributing Guide**: [CONTRIBUTING.md](https://github.com/taishi-i/toiro/blob/master/CONTRIBUTING.md)

## Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/taishi-i/toiro.git
cd toiro
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install development packages
```bash
pip install -U pip
pip install -e .
pip install -e ".[all_tokenizers]"  # Install all tokenizers (optional)
```

### 4. Run tests
```bash
pytest -q  # or: python -m pytest
```

Test files are located in the `test/` directory:
- `test_tokenizers.py` - Tokenizer tests
- `test_datadownloader.py` - Data downloader tests
- `test_classifiers.py` - Classifier tests

## How to Contribute

### Bug Reports
Report bugs via [GitHub Issues](https://github.com/taishi-i/toiro/issues). Please include:
- Python version
- toiro version
- Steps to reproduce
- Error messages

### Feature Requests
If you have ideas for new features, propose them via [GitHub Issues](https://github.com/taishi-i/toiro/issues).

### Pull Requests
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a pull request

## Adding a Tokenizer

To add a new tokenizer:

1. Create a new file in `toiro/tokenizers/` (e.g., `tokenizer_newone.py`)
2. Implement the `tokenize()` function
3. Add an availability check function in `tokenizer_utils.py`
4. Update `__init__.py` to import the new tokenizer
5. Add tests in `test/test_tokenizers.py`

## Updating Documentation

Documentation is in the `docs/` directory. You can preview it locally using MkDocs:

```bash
pip install mkdocs-material mkdocs-static-i18n mkdocstrings[python]
mkdocs serve
```

Open `http://127.0.0.1:8000` in your browser to view the preview.

## Questions and Support

If you have questions, feel free to ask via [GitHub Discussions](https://github.com/taishi-i/toiro/discussions) or [Issues](https://github.com/taishi-i/toiro/issues).
