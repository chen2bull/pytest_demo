#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# content of test_sample.py
# @pytest.mark.xfail
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
        import pytest
        pytest.skip("")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed
