# -*- coding: utf-8 -*-
"""
@FileName: stack
@Time: 2020/2/4 14:18
@Author: zhaojm

Module Description

"""


class StackNode(object):
    def __init__(self):
        self.prev = None
        self.data = None


class Stack(object):
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
