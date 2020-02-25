### 主要用途
    该模块是测试报告封装模块，配合引入 config 内的 HTMLTestReportCN 使用。

### 主要参数说明
    初始化参数，报告路径，报告 title 和描述。
    report_file_path: 报告生成存放路径，
    参数为 None 时 目标 py 文件在根目录下的文件夹内时使用；
    参数为 1 时 目标 py 文件直接在根目录下时使用；

### 模块说明
    外部需要生成报告时，import running_report, 在执行时对 RunningReport() 赋值，
    按需传入 report_file_path 路径，其他参数值可不填，
    执行 RunningReport()下的函数 run_report() 运行指令。 
    
    示例：
    report = RunningReport(report_file_path=1)
    suite = unittest.TestSuite()
    suite.addTest(ClassName('test_case'))
    report.run_report(suite=suite)