### 主要用途
    封装主要元素定位方法，和鼠标事件。
    
### 主要参数说明
    初始化内引用 read_ini.py 读取配置文件内的 element 信息传递给 get_element & get_elements 两个函数使用。
    key : 继承自 read_ini.py 内的 get_value 读取配置文件信息;
    get_elements(target) : 对 elements 定位方式拿回的数据，循环查找匹配对象的赋值变量;
     
### 模块说明
    对读取到的配置文件内容带入到 get_element & get_elements 
    两个函数内进行分割判断调用对应的定位方法。