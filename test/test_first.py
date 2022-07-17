# -*- coding: utf-8 -*-

# 文件：test_开头或者_test结尾
# 类：Test开头
# 方法/函数：test_开头
# 注意：测试类中不可以添加__init__构造函数
import sys

import pytest


@pytest.mark.skip(reason="跳过原因")
def test_skip():
    assert True


def inc(x):
    return x + 1


def test_answer():
    if inc(4) == 5:
        pytest.skip("Fail")


@pytest.mark.skipif(sys.platform == "win32", reason="does not run on win")
def test_skipif():
    assert True


# @pytest.mark.xfail 实际结果失败的话返回XFAIL ,成功的话返回XPASS
@pytest.mark.xfail
def test_xfail():
    assert 1 == 1


mark = pytest.mark.xfail(reason="原因")


@mark
def test_xfail1():
    assert 1 == 2


# 代码中调用xfail，pytest.xfail(reason="该功能尚未完成")以下部分不执行

def test_xfail2():
    print('测试')
    pytest.xfail(reason="该功能尚未完成")
    assert 1 == 2


search_list = ['appium', 'selenium', 'pytest']


# @pytest.mark.parametrize 参数化
# 1、参数化的名字，需要与方法中的参数一样对应
# 2、如果传递多个参数的话，要放在列表中，列表中嵌套列表或者元组
# 3、ids的个数 == 传递的数据个数
@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list


@pytest.mark.parametrize('test_input,expected', [("3+5", 8), ("2+5", 7), ("5+5", 10)],
                         ids=["number1", "number2", "number3"])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected
