# -*- coding: utf-8 -*-
"""
@FileName: closure
@Time: 2020/2/12 18:09
@Author: zhaojm

Module Description


闭包，存储运行时的数据

"""

import copy

from prototype.member import Member


class Closure(object):
    # def __get_d(self):
    #     d = self.__dict__
    #
    #     d['__class_name__'] = self.__class__.__name__
    #
    #     return d
    #
    # def __str__(self):
    #     return str(self.__get_d())
    #
    # def __repr__(self):
    #     return repr(self.__get_d())

    def __init__(self, super, proto):
        self.super = super  # 调用链的实现，有了这条调用链，就可以找到往上所有的环境，从而找到对应的数据。用于实现闭包的变量捕获。
        self.proto = proto  # 当前函数的原型
        self.vars = copy.deepcopy(proto.vars)  # 局部变量表
        self.members = copy.deepcopy(proto.members)  # 成员表，用于实现面向对象

    def store_name(self, idx, a):
        var = self.vars[idx]
        print(self, 'closure.store_name << var:', var, "a", a)
        if var.store_type == var.TYPE_STORE_LOCAL:
            var.data = a
        elif var.store_type == var.TYPE_STORE_SUPER:
            return self.super.store_name(var.idx, a)
        else:
            raise Exception("un except type", var.store_type)

    def load_name(self, idx):
        var = self.vars[idx]
        print(self, 'closure.load_name << var:', var)
        if var.store_type == var.TYPE_STORE_LOCAL:
            return self.vars[idx].data
        elif var.store_type == var.TYPE_STORE_SUPER:
            return self.super.load_name(var.idx)
        else:
            raise Exception("un except type", var.store_type)

    def get_name(self, idx):
        """
        用于调试打印，
        用于设置name store member
        """
        return self.vars[idx].name

    def store_member(self, idx, a):
        member = self.members[idx]
        member.data = a

    def load_member(self, idx):
        return self.members[idx].data

    def get_member_idx(self, name):
        for idx, member in enumerate(self.members):
            if member.name == name:
                return idx
        member = Member()
        member.name = name
        member.data = None
        self.members.append(member)
        idx = len(self.members) - 1
        member.idx = idx
        return idx
