#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import os
'''
Run tests in a module
$pytest test_mod.py

Run tests in a directory
$pytest testing/

Run tests by keyword expressions
$pytest -k "TestClass or method"

To run a specific test within a module:
$pytest test_mod.py::test_func

Another example specifying a test method in the command line:
$pytest test_mod.py::TestClass::test_method

$pytest --showlocals # show local variables in tracebacks
$pytest -l # show local variables (shortcut)

用pdb和设置断点
$pytest -x --pdb # drop to PDB on first failure, then end test session
To set a breakpoint in your code use the native Python import pdb;pdb.set_trace() call in your code and
pytest automatically disables its output capture for that test:

查看测试最慢的十个次测试:
pytest --durations=10

生成Jenkins认识的JunitXML格式
pytest --junitxml=path

配置文件中设置JUnitXML文件的根(pytest3.1开始支持,可以代替上面的调用)
[pytest]
junit_suite_name = my_suite

运行$pytest --collect-only test_ids.py可以看到test_ab这个测试方法执行的次数=a个数*b个数

'''


# 抛出异常的case
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


# 使用类集中管理cases
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

        # def test_two(self):
        #     x = "hello"
        #     assert hasattr(x, 'check')


# assertion introspection
def test_needsfiles(tmpdir):
    print(tmpdir)  # tmpdir是跑测试用例的临时目录,类似的变量可以通过pytest --fixtures来查看
    a = 10
    b = a / 3
    assert b != 0

'''
# 使用自定义的fixture
# @pytest.fixture(scope='module') # 可以吧smtp定义为模块级别的fixture,这样的话,在同一个模块只会被调用一次
# @pytest.fixture(scope='session') # 可以吧smtp定义为session级别的fixture,无论如何，它只会被调用一次
@pytest.fixture  # 默认每次个方法第一次读到smtp的时候,都会调用一次这个函数
def smtp():
    import smtplib
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_obj  # provide the fixture value
    print("teardown smtp")      # yield以后的代码将在这个fixture不在被使用的时候调用
    smtp_obj.close()
    # 也可以写成以下的形式
    # with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
    #     yield smtp  # provide the fixture value


def test_ehlo(smtp):  # 之列用到的smtp就是用@pytest.fixture修饰的fixture
    response, msg = smtp.ehlo()
    assert response == 250
    # assert 0  # for demo purposes


def test_noop(smtp):
    response, msg = smtp.noop()
    assert response == 250
    # assert 0  # for demo purposes
'''

'''
# 分别用两个参数来跑下面的case:test_param_fixtures
@pytest.fixture(scope="module",
                params=["smtp.gmail.com", "mail.python.org"])
def smtp2(request):
    import smtplib
    smtp2 = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp2
    print("finalizing %s" % smtp2)
    smtp2.close()


def test_param_fixtures(smtp2):
    response, msg = smtp2.noop()
    assert response == 250
    assert 0  # for demo purposes
'''


# 演示monkey patching
def get_ssh():  # pseudo application code
    return os.path.join(os.path.expanduser("~admin"), '.ssh')


def test_monkey(monkeypatch):
    def mockreturn(path):
        return os.sep + 'abc'
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = get_ssh()
    x2 = os.sep.join(['', 'abc', '.ssh'])
    assert x2 == x
    assert x == '/abc/.ssh' or x == '\\abc\\.ssh'


# 演示tmpdir的使用
# tmpdir is a py.path.local object which offers os.path methods and more.
def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1

