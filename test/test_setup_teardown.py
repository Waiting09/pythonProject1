# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 17:11
# @Author  : L


# setup_module/ teardown_module：全局模块级
# setup_class/teardown _class：类级,只在类中前后运行一次
# setup_function/ teardown_function：函数级,在类外
# setup_method/ teardown_method：方法级,类中的每个方法执行前后
# setup/teardown：在类中,运行在调用方法的前后(重点)


# 模块级别
import pytest


def setup_module():
    print("资源准备：setup_module")


def teardown_module():
    print("资源销毁：teardown_module")


def test_case1():
    print("case1")


def setup_function():
    print("资源准备：setup_function")


def teardown_function():
    print("资源销毁：teardown_function")


class TestDemo:

    # 执行类 前后分别执行setup_class teardown_class
    def setup_class(self):
        print("TestDemo:setup_class")

    def teardown_class(self):
        print("TestDemo:teardown_class")

    # 每个类里面的方法前后分别执行 setup,teardown
    def setup(self):
        print("TestDemo:setup")

    def teardown(self):
        print("TestDemo:teardown")

    """
    def setup_method(self):
        print("TestDemo:setup_method")

    def teardown_method(self):
        print("TestDemo:teardown_methond")
    """

    @pytest.mark.str #标记这个用例
    def test_demo1(self):
        print("test_demo1")


    def test_demo2(self):
        print("test_demo2")

