from uuid import uuid4

import pytest

from package_index import fetch_package, PackageIndexError


def test_fetch_self():
    package = fetch_package('package-index')
    assert package.contains_version('1.0.0b1')


def test_non_existing():
    with pytest.raises(PackageIndexError):
        fetch_package(f'serious-{uuid4()}')
