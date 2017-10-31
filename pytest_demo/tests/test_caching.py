#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import time

"""
pytest提供一下两个选项
• --lf, --last-failed   只跑failures的用例
• --ff, --failed-first  先跑failures的用例,再跑其他用例

"""


@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")


# 可以使用config.cache加快下次测试的时间
# Plugins or conftest.py support code can get a cached value using the pytest config object.
@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        time.sleep(9 * 0.6)  # expensive computation :)
        val = 42
    request.config.cache.set("example/value", val)
    return val


def test_function(mydata):
    # assert mydata == 23
    assert mydata == 42
"""
--cache-show        显示cache的时间
--cache-clear       清除cache
"""