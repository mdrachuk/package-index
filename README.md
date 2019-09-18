# package-index
[![PyPI](https://img.shields.io/pypi/v/package-index)][pypi]
[![Downloads](https://img.shields.io/pypi/dm/package-index)][pypi]
[![Build Status](https://img.shields.io/azure-devops/build/misha-drachuk/package-index/12)](https://dev.azure.com/misha-drachuk/package-index/_build/latest?definitionId=12&branchName=master)
[![Test Coverage](https://img.shields.io/coveralls/github/mdrachuk/package-index/master)](https://coveralls.io/github/mdrachuk/package-index)
[![Supported Python](https://img.shields.io/pypi/pyversions/package-index)][pypi]

Check version of a Python module.

Queries PyPI and looks for the `<module>.__version__` among all available versions.
Raises an error if the version already exists.

Comes in handy in CI to remember changing library version.

For more on Python module versioning check out [PEP-440](https://www.python.org/dev/peps/pep-0440). 

## Installation
Available from [PyPI][pypi]:
```shell
pip install package-index
```

## Module Example
With a \<module\> present on PyPI and `<module>.py` in current directory:
```python
__version__ = '7.7.7'

...
```

Simply run:
```shell
package-index <module>
```

If `7.7.7` version of \<module\> is on PyPI already you’ll get a `VersionExists` error:
```plain
Traceback (most recent call last):
  File "./package-index", line 86, in <module>
    main(sys.argv[1:])
  File "./package-index", line 82, in main
    check_unique(name, version)
  File "./package-index", line 28, in check_unique
    raise VersionExists(name, version)
__main__.VersionExists: Package "<module>" with version "7.7.7" already exists on PyPI.
Change the "<module>.__version__" to fix this error.
```

## Package Example
Packages work in the same way as modules except `__version__` is defined in `<module>/__init__.py`

[pypi]: https://pypi.org/project/package-index/