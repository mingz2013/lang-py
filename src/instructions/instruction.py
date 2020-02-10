# -*- coding: utf-8 -*-
"""
@FileName: instruction
@Time: 2020/2/4 15:37
@Author: zhaojm

Module Description


定义字节码


opcode 0-7 8

idx 8-15 8

16bit



"""


class Executes(object):
    def __init__(self):
        pass

    def lc(self, opcode, vm):
        vm.cur_frame.load_const(opcode.idx)

    def sc(self, opcode, vm):
        vm.cur_frame.store_const(opcode.idx)

    def ln(self, opcode, vm):
        vm.cur_frame.load_name(opcode.idx)

    def sn(self, opcode, vm):
        vm.cur_frame.store_name(opcode.idx)

    def nop(self, opcode, vm):
        """"""

    def add(self, opcode, vm):
        vm.cur_frame.add()

    def sub(self, opcode, vm):
        vm.cur_frame.sub()

    def mul(self, opcode, vm):
        vm.cur_frame.mul()

    def div(self, opcode, vm):
        vm.cur_frame.div()

    def rem(self, opcode, vm):
        vm.cur_frame.rem()

    def jmp(self, opcode, vm):
        vm.add_pc(opcode.idx)

    def call(self, opcode, vm):
        nArgs, nResults = opcode << 0xff, opcode << 0xffff
        vm.call(nArgs, nResults)

    def ret(self, opcode, vm):
        vm.ret()


opcodes = [
    ('opcode', 'type', 'name', 'desc'),

    (0b00000000, 0b0, 'nop', ''),

    (0b00000000, 0b0, 'add', ''),
    (0b00000000, 0b0, 'sub', ''),
    (0b00000000, 0b0, 'mul', ''),
    (0b00000000, 0b0, 'div', ''),
    (0b00000000, 0b0, 'rem', ''),

    (0b00000000, 0b0, 'call', ''),
    (0b00000000, 0b0, 'ret', ''),

    (0b00000000, 0b1, 'lc', 'load const'),
    (0b00000000, 0b1, 'sc', 'store const'),
    (0b00000000, 0b1, 'ln', 'load name'),
    (0b00000000, 0b1, 'sn', 'store name'),

    (0b00000000, 0b1, 'j', 'jmp'),

]


def LoadConst(idx):
    """

    """
    return None


def LoadName(idx):
    """

    """
    return None


def StoreName(idx):
    return None


def MakeList(length):
    """

    """
    return None


def MakeFunction():
    return None


def CallFunction(length):
    """

    """
    return None


def Ret():
    return None


def Push(obj):
    """

    """
    return None


def Pop():
    return None


def Add():
    return None


def Sub():
    return None


def Mul():
    return None


def Div():
    return None


def Rem():
    return None


def Eq():
    """
    Equal
    """
    return None


def Neq():
    """
    not equal
    """
    return None


def Lt():
    """
    less than
    """
    return None


def Lte():
    """
    less than or equal
    """
    return None


def Gt():
    """
    greater than
    """
    return None


def Gte():
    """
    greator than or equal
    """
    return None


def Is():
    """
    is
    """
    return None


def In():
    """
    in
    """
    return None


def Or():
    """
    or
    """
    return None


def And():
    """
    And
    """
    return None


def Not():
    """
    not
    """
    return None


def Print(length):
    """
    print
    """
    return None
