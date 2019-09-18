# package-index
[![PyPI](https://img.shields.io/pypi/v/package-index)][pypi]
[![Downloads](https://img.shields.io/pypi/dm/package-index)][pypi]
[![Build Status](https://img.shields.io/azure-devops/build/misha-drachuk/package-index/12)](https://dev.azure.com/misha-drachuk/package-index/_build/latest?definitionId=12&branchName=master)
[![Test Coverage](https://img.shields.io/coveralls/github/mdrachuk/package-index/master)](https://coveralls.io/github/mdrachuk/package-index)
[![Supported Python](https://img.shields.io/pypi/pyversions/package-index)][pypi]

Dataclasses API for PyPI and other warehouses. 

## Installation
Available from [PyPI][pypi]:
```shell
pip install package-index
```

## Usage

```python
>>> from package_index import fetch_package

>>> package = fetch_package('package-index')

>>> print(package.info)
PackageInfo(name='package-index', author='mdrachuk', author_email='misha@drach.uk', bugtrack_url=None, classifiers=['De...

>>> print(package.versions)
{'1.0.0b0', '1.0.0b1'}
```

[pypi]: https://pypi.org/project/package-index/