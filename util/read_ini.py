# -*- coding: UTF-8 -*-
import os
import configparser
from pathlib import Path

class ReadIni(object):
    # 初始化目录与节点路径

    def __init__(self, ini_file_path=None, node=None):
        if ini_file_path is None:
            # 获取 home 路径
            home = str(Path.home())
            # 配置文件路径
            ini_file_path = home + '/TestingFramework/config/PageElement.ini'
        if node is None:
            self.node = 'LoginPageElement'
        else:
            self.node = node
        self.cf = self.load_ini(ini_file_path)

    # 读取 ini 文件
    def load_ini(self, ini_file_path):
        cf = configparser.ConfigParser()
        cf.read(ini_file_path)
        return cf

    # 获取对应节点的 key
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    run_ReadIni = ReadIni()
