#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


# content of test_ids.py
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass


def test_ab(a, b):
    pass


# 上面的case也可以改成以下的形式
@pytest.mark.usefixtures("a", "b")
class BigClass(object):
    def test_aa(self):
        print(a)
        pass


'''
参数化fixture的功能是，可以方便地写多个正交的fixture相关的测试
的测试
'''


'''
也可以把所有测试用例都用到的fixtures写在一个ini文件里
# content of pytest.ini
[pytest]
usefixtures = cleandir
'''