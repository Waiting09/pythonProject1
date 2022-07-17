# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 17:11
# @Author  : L
# @File    : test_case.py

# @pytest.mark.skip #跳过这个用例

from selenium import webdriver
import time

driver = webdriver.Chrome()
# 打开百度首页
driver.get("http://fdhkftest.realtynavi.com")
import requests
# 窗口最大化
driver.maximize_window()
# 获取窗口大小
# wind = driver.get_window_size()
# 打印出窗口大小
# print("窗口大小为：",wind)
