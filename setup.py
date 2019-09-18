from setuptools import setup

import package_index


def readme():
    with open('README.md', 'r', encoding='utf8') as f:
        return f.read()


setup(
    name='package-index',
    version=package_index.__version__,
    py_modules=['package_index'],
    author='mdrachuk',
    author_email='misha@drach.uk',
    description="Dataclasses API for PyPI and other warehouses.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/mdrachuk/package-index",
    license="MIT",
    keywords="python packaging pypi warehouse",
    python_requires=">=3.7",
    zip_safe=False,
    project_urls={
        'Pipelines': 'https://dev.azure.com/misha-drachuk/package-index',
        'Source': 'https://github.com/mdrachuk/package-index/',
        'Issues': 'https://github.com/mdrachuk/package-index/issues',
    },
    install_requires=[
        'requests>=2.22.0',
        'serious==1.0.0.dev20',
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
)
