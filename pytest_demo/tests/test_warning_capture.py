#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings


# The recwarn fixture will record warnings for the whole function
def test_hello(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    w = recwarn.pop(UserWarning)
    assert issubclass(w.category, UserWarning)
    assert str(w.message) == "hello"
    assert w.filename
    assert w.lineno
