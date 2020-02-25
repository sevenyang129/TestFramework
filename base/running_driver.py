# -*- coding: UTF-8 -*-
import os
from selenium import webdriver


def web_url():
    return 'https://www.baidu.com'

def img_path(img_name):
    return os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'images', 'new_images', img_name + '.png')


class RunDriver(object):
    def __init__(self, dr_path=None):
        """
        需要用到 FireFox 把 config 内的 geckodriver 复制到 /usr/local/bin 内;
        使用 Safari 需要把浏览器偏好设置内的开发标签打开，并勾选“允许自动化运行”
        使用时，引入该模块，RunDriver(dr_path='路径位置').run_driver(driver='浏览器名称')
        """
        if dr_path is None:
            self.dr_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'config', 'chromedriver')
        elif dr_path == 1:
            self.dr_path = os.path.join(os.getcwd(), 'config', 'chromedriver')
        # print(self.dr_path)
    def run_driver(self, driver=None):
        if driver is None:
            return webdriver.Chrome(self.dr_path)
        elif driver == 'FireFox':
            return webdriver.Firefox()
        elif driver == 'Safari':
            return webdriver.Safari()