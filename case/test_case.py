# -*- coding: UTF-8 -*-
import unittest
from time import sleep
from base.running_log import RunningLog
from base.running_driver import RunDriver
from base.running_report import RunningReport
from config.HTMLTestReportCN import DirAndFiles
from base import running_driver
from page_elements.search_elements import SearchElements


class TestBaiDu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = RunningLog(logger='TestBaiDu')
        cls.logger = cls.log.get_log()

    def setUp(self) -> None:
        self.driver = RunDriver().run_driver()
        self.driver.implicitly_wait(10)
        self.driver.get(running_driver.web_url())
        self.driver.set_window_size(1200, 1000)
        self.search_ele = SearchElements(self.driver)

    def test_case_1(self):
        self.search_ele.search_input().send_keys('python')
        self.search_ele.search_button().click()
        try:
            self.assertTrue(self.search_ele.search_result())
            self.logger.info('search result succeed')
        except:
            self.logger.error('Search target not found')
            DirAndFiles.get_screenshot(self.driver, 'search_result')

    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.close_handle()


if __name__ == '__main__':
    report = RunningReport()
    suite = unittest.TestSuite()
    suite.addTest(TestBaiDu('test_case_1'))
    report.run_report(suite=suite)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)