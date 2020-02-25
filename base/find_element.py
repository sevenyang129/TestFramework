# -*- coding: UTF-8 -*-

from util.read_ini import ReadIni
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindElement(object):
    """
    初始化内引用 read_ini.py 读取配置文件内的 element 信息传递给 get_element & get_elements 两个函数使用。
    key : 继承自 read_ini.py 内的 get_value 读取配置文件信息;
    get_elements(target) : 对 elements 定位方式拿回的数据，循环查找匹配对象的赋值变量;
    """

    def __init__(self, driver, ini_file_path=None, node=None):
        self.driver = driver
        self.read_ini = ReadIni(ini_file_path=ini_file_path, node=node)
        self.read_inis = ReadIni(ini_file_path=ini_file_path, node=node)

    # element 基础定位方式
    def get_element(self, key):
        data = self.read_ini.get_value(key)
        by = data.split('->')[0]
        element = data.split('->')[1]
        try:
            if by == 'id':
                try:
                    ele = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, element)))
                    return ele
                except Exception as e:
                    raise e

            elif by == 'xpath':
                try:
                    ele = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, element)))
                    return ele
                except Exception as e:
                    raise e

            elif by == 'css':
                try:
                    ele = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
                    return ele
                except Exception as e:
                    raise e
        except:
            return None

    # elements 定位方式
    def get_elements(self, key, target):
        datas = self.read_inis.get_value(key)
        bys = datas.split('->')[0]
        elements = datas.split('->')[1]
        try:
            if bys == 'xpath':
                items = self.driver.find_elements_by_xpath(elements)
                for i in items:
                    if i.text == target:
                        return i
            if bys == 'css':
                items = self.driver.find_elements_by_css_selector(elements)
                for i in items:
                    if i.text == target:
                        return i
        except:
            return None

    # 鼠标悬浮
    def hover_element(self, key):
        el = key
        ActionChains(self.driver).move_to_element(el).perform()


if __name__ == '__main__':
    pass