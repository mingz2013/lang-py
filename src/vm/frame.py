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


    提供基本的寄存器操作方法，寄存器式虚拟机
    或者栈的基本操作方法，栈式虚拟机


    用于实现：
    算术运算符
    比较运算符


    """

    def __init__(self, proto):
        super(Frame, self).__init__()
        self._pc = 0  # program counter
        self.proto = proto  # ProtoType, 函数原型，用于从函数原型里面读取常量，指令等
        self.stack = Stack()  # 栈

        self.args = []  # 参数
        self.results = []  # 结果

    @property
    def pc(self):
        return self._pc

    def fetch(self):
        """
        取指
        """
        i = self.proto.get_code(self._pc)
        self._pc += 1
        return i

    def j(self, n):
        self._pc += n

    def pop(self):
        return self.stack.pop()

    def push(self, obj):
        self.stack.push(obj)

    def add(self):
        a = self.stack.pop()
        b = self.stack.pop()
        if type(a) != type(b):
            raise Exception(a, b, 'not type equal')
            # return
        c = a + b
        self.stack.push(c)

    def sub(self):
        a = self.stack.pop()
        b = self.stack.pop()
        if type(a) != type(b):
            raise Exception(a, b, 'not type equal')
            # return
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

    def rem(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a % b
        self.stack.push(c)

    def lc(self, idx):
        """
        load const
        获取常量, 放到栈顶
        """
        a = self.proto.load_constant(idx)
        self.stack.push(a)

    def sc(self, idx):
        """

        """

    def ln(self, idx):
        """

        """
        a = self.proto.load_name(idx)
        self.stack.push(a)

    def sn(self, idx):
        """"""
        a = self.stack.pop()
        self.proto.store_name(idx, a)

    def ml(self, idx):
        """

        """
        l = []
        for i in range(idx):
            a = self.stack.pop()
            l.append(a)
        self.stack.push(l)

    def mf(self, idx):
        """"""

    def eq(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a == b
        self.stack.push(c)

    def neq(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a != b
        self.stack.push(c)

    def lt(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a < b
        self.stack.push(c)

    def lte(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a <= b
        self.stack.push(c)

    def gt(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a > b
        self.stack.push(c)

    def gte(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a >= b
        self.stack.push(c)

    def is_(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a is b
        self.stack.push(c)

    def in_(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        print("in_", a, b)
        c = a in b
        self.stack.push(c)

    def or_(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a or b
        self.stack.push(c)

    def and_(self):
        """"""
        a = self.stack.pop()
        b = self.stack.pop()
        c = a and b
        self.stack.push(c)

    def not_(self):
        """"""
        a = self.stack.pop()
        c = not a
        self.stack.push(c)

    def print(self, idx):
        """"""""
        args = [self.stack.pop() for i in range(idx)]
        print(*args)
