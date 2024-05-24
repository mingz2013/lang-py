# -*- coding: utf-8 -*-
"""

Module Description

"""
from lang.vm.frame import Frame
from lang.vm.stack_node import StackNode


class Stack(object):
    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self):
        self.top_node: Frame = None
        self.back_node: Frame = None

    def push(self, node: StackNode):
        assert isinstance(node, StackNode)
        node.prev = self.top_node
        self.top_node = node

    def pop(self) -> Frame:
        node = self.top_node
        self.top_node = node.prev
        return node
