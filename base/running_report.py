import os
import time
from config import HTMLTestReportCN
from pathlib import Path

class RunningReport(object):
    """
        初始化参数，报告路径，报告 title 和描述。
    report_file_path: 报告生成存放路径，
    参数为 None 时 目标 py 文件在根目录下的文件夹内时使用；
    参数为 1 时 目标 py 文件直接在根目录下时使用；
     外部需要生成报告时，import running_report, 在执行时对 RunningReport() 赋值，
    按需传入 report_file_path 路径，其他参数值可不填，
    执行 RunningReport()下的函数 run_report() 运行指令。
    """


    def __init__(self, report_file_path=None, title=None, description=None):

        path_time = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
        # 获取 home 路径
        home = str(Path.home())

        if report_file_path is None:
            self.report_file_path = home + '/TestingFramework/report/' + path_time + '.html'

        if title is None:
            self.title = 'LanHu test report'
        if description is None:
            self.description = 'LanHu web testing'

        self.fw = open(self.report_file_path, 'wb')
        self.runner = HTMLTestReportCN.HTMLTestRunner(
            stream=self.fw, title=self.title, description=self.description, verbosity=2)

    def run_report(self, suite):
        self.runner.run(suite)

# if __name__ == '__main__':
#     r = RunningReport()
#     r.run_report()
