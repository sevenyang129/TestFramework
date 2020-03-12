# -*- coding: UTF-8 -*-
import os
from selenium import webdriver
from pathlib import Path

def web_url():
    return 'https://lanhuapp.com/web/#/user/login'

def img_path(img_name):
    i_path = str(Path.home()) + '/images/new_images/' + img_name + '.png'
    return i_path


class RunDriver(object):
    def __init__(self, dr_path=None):
        """
        需要用到 FireFox 把 config 内的 geckodriver 复制到 /usr/local/bin 内;
        使用 Safari 需要把浏览器偏好设置内的开发标签打开，并勾选“允许自动化运行”
        使用时，引入该模块，RunDriver(dr_path='路径位置').run_driver(driver='浏览器名称')
        """
        home = str(Path.home())
        if dr_path is None:
            self.dr_path = home + '/TestingFramework/config/chromedriver'

        # print(self.dr_path)
    def run_driver(self, driver=None):
        if driver is None:
            return webdriver.Chrome(self.dr_path)
        elif driver == 'FireFox':
            return webdriver.Firefox()
        elif driver == 'Safari':
            return webdriver.Safari()



if __name__ == '__main__':
    pass