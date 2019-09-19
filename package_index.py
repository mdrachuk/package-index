"""
Dataclasses API for PyPI and other warehouses.

PyPI: https://pypi.org/
Warehouse: https://github.com/pypa/warehouse
"""
from __future__ import annotations

__version__ = '1.0.0rc0'
__author__ = 'Misha Drachuk'
__license__ = 'MIT'

from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Set, List, Optional

import requests
from pkg_resources import safe_version
from serious import JsonModel


def fetch_package(name: str, warehouse='https://pypi.org/pypi') -> Package:
    """Fetch a package from pypi.org by name.

    Provide a URL for other warehouse to use it instead of PyPI.
    """
    response = requests.get(f'{warehouse}/{name}/json')
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise PackageIndexError(name) from e
    package_json = response.text
    model = JsonModel(Package, camel_case=False)
    return model.load(package_json)


Version = str  # an alias for correct typings


@dataclass
class Package:
    info: PackageInfo
    releases: Dict[Version, List[Release]]
    last_serial: int
    urls: List[Release]

    @property
    def versions(self) -> Set[str]:
        return set(self.releases.keys())

    def contains_version(self, target: str) -> bool:
        target = safe_version(target)
        existing = {safe_version(version) for version in self.versions}
        return target in existing


@dataclass(frozen=True)
class PackageInfo:
    name: str
    author: str
    author_email: str
    bugtrack_url: Optional[str]
    classifiers: List[str]
    description: str
    description_content_type: str
    docs_url: Optional[str]
    download_url: str
    downloads: Dict[str, int]
    home_page: str
    keywords: str
    license: str
    maintainer: str
    maintainer_email: str
    package_url: str
    platform: str
    project_url: str
    project_urls: Dict[str, str]
    release_url: str
    requires_dist: Optional[List[str]]
    requires_python: str
    summary: str
    version: str


@dataclass(frozen=True)
class Release:
    comment_text: str
    digests: Dict[str, str]
    downloads: int
    filename: str
    has_sig: bool
    md5_digest: str
    packagetype: str
    python_version: str
    requires_python: str
    size: int
    upload_time: datetime
    url: str


class PackageIndexError(Exception):
    def __init__(self, name: str):
        super().__init__(f'Package "{name}" could not be fetched from PyPI. ')
