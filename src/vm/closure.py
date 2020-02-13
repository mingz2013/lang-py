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
        self.super = super  # 调用链的实现，有了这条调用链，就可以找到往上所有的环境，从而找到对应的数据
        self.proto = proto
        self.local_vars = copy.deepcopy(proto.vars)  # 局部变量表

    def store_name(self, idx, a):
        var = self.local_vars[idx]
        if var.store_type == var.TYPE_STORE_LOCAL:
            var.data = a
        elif var.store_type == var.TYPE_STORE_SUPER:
            return self.super.store_name(var.idx, a)
        else:
            raise Exception("un except type", var.store_type)

    def load_name(self, idx):
        var = self.local_vars[idx]
        if var.store_type == var.TYPE_STORE_LOCAL:
            return self.local_vars[idx].data
        elif var.store_type == var.TYPE_STORE_SUPER:
            return self.super.load_name(var.idx)
        else:
            raise Exception("un except type", var.store_type)
