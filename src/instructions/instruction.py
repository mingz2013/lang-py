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
import functools
import struct


class Executes(object):
    def __init__(self):
        pass

    def nop(self, inst, vm):
        """"""

    def add(self, inst, vm):
        vm.cur_frame.add()

    def sub(self, inst, vm):
        vm.cur_frame.sub()

    def mul(self, inst, vm):
        vm.cur_frame.mul()

    def div(self, inst, vm):
        vm.cur_frame.div()

    def rem(self, inst, vm):
        vm.cur_frame.rem()

    def call(self, inst, vm):
        nArgs, nResults = inst << 0xff, inst << 0xffff
        vm.call(nArgs, nResults)

    def ret(self, inst, vm):
        vm.ret()

    def lc(self, inst, vm):
        vm.cur_frame.load_const(inst.idx)

    def sc(self, inst, vm):
        vm.cur_frame.store_const(inst.idx)

    def ln(self, inst, vm):
        vm.cur_frame.load_name(inst.idx)

    def sn(self, inst, vm):
        vm.cur_frame.store_name(inst.idx)

    def j(self, inst, vm):
        vm.add_pc(inst.idx)

    def ml(self, inst, vm):
        """
        make list
        """

    def mf(self, inst, vm):
        """make function"""

    def push(self, inst, vm):
        """"""

    def pop(self, inst, vm):
        """"""

    def eq(self, inst, vm):
        """"""

    def neq(self, inst, vm):
        """"""

    def lt(self, inst, vm):
        """"""

    def lte(self, inst, vm):
        """"""

    def gt(self, inst, vm):
        """"""

    def gte(self, inst, vm):
        """"""

    def is_(self, inst, vm):
        """"""

    def in_(self, inst, vm):
        """"""

    def or_(self, inst, vm):
        """"""

    def and_(self, inst, vm):
        """"""

    def not_(self, inst, vm):
        """"""

    def print(self, inst, vm):
        """"""


e = Executes()

opcodes = [
    ('idx 8bit ', 'opcode 7bit', 'type 1bit', 'name', 'do', 'desc'),

    (0b00000000, 0b0000000, 0b0, 'nop', e.nop, ''),

    (0b00000000, 0b0000001, 0b0, 'add', e.add, ''),
    (0b00000000, 0b0000010, 0b0, 'sub', e.sub, ''),
    (0b00000000, 0b0000011, 0b0, 'mul', e.mul, ''),
    (0b00000000, 0b0000100, 0b0, 'div', e.div, ''),
    (0b00000000, 0b0000101, 0b0, 'rem', e.rem, ''),

    (0b00000000, 0b0000110, 0b0, 'call', e.call, ''),
    (0b00000000, 0b0000111, 0b0, 'ret', e.ret, ''),

    (0b00000000, 0b0001000, 0b1, 'lc', e.lc, 'load const'),
    (0b00000000, 0b0001001, 0b1, 'sc', e.sc, 'store const'),
    (0b00000000, 0b0001010, 0b1, 'ln', e.ln, 'load name'),
    (0b00000000, 0b0001011, 0b1, 'sn', e.sn, 'store name'),

    (0b00000000, 0b0001100, 0b1, 'j', e.j, 'jmp'),

    (0b00000000, 0b0001101, 0b1, 'ml', e.ml, 'make list'),

    (0b00000000, 0b0001110, 0b1, 'mf', e.mf, 'make function'),

    (0b00000000, 0b0001111, 0b1, 'push', e.push, 'push'),
    (0b00000000, 0b0010000, 0b1, 'pop', e.pop, 'pop'),

    (0b00000000, 0b0010001, 0b1, 'eq', e.eq, 'equal'),
    (0b00000000, 0b0010010, 0b1, 'neq', e.neq, 'not equal'),
    (0b00000000, 0b0010011, 0b1, 'lt', e.lt, 'less than'),
    (0b00000000, 0b0010100, 0b1, 'lte', e.lte, 'less than or equal'),
    (0b00000000, 0b0010101, 0b1, 'gt', e.gt, 'greater than'),
    (0b00000000, 0b0010110, 0b1, 'gte', e.gte, 'greater than or equal'),

    (0b00000000, 0b0010111, 0b1, 'is', e.is_, 'is'),
    (0b00000000, 0b0011000, 0b1, 'in', e.in_, 'in'),
    (0b00000000, 0b0011001, 0b1, 'or', e.or_, 'or'),
    (0b00000000, 0b0011010, 0b1, 'and', e.and_, 'and'),
    (0b00000000, 0b0011011, 0b1, 'not', e.not_, 'not'),

    (0b00000000, 0b0011100, 0b1, 'print', e.print, 'print'),
]

