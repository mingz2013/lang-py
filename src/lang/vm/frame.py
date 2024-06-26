# -*- coding: utf-8 -*-
"""

Module Description

"""
from typing import List, Any

from lang import logger
from lang.instructions.instruction import Instruction
from lang.prototype.prototype import ProtoType
from lang.vm.closure import Closure
from lang.vm.stack_node import StackNode


class Stack(object):
    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self):
        self.data: List[Any] = []

    def pop(self):
        return self.data.pop()

    def push(self, obj):
        self.data.append(obj)

    def top(self):
        return self.data[-1]


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

    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self, closure: Closure):
        super(Frame, self).__init__()
        self._pc: int = 0  # program counter
        # self.proto = proto  # ProtoType, 函数原型，用于从函数原型里面读取常量，指令等
        self.closure: Closure = closure  # 闭包

        self.stack: Stack = Stack()  # 栈

        # self.args = []  # 参数
        # self.results = []  # 结果

    @property
    def proto(self) -> ProtoType:
        return self.closure.proto

    @property
    def pc(self) -> int:
        return self._pc

    def fetch(self) -> Instruction:
        """
        取指
        """
        i = self.proto.get_code(self._pc)
        self._pc += 1
        return i

    def j(self, n: int):
        self._pc += n

    def jif(self, n: int):
        a = self.stack.pop()
        if not a:
            self._pc += n

    def top(self):
        return self.stack.top()

    def pop(self):
        return self.stack.pop()

    def push(self, obj):
        self.stack.push(obj)

    def add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        if type(a) != type(b):
            logger.debug("not type equal", a, b)
            # raise Exception(a, b, 'not type equal')
            # return
        c = a + b
        self.stack.push(c)

    def sub(self):
        b = self.stack.pop()
        a = self.stack.pop()
        if type(a) != type(b):
            logger.debug("not type equal", a, b)
            # raise Exception(a, b, 'not type equal')
            # return
        c = a - b

        self.stack.push(c)

    def div(self):
        b = self.stack.pop()
        a = self.stack.pop()
        c = a / b
        self.stack.push(c)

    def mul(self):
        b = self.stack.pop()
        a = self.stack.pop()
        c = a * b
        self.stack.push(c)

    def rem(self):
        b = self.stack.pop()
        a = self.stack.pop()
        c = a % b
        self.stack.push(c)

    def lc(self, idx: int):
        """
        load const
        获取常量, 放到栈顶
        """
        a = self.proto.load_constant(idx)
        self.stack.push(a)

    def sc(self, idx: int):
        """

        """

    def ln(self, idx: int):
        """

        """
        a = self.closure.load_name(idx)
        self.stack.push(a)

    def sn(self, idx: int):
        """"""
        a = self.stack.pop()
        self.closure.store_name(idx, a)

    def lm(self, idx: int):
        """
        load member
        """
        name = self.closure.get_name(idx)

        closure = self.stack.pop()

        idx = closure.get_member_idx(name)
        data = closure.load_member(idx)
        self.stack.push(data)

    def sm(self, idx: int):
        """
        store member
        """
        name = self.closure.get_name(idx)

        closure = self.stack.pop()
        data = self.stack.pop()

        idx = closure.get_member_idx(name)
        closure.store_member(idx, data)

    # def lmd(self, idx):
    #     pass

    def lp(self):
        idx = self.stack.pop()
        p = self.proto.load_sub_proto(idx)
        c = Closure(self.closure, p)
        self.stack.push(c)

    def ml(self, idx: int):
        """

        """
        l = []
        for i in range(idx):
            a = self.stack.pop()
            l.append(a)
        l.reverse()
        self.stack.push(l)

    def mf(self, idx: int):
        """"""
        raise Exception("un mf")

    def eq(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a == b
        self.stack.push(c)

    def neq(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a != b
        self.stack.push(c)

    def lt(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a < b
        self.stack.push(c)

    def lte(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a <= b
        self.stack.push(c)

    def gt(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a > b
        self.stack.push(c)

    def gte(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a >= b
        self.stack.push(c)

    def is_(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a is b
        self.stack.push(c)

    def in_(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        # print("in_", a, b)
        c = a in b
        self.stack.push(c)

    def or_(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a or b
        self.stack.push(c)

    def and_(self):
        """"""
        b = self.stack.pop()
        a = self.stack.pop()
        c = a and b
        self.stack.push(c)

    def not_(self):
        """"""
        a = self.stack.pop()
        c = not a
        self.stack.push(c)

    def print(self, idx: int):
        """"""""
        logger.debug("print<< ", idx)
        args = [self.stack.pop() for i in range(idx)]
        # print("print<< args: ", args)
        args.reverse()
        print(*args)
