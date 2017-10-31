#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


def test_func_fast():
    pass


@pytest.mark.slow
def test_func_slow():
    pass