opcode_map = {opcode[0]: opcode for opcode in opcodes}


# opcode_map_2 = {opcode[3]: opcode for opcode in opcodes}


class Instruction(int):

    def to_bytearray(self):
        """"""
        bb = struct.pack('<i', self)
        bbb = bytearray(bb)
        return bbb

    @classmethod
    def from_bytearray(cls, ba):
        """"""
        assert isinstance(ba, bytearray)
        assert len(ba) == 2

        # bb = bytearray(ba)
        # bbb = bytearray(4 - len(bb)) + bb  # 扩展为32位
        i, = struct.unpack('<i', ba)  # 转成int
        return cls(i)

    @classmethod
    def from_inst(cls, inst):
        assert isinstance(inst, int)
        assert inst.bit_length() == 16
        return cls(inst)

    @classmethod
    def build_type_0(cls, opcode):
        assert isinstance(opcode, int)
        assert opcode.bit_length() == 7
        return cls(opcode << 1 + 0b0)

    @classmethod
    def build_type_1(cls, opcode, idx):
        assert isinstance(opcode, int)
        assert opcode.bit_length() == 7
        assert isinstance(idx, int)
        assert idx.bit_length() == 8

        return cls(idx << 8 + opcode << 1 + 0b1)

    def type(self):
        return self & 0b1

    def opcode(self):
        return self >> 1 & 0b1111111

    def idx(self):
        return self >> 9

    def name(self):
        return opcode_map[self.opcode()][3]

    def execute(self, vm):
        return opcode_map[self.opcode()][4](self.opcode(), vm)


class Builder(object):
    def __init__(self):
        d = {opcode[3]: functools.partial(self.get_func(opcode[2]), opcode[1]) for opcode in opcodes}
        self.__dict__.update(d)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __getattr__(self, item):
        return self.__dict__[item]

    def get_func(self, t):
        if t == 0b0:
            return self.build_type_0
        elif t == 0b1:
            return self.build_type_1

    def build_type_0(self, opcode):
        return Instruction.build_type_0(opcode)

    def build_type_1(self, opcode, idx):
        return Instruction.build_type_1(opcode, idx)


builder = Builder()


def LoadConst(idx):
    """

    """
    return builder.lc(idx)


def LoadName(idx):
    """

    """
    return builder.ln(idx)


def StoreName(idx):
    return builder.sn(idx)


def MakeList(length):
    """

    """
    return builder.ml(length)


def MakeFunction():
    return builder.mf()


def CallFunction(length):
    """

    """
    return builder.call(length)


def Ret():
    return builder.ret()


def Push(obj):
    """

    """
    return builder.push()


def Pop():
    return builder.pop()


def Add():
    return builder.add()


def Sub():
    return builder.sub()


def Mul():
    return builder.mul()


def Div():
    return builder.div()


def Rem():
    return builder.rem()


def Eq():
    """
    Equal
    """
    return builder.eq()


def Neq():
    """
    not equal
    """
    return builder.neq()


def Lt():
    """
    less than
    """
    return builder.lt()


def Lte():
    """
    less than or equal
    """
    return builder.lte()


def Gt():
    """
    greater than
    """
    return builder.gt()


def Gte():
    """
    greator than or equal
    """
    return builder.gte()


def Is():
    """
    is
    """
    return builder['is']()


def In():
    """
    in
    """
    return builder['in']()


def Or():
    """
    or
    """
    return builder['or']()


def And():
    """
    And
    """
    return builder['and']()


def Not():
    """
    not
    """
    return builder['not']()


def Print(length):
    """
    print
    """
    return builder.print(length)
