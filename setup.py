#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import os
# import codecs
import sys

import eparse

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)
long_description = read('README.md')


# for nose
# class NoseTest(TestCommand):
#     def finalize_options(self):
#         TestCommand.finalize_options(self)
#         self.test_args = []
#         self.test_suite = True
#
#     def run_tests(self):
#         import nose
#         nose.run_exit(argv=['nosetests'])

# for pytest
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["-l"]  # 跑pytest的选项在这里
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='eparse',
    version=eparse.__version__,
    url='http://github.com/cmingjian/eparse/',
    license='Apache Software License',
    author='MJ Chen',
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies
    install_requires=['openpyxl==2.4.9'],
    author_email='cmingjian@qq.com',
    description='eparse',
    long_description=long_description,
    # packages=['eparse'],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md', '*.xlsx'],
    },
    platforms='any',
    # for nose
    # tests_require=[
    #     'nose',
    #     'coverage',
    #     'mock'
    # ],
    # cmdClass={'test': NoseTest},
    # for pytest
    tests_require=[
        'pytest',
        'coverage',
        'mock',
    ],
    cmdclass={'test': PyTest},
    extras_require={
        'testing': ['pytest'],
    },
    test_suite='pytest_demo.tests.test_eparse',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Quality Assurance',
    ],
)


