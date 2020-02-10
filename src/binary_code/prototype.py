# -*- coding: utf-8 -*-
"""
@FileName: prototype
@Time: 2020/2/7 15:16
@Author: zhaojm

Module Description

"""


class ProtoType(object):
    def __init__(self):
        self.source_name = ""  # 源文件名
        self.proto = None  # 指向上一级的指针
        self.name = ""  # 函数名
        self.code = []  # 指令表
        self.constants = []  # 常量表
        self.args = []  # 参数表
        self.local_vars = []  # 局部变量表
        self.protos = []  # 子函数原型表

    def clone(self):
        """
        clone
        """

    def parse(self, reader):
        """
        用于解析数据
        """
