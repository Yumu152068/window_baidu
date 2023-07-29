
import sys
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException as e
import window as w
driver = webdriver.Edge()
driver.get('https://www.baidu.com/')
sr = driver.find_element(By.NAME, 'wd')
try:
    a = ''
    def none(a):
        if a == '':
            a = w.window()
            none(a)
        return a
    a = none(a)
    sr.send_keys(a)
    su = driver.find_element(By.ID, 'su')

    su.click()
except NameError:
    sys.exit()

while True:
    try:
        cur_url = driver.current_url
    except e:
        break