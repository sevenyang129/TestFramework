### 用途
    主要功能是为了读取 config 目录下的 ini 配置文件。配置文件内存放自动化需要用的 element 对象路径。
    
### 主要参数说明
    file_name : ini 配置文件路径，为了 Git 和多人协作共用测试用例，该文件路径提交时不允许写死！！！ 需要使用工程所在的相对路径。
    node : ini 配置文件内的节点名称，通过定位对应节点名称，可以更快的查找到对象 element 对象。
    get_value(self, key) : key 对应 ini 配置文件内的 element 对象 key。
    file_name & node 有默认参数，调用时可以按需求进行实例化或更改。
    key 调用时必须实例化。
    
### 模块说明
    初始化对应路径内的 ini 配置文件（node 可用默认值，调用时实例化）；
    把路径带入到 load_ini 函数通过 [configparser] model 读取配置文件；
    通过 get_value 函数对拿到的配置文件进行 element 查找操作。
    