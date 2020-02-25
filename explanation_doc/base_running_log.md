### 主要用途
    模块只有拥有在 PageTest 中生成必要的测试日志，
    以便分析和定位运行中的问题。

### 主要参数
    log_file_path: 日志生成存放路径；
    参数为 None 时 目标 py 文件在根目录下的文件夹内时使用；
    参数为 1 时 目标 py 文件直接在根目录下时使用；
    日志命名为当前本地时间；
    formatter: 单行日志打印参数与样式，具体参数说明请看 Formatter 模块注释。

### 模块说明
    在 unittest 框架内使用时，引入 running_log 模块，setUp 时赋值其模块下的 get_log() 函数；
    例如:
         cls.log = RunningLog(logger='TestCase', log_file_path=1)
            cls.logger = cls.log.get_log()
     
    在用例执行完成后 tearDown 内 使用 close_handle() 结束日志程序，释放内存资源；
    例如:
         cls.log.close_handle()