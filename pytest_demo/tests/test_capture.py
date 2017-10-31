#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

'''
默认输出到stderr和stdout的都会被capture到,当用例fail的时候就会显示
而stdin被设置为null,因为自动测试中要求输入是不合理的

pytest -s # disable all capturing
pytest --capture=sys # replace sys.stdout/stderr with in-mem files
pytest --capture=fd # also point filedescriptors 1 and 2 to temp file
'''


# The capsys and capfd fixtures allow to access stdout/stderr output created during test execution.
def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print("next")
    out, err = capsys.readouterr()
    assert out == "next\n"
