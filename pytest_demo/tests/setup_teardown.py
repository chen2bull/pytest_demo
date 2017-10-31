#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# As of pytest-3.0, the module parameter is optional.
def setup_module(module):
    """
    setup any state specific to the execution of the given module.
    """


def teardown_module(module):
    """
    teardown any state that was previously setup with a setup_module
    method.
    """


class WhatEv:
    @classmethod
    def setup_class(cls):
        """
        setup any state specific to the execution of the given class (which
        usually contains tests).
        """

    @classmethod
    def teardown_class(cls):
        """
        teardown any state that was previously setup with a call to
        setup_class.
        """

    def setup_method(self, method):
        """
        setup any state tied to the execution of the given method in a
        class. setup_method is invoked for every test method of a class.
        """

    def teardown_method(self, method):
        """
        teardown any state that was previously setup with a setup_method
        call.
        """
