from base.find_element import FindElement


class SearchElements(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = FindElement(self.driver)

    # 搜索框
    def search_input(self):
        return self.fd.get_element('search_input')

    # 百度一下按钮
    def search_button(self):
        return self.fd.get_element('search_button')

    # 搜索结果提示
    def search_result(self):
        return self.fd.get_element('search_result')
