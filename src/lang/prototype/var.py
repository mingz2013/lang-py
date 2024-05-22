# -*- coding: utf-8 -*-
"""

Module Description

"""


class Var(object):
    TYPE_STORE_LOCAL = 1  # 在本级
    TYPE_STORE_SUPER = 0  # 在上一级

    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self):
        self.name = None
        self.data = None  # 数据
        self.store_type = -1
        self.value_type = -1
        self.idx = -1  # 在上一级的位置，或者在本级的位置
