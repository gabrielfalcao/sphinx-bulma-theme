#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


local_file = lambda *f: open(os.path.join(os.path.dirname(__file__), *f)).read()


def read_version():
    ctx = {}
    exec(local_file('sphinx_bulma_theme/version.py'), ctx)
    return ctx['version']


def read_readme():
    """Read README content.
    If the README.rst file does not exist yet
    (this is the case when not releasing)
    only the short description is returned.
    """
    try:
        return local_file('README.rst')
    except IOError:
        return __doc__


setup(
    name='sphinx_bulma_theme',
    author='Gabriel Falcao',
    author_email='gabriel@nacaolivre.org',
    description=read_version(),
    include_package_data=True,
    install_requires=[
        "pathlib2>=2.3.2",
        "Sphinx>=1.7.3"
        "sphinx-autobuild>=0.7.1",
    ],
    long_description=read_readme(),
    packages=find_packages(exclude=['*tests*']),
    test_suite='nose.collector',
    version=read_version(),
    entry_points={
        'sphinx.html_themes': [
            'bulma = sphinx_bulma_theme',
        ],
    },
    package_data={
        'sphinx_bulma_theme': ' '.join([
            '*.cfg',
            '*.conf',
            '*.css',
            '*.eot',
            '*.js',
            '*.otf',
            '*.py',
            '*.rst',
            '*.svg',
            '*.ttf',
            '*.txt',
            '*.woff',
        ]),
        '': ' '.join([
            '*.cfg',
            '*.conf',
            '*.css',
            '*.eot',
            '*.js',
            '*.otf',
            '*.py',
            '*.rst',
            '*.svg',
            '*.ttf',
            '*.txt',
            '*.woff',
        ]),
    },
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    zip_safe=False,
)
