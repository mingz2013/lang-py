# -*- coding: utf-8 -*-
"""
@FileName: var
@Time: 2020/2/12 20:52
@Author: zhaojm

Module Description

"""


class Var(object):
    TYPE_STORE_LOCAL = 1  # 在本级
    TYPE_STORE_SUPER = 0  # 在上一级

    def __init__(self):
        self.name = None
        self.data = None  # 数据
        self.store_type = None
        self.value_type = None
        self.idx = -1  # 在上一级的位置，或者在本级的位置
