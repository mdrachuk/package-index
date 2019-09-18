from uuid import uuid4

import pytest

from package_index import fetch_package, PackageIndexError


def test_fetch_self():
    # TODO:mdrachuk:9/18/19: change to package-index
    package = fetch_package('serious')
    assert package.contains_version('1.0.0.dev20')


def test_non_existing():
    with pytest.raises(PackageIndexError):
        fetch_package(f'serious-{uuid4()}')
