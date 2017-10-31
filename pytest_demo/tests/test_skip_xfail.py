#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import sys


# 用skip标志case会被skip
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass


def valid_config():
    return False


# 在测试代码中skip
def test_skip_in_case():
    if not valid_config():
        pytest.skip("unsupported configuration")


# 条件skip
@pytest.mark.skipif(sys.version_info > (3, 3), reason="requires python3.3")
def test_conditional():
    pass


@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
class TestPosixCalls(object):
    def test_function(self):
        """will not be setup or run under 'win32' platform"""
        pass


# 用xfail标志case总会fail,xfailed状态的意思是(expected fail)
# 如果case正常执行,状态将为XPASS(unexpectedly passing)
@pytest.mark.xfail
def test_xfail():
    pass
    assert 0


# run设置为false,不会执行这个用例
@pytest.mark.xfail(run=False)
def test_not_run():
    pass


# 如果strict被设置为True,那么这个测试用例必须fail,否则会报错
@pytest.mark.xfail(strict=True)
def test_case_must_fail():
    assert 0


# 必须是抛出RuntimeError,否则为fail,如果pass了,状态将为XPASS
@pytest.mark.xfail(raises=RuntimeError)
def test_throw_exception():
    raise RuntimeError


def test_xfail_in_case():
    if not valid_config():
        pytest.xfail("failing configuration (but should work)")


# 当使用parametrize的时候,可以指定特定参数下的测试实例为fail
@pytest.mark.parametrize(("n", "expected"), [
    (1, 2),
    pytest.param(1, 0, marks=pytest.mark.xfail),
    pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
    (2, 3),
    (3, 4),
    (4, 5),
    pytest.param(10, 12, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")),
    # (10, 12),
])
def test_increment(n, expected):
    assert n + 1 == expected

'''
当用pytest --runxfail的时候, 所有的xfail标记会被忽略
'''

