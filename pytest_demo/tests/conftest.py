#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


# 这个pytest_runtest_setup钩子方法会在整个目录中的每个case中被执行
def pytest_runtest_setup(item):
    print("setting up", item)


def pytest_runtest_teardown(item):
    print("tearing down", item)


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


# 用来添加命令行选项
def pytest_addoption(parser):
    # for test_cmd_options.py
    parser.addoption("--cmdopt", action="store", default="type1", help="my option: type1 or type2")
    # for test_skip_by_opt.py
    parser.addoption("--runslow", action="store_true", default=False, help="run slow tests")


# 添加报告头
def pytest_report_header(config):
    opt = config.getoption('cmdopt')
    if opt != "type1" and opt != "type2":
        return ["error:cmdopt must be type1 or type2", "did you know that?"]


# for test_cmd_options.py
# pytest test_cmd_options.py --cmdopt=type1
# pytest test_cmd_options.py --cmdopt=type2
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


# for test_skip_by_opt.py
# pytest test_skip_by_opt.py    1 pass,1 fail
# pytest test_skip_by_opt.py --runslow 2 pass
def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
