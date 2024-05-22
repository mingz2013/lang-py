# -*- coding: utf-8 -*-
"""

Module Description

"""


class StackNode(object):
    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self):
        self.prev = None
        self.data = None


class Stack(object):
    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

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
