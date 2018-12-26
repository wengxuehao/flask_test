#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 0. pip install selenium

# 1. 导入模块
from selenium import webdriver
import time

# 2. 通过驱动路径构建浏览器对象
# 传递驱动文件路径
browser = webdriver.Chrome("C:\seleniumdirver\chromedriver.exe")

# 3. 控制浏览器
# time.sleep(10)
# 解决打开浏览器输入不了网址错误，是驱动版本和浏览器不匹配
browser.get("http://www.baidu.com")

input_element = browser.find_element_by_id("kw")
# time.sleep(10)
input_element.send_keys("传智播客")
browser.save_screenshot('传智博客截图1.png')
time.sleep(10)
button_element = browser.find_element_by_id('su')
button_element.click()

# 添加等待时常
time.sleep(10)
site_element = browser.find_element_by_class_name("favurl")
print(site_element.get_attribute('href'))
print(site_element.text)
site_element.click()

time.sleep(60)

# 4. 退出浏览器
browser.quit()
