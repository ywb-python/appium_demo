#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 22:57
# @Author  : ywb
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

from appium import webdriver

# TODO：设置终端参数
desired_apps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "Samsung Galaxy S10",
    "appPackage": "com.taobao.taobao",
    "appActivity": "com.taobao.tao.welcome.Welcome",
    "noReset": True
}

# TODO：启动appium server
# TODO：模拟器、真机必须能够被电脑识别
# TODO：发送指令给appium server
webdriver.Remote('http://127.0.0.1:62001/wd/hub', desired_apps)




