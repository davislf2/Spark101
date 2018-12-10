#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit pyspark_mllib/__version__.py
version = {}
with open(os.path.join(here, 'pyspark_mllib', '__version__.py')) as f:
    exec(f.read(), version)

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='pyspark_mllib',
    version=version['__version__'],
    description="practice of PySpark and MLlib",
    long_description=readme + '\n\n',
    author="Davis Hong",
    author_email='davislf2.net@gmail.com',
    url='https://github.com//pyspark_mllib',
    packages=[
        'pyspark_mllib',
    ],
    package_dir={'pyspark_mllib':
                 'pyspark_mllib'},
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='pyspark_mllib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    install_requires=[],  # FIXME: add your package's dependencies to this list
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    }
)
