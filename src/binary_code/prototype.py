# -*- coding: utf-8 -*-
"""
@FileName: prototype
@Time: 2020/2/7 15:16
@Author: zhaojm

Module Description

"""


class ProtoType(object):
    def __init__(self):
        # bin code
        self.source_name = ""  # 源文件名
        self.name = ""  # 函数名
        self.code = []  # 指令表
        self.constants = []  # 常量表
        self.names = []  # 变量名
        self.args = []  # 参数表
        self.local_vars = []  # 局部变量表
        self.protos = []  # 子函数原型表

        # vm
        self.proto = None  # 指向上一级的指针

    def add_name(self, n):
        self.names.append(n)
        return len(self.names) - 1

    def add_constant(self, c):
        self.constants.append(c)
        return len(self.constants) - 1

    def add_sub_proto(self, p):
        self.protos.append(p)
        return len(self.protos) - 1

    def add_code(self, *code):
        print("add code<<", *code)
        self.code.append(code)
        return len(self.code) - 1

    def clone(self):
        """
        clone
        """

    def parse(self, reader):
        """
        用于解析数据
        """
