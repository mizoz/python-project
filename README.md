# Python Project Template

A Python project template with requirements.txt and setup.py for easy package development and distribution.

## Features

- Ready-to-use project structure
- requirements.txt for dependencies
- setup.py for package installation
- Configured for pip install
- Best practices included

## Project Structure

```
python-project/
├── setup.py          # Package configuration
├── requirements.txt  # Dependencies
├── package_name/     # Main package
│   ├── __init__.py
│   └── module.py
└── README.md
```

## Installation

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install package in development mode

```bash
pip install -e .
```

### Install as package

```bash
python setup.py install
```

## Usage

```python
from package_name import module

result = module.some_function()
print(result)
```

## Development

### Install dev dependencies

```bash
pip install -r requirements-dev.txt
```

### Run tests

```bash
pytest
```

### Build package

```bash
python setup.py sdist bdist_wheel
```

## License

MIT License

## Author

mizoz
