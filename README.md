![Python 3.9 & 3.10](https://img.shields.io/badge/python-3.9%20%7C%203.10-%23007ec6)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Tests](https://github.com/Rom1-J/ralgo/workflows/tests/badge.svg)](https://github.com/Rom1-J/ralgo/actions?query=workflow%3Atests)
[![Style](https://github.com/Rom1-J/ralgo/workflows/style/badge.svg)](https://github.com/Rom1-J/ralgo/actions?query=workflow%3Astyle)

# Ralgo

An experimental encoding/decoding algorithm based on prime factor and matrix

- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Development](#development)
- [License](#license)
- [FAQ](#faq)

## Features

- Encode any type of data such as text, bytes, files, images,...
- Use two custom chars for the encoded output
- Choice to compress the encoded output
- Choice to show encoded output as an image

## Installation

Ralgo requires [Python](https://python.org/) 3.9+.

Install as a package

```sh
$ pip install git+https://github.com/Rom1-J/ralgo
```

Install from sources

```sh
$ git clone https://github.com/Rom1-J/ralgo
$ cd ralgo
$ pip install .
```

## Dependencies

- numpy==1.20.1
- Pillow==8.1.0
- sympy==1.7.1

## Development

Want to contribute? 

Simply download the repo and perform the following commands to configure your development environment with:

```sh
$ git clone https://github.com/Rom1-J/ralgo
$ cd ralgo
$ make
$ make install && make install-dev
```

Before suggesting a change, don't forget to lint, test and check the covereage with :

```sh
$ make lint
$ make test
$ make coverage
```

## License

[AGPL-3.0 License](https://github.com/Rom1-J/ralgo/blob/master/LICENSE)

## FAQ

**Question:** How does it work ?

**Answer:**

[Refer to this pdf](https://github.com/Rom1-J/ralgo/blob/master/docs/explain.pdf)

##