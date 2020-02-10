# -*- coding: utf-8 -*-
"""
@FileName: frame
@Time: 2020/2/4 14:14
@Author: zhaojm

Module Description

"""

from vm.stack import StackNode


class Stack(object):
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, obj):
        self.data.append(obj)


class Frame(StackNode):
    """
    Frame

    一个函数内部的寄存器，或者是堆栈


    提供基本的寄存器操作方法，
    或者栈的基本操作方法


    用于实现：
    算术运算符
    比较运算符


    """

    def __init__(self, proto, args, results):
        super(Frame, self).__init__()
        self._pc = 0  # program counter
        self.proto = proto  # ProtoType, 函数原型，用于从函数原型里面读取常量，指令等
        self.stack = Stack()  # 栈

        self.args = args  # 参数
        self.results = results  # 结果

    def pop(self):
        return self.stack.pop()

    def push(self, obj):
        self.stack.push(obj)

    @property
    def pc(self):
        return self._pc

    def add_pc(self, n):
        self._pc += n

    def fetch(self):
        """
        取指
        """
        i = self.proto.code[self.pc]
        self._pc += 1
        return i

    def get_const(self, idx):
        """
        获取常量, 放到栈顶
        """
        c = self.proto.constants[idx]
        self.stack.push(c)

    def add(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a + b
        self.stack.push(c)

    def sub(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a - b
        self.stack.push(c)

    def div(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a / b
        self.stack.push(c)

    def mul(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a * b
        self.stack.push(c)
