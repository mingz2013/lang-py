# -*- coding: utf-8 -*-
"""
@FileName: vm
@Time: 2020/2/4 14:13
@Author: zhaojm

Module Description

"""

from instructions import instruction
from prototype.prototype import ProtoType
from vm.frame import Frame
from vm.stack import Stack


class VM(object):
    """
    VM
    Virtual Machine
    """

    def __init__(self, filename):
        self.prototype = ProtoType()  # 二进制文件解析后的数据
        self.stack = Stack()  # callstack

    def init(self, args):
        """
        vm call, 初始执行
        """
        f = Frame(self.prototype)
        for a in args:
            f.push(a)

        self.stack.push(f)

        self.loop()

    def loop(self):
        while True:
            data = self.frame.fetch()
            inst = instruction.Instruction.from_inst(data)
            inst.execute(self)

    @property
    def frame(self):
        return self.stack.top_node

    @property
    def pc(self):
        return self.frame.pc

    def add_pc(self, n):
        self.frame.add_pc(n)

    def call(self, idx):
        """

        对于调用者函数：

        函数调用的时候，
        1 先将结果寄存器按顺序推入栈
        2 再将参数寄存器推入栈
        3 再将调用的函数原型推入栈
        4 执行call指令

        执行函数调用，
        1 先弹出函数原型
        2 再弹出参数列表
        3 再弹出结果列表



        对于被调用者函数：

        函数调用的时候，
        1 帧里面，保存了参数列表，结果列表
        2 执行字节码，可修改结果列表
        3 调用结束，最后执行ret指令

        """

        proto = self.frame.pop()
        f = Frame(proto)

        for i in range(idx):
            a = self.frame.pop()
            f.push(a)

        self.stack.push(f)

    def ret(self, idx):
        """
        函数返回的时候，
        1 取出结果列表
        2 弹出栈帧
        3 将结果列表压入调用者的栈帧

        """
        f = self.stack.pop()

        for i in range(idx):
            a = f.pop()
            self.frame.push(a)

    def j(self, idx):
        self.add_pc(idx)

    def nop(self):
        """"""
        pass

    def add(self):
        self.frame.add()

    def sub(self):
        self.frame.sub()

    def mul(self):
        self.frame.mul()

    def div(self):
        self.frame.div()

    def rem(self):
        self.frame.rem()

    def lc(self, idx):
        self.frame.lc(idx)

    def sc(self, idx):
        self.frame.sc(idx)

    def ln(self, idx):
        self.frame.ln(idx)

    def sn(self, idx):
        self.frame.sn(idx)

    def ml(self, idx):
        self.frame.ml(idx)

    def mf(self, idx):
        self.frame.mf(idx)

    def push(self):
        self.frame.push()

    def pop(self):
        self.frame.pop()

    def eq(self):
        self.frame.eq()

    def neq(self):
        self.frame.neq()

    def lt(self):
        self.frame.lt()

    def lte(self):
        self.frame.lte()

    def gt(self):
        self.frame.gt()

    def gte(self):
        self.frame.gte()

    def is_(self):
        self.frame.is_()

    def in_(self):
        self.frame.in_()

    def or_(self):
        self.frame.or_()

    def and_(self):
        self.frame.and_()

    def not_(self):
        self.frame.not_()

    def print(self, idx):
        self.frame.print(idx)
