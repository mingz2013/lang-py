# -*- coding: utf-8 -*-
"""
@FileName: prototype
@Time: 2020/2/7 15:16
@Author: zhaojm

Module Description

"""
from prototype.var import Var


class ProtoType(object):

    def __get_d(self):
        d = self.__dict__

        d['__class_name__'] = self.__class__.__name__

        return d

    def __str__(self):
        return str(self.__get_d())

    def __repr__(self):
        return repr(self.__get_d())

    def __init__(self, proto=None, name=None):
        # bin code
        self.name = name  # 函数名, 或者文件名
        self.code = []  # 指令表
        self.constants = []  # 常量表
        self.vars = []  # 变量 Var()
        # self.args = []  # 参数表

        self.proto = proto  # 父级 ProtoType

        self.protos = []  # 子函数原型表

    def add_name(self, n, local_must=False):
        """

        :param n: 名称
        :param local_must: 是否一定要存储到本地
        """

        if local_must:
            if self.find_name(n) >= 0:
                # local_must = True 的时候，肯定是第一次添加才对
                raise Exception('error in add name')
            var = Var()
            var.name = n
            var.data = None
            var.store_type = var.TYPE_STORE_LOCAL
            self.vars.append(var)
            return len(self.vars) - 1
        else:  # 不一定存储到本地
            # 如果本地没有，
            #   从上一级查找，直到找到所有的层级，
            #       如果有找到：
            #           就返回结果，并一层层存储下来，直到存储到本一层。
            #       如果没有找到：
            #           存储到本地
            i = self.find_super(n)
            if i < 0:
                # 上一级没找到，存储到本级
                var = Var()
                var.name = n
                var.data = None
                var.store_type = var.TYPE_STORE_LOCAL
                self.vars.append(var)
                i = len(self.vars) - 1
                var.idx = i

            return i

    def find_super(self, n):
        """
        从链上查找name
        """
        i = self.find_name(n)
        if i >= 0:
            # 本地找到直接返回
            return i

        if not self.proto:
            # 没有上一级直接返回
            return i

        i = self.proto.find_super(n)
        if i >= 0:
            # 上一级找到存储到本级
            v = Var()
            v.name = n
            v.store_type = v.TYPE_STORE_SUPER
            v.idx = i
            self.vars.append(v)
            return len(self.vars) - 1
        else:
            # 上一级也没找到返回
            return i

    def find_name(self, n):
        """
        从本级查找索引
        """
        for i, var in enumerate(self.vars):
            if var.name == n:
                return i
        return -1

    def get_name(self, idx):
        """
        用于调试打印，
        """
        return self.vars[idx].name

    def add_constant(self, c):
        if c in self.constants:
            return self.constants.index(c)
        self.constants.append(c)
        return len(self.constants) - 1

    def load_constant(self, idx):
        return self.constants[idx]

    def add_sub_proto(self, p):
        self.protos.append(p)
        return len(self.protos) - 1

    def load_sub_proto(self, idx):
        return self.protos[idx]

    def add_code(self, code):
        print("add code<<", code)
        self.code.append(code)
        return len(self.code) - 1

    def get_code(self, idx):
        if idx >= len(self.code):
            return -1
        return self.code[idx]

    @property
    def code_len(self):
        return len(self.code)

    def clone(self):
        """
        clone
        """

    def parse(self, reader):
        """
        用于解析数据
        """
