# -*- coding: utf-8 -*-
"""
@FileName: closure
@Time: 2020/2/12 18:09
@Author: zhaojm

Module Description


闭包，存储运行时的数据

"""

import copy


class Closure(object):

    def __init__(self, super, proto):
        self.super = super  # 调用链的实现，有了这条调用链，就可以找到往上所有的环境，从而找到对应的数据。用于实现闭包的变量捕获。
        self.proto = proto  # 当前函数的原型
        self.vars = copy.deepcopy(proto.vars)  # 局部变量表
        self.members = copy.deepcopy(proto.members)  # 成员表，用于实现面向对象

    def store_name(self, idx, a):
        var = self.vars[idx]
        if var.store_type == var.TYPE_STORE_LOCAL:
            var.data = a
        elif var.store_type == var.TYPE_STORE_SUPER:
            return self.super.store_name(var.idx, a)
        else:
            raise Exception("un except type", var.store_type)

    def load_name(self, idx):
        var = self.vars[idx]
        if var.store_type == var.TYPE_STORE_LOCAL:
            return self.vars[idx].data
        elif var.store_type == var.TYPE_STORE_SUPER:
            return self.super.load_name(var.idx)
        else:
            raise Exception("un except type", var.store_type)

    def store_member(self, idx, a):
        member = self.members[idx]
        member.data = a

    def load_member(self, idx):
        return self.members[idx].data
