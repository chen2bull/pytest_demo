# content of test_step.py
import pytest


@pytest.mark.incremental
class TestUserHandling(object):
    def test_login(self):
        pass

    def test_modification(self):
        assert 0

    def test_deletion(self):
        pass


def test_normal():
    pass
