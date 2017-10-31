#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


class DB(object):
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        print("begin", name)
        self.intransaction.append(name)

    def rollback(self):
        print("rollback")
        self.intransaction.pop()


@pytest.fixture(scope="module")
def db():
    return DB()


class TestClass(object):
    # transact是class级别的fixture，且有autouse标记，所有这个类中的case都会用到它
    # if an autouse fixture is defined in a conftest.py file then all tests
    # in all test modules below its directory will invoke the fixture.
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        # yield以下的代码在teardown的时候执行
        db.rollback()

    def test_method1(self, db):
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        assert db.intransaction == ["test_method2"]
