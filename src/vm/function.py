# -*- coding: utf-8 -*-
"""
@FileName: function
@Time: 2020/2/12 15:52
@Author: zhaojm

Module Description


从原型生成function，真正执行的应该是function。
一些临时变量存储到function中。而不能存储到原型中。
如果存储到原型中，再次调用这个原型函数的时候，就会有上一次调用时候的数据污染。

"""


class Function(object):
    """
    Function,
    """

    def __init__(self, proto):
        self.proto = proto
        self.vars = []  # name绑定的
        self.functions = []  # 调用
