#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

"""
查看参数化fixture,就在本工程全局搜索smtp2

"""


# 一份代码,多个执行实例
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
    pytest.param("6*9", 42, marks=pytest.mark.xfail),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# 多个参数
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass

# 参数化的另一使用,见Basic pytest_generate_tests example
