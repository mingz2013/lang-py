# -*- coding: utf-8 -*-
"""
@FileName: stack
@Time: 2020/2/4 14:18
@Author: zhaojm

Module Description

"""


class StackNode(object):
    def __get_d(self):
        d = self.__dict__

        d['__class_name__'] = self.__class__.__name__

        return d

    def __str__(self):
        return str(self.__get_d())

    def __repr__(self):
        return repr(self.__get_d())

    def __init__(self):
        self.prev = None
        self.data = None


class Stack(object):
    def __get_d(self):
        d = self.__dict__

        d['__class_name__'] = self.__class__.__name__

        return d

    def __str__(self):
        return str(self.__get_d())

    def __repr__(self):
        return repr(self.__get_d())

    def __init__(self):
        self.top_node = None
        self.back_node = None

    def push(self, node):
        assert isinstance(node, StackNode)
        node.prev = self.top_node
        self.top_node = node

    def pop(self):
        node = self.top_node
        self.top_node = node.prev
        return node
