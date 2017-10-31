#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


# 这个pytest_runtest_setup钩子方法会在整个目录中的每个case中被执行
def pytest_runtest_setup(item):
    print("setting up", item)


# 这里可以定义一些全局的fixture
# 注意各个级别的fixture都是可以被override的
# 假如某个测试模块里又定义了一个同名的fixture,那么在该模块中,config_str就是被重写过的fixture
@pytest.fixture(scope="session")
def config_str():
    return "hey hey hey"


# 在fixture中创建文件
# 比如在程序中要创建一个大的图片,那么可以用tmpdir_factory创建一个临时目录
# tmpdir_factory.mktemp()创建临时目录
# tmpdir_factory.getbasetemp()获取base临时目录
@pytest.fixture(scope='session')
def image_file(tmpdir_factory):
    # img = compute_expensive_image()
    fn = tmpdir_factory.mktemp('data').join('img.png')
    # img.save(str(fn))
    return fn


# This autouse fixture will be executed for each test function and it will delete the method
# request.session.Session.request so that any attempts within tests to create http requests will fail.
# @pytest.fixture(autouse=True)
# def no_requests(monkeypatch):
#     monkeypatch.delattr("requests.sessions.Session.request")

