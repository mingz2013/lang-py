# -*- coding: utf-8 -*-
"""
Module Description


定义字节码


opcode 0-7 8

idx 8-15 8

16bit



"""
import functools
import struct
from typing import Tuple, Dict, Callable

from lang import logger


class Executes(object):
    def __init__(self):
        pass

    def nop(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.nop()

    def add(self, inst: 'Instruction', vm: 'VM'):
        vm.add()

    def sub(self, inst: 'Instruction', vm: 'VM'):
        vm.sub()

    def mul(self, inst: 'Instruction', vm: 'VM'):
        vm.mul()

    def div(self, inst: 'Instruction', vm: 'VM'):
        vm.div()

    def rem(self, inst: 'Instruction', vm: 'VM'):
        vm.rem()

    def call(self, inst: 'Instruction', vm: 'VM'):
        vm.call(inst.idx)

    def ret(self, inst: 'Instruction', vm: 'VM'):
        vm.ret(inst.idx)

    def lc(self, inst: 'Instruction', vm: 'VM'):
        vm.lc(inst.idx)

    def sc(self, inst: 'Instruction', vm: 'VM'):
        vm.sc(inst.idx)

    def ln(self, inst: 'Instruction', vm: 'VM'):
        vm.ln(inst.idx)

    def sn(self, inst: 'Instruction', vm: 'VM'):
        vm.sn(inst.idx)

    def lm(self, inst: 'Instruction', vm: 'VM'):
        vm.lm(inst.idx)

    def sm(self, inst: 'Instruction', vm: 'VM'):
        vm.sm(inst.idx)

    def lmd(self, inst: 'Instruction', vm: 'VM'):
        vm.lmd(inst.idx)

    def lp(self, inst: 'Instruction', vm: 'VM'):
        vm.lp()

    def j(self, inst: 'Instruction', vm: 'VM'):
        vm.j(inst.idx)

    def jif(self, inst: 'Instruction', vm: 'VM'):
        vm.jif(inst.idx)

    def ml(self, inst: 'Instruction', vm: 'VM'):
        """
        make list
        """
        vm.ml(inst.idx)

    def mf(self, inst: 'Instruction', vm: 'VM'):
        """make function"""
        vm.mf(inst.idx)

    def push(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.push(inst.idx)

    def pop(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.pop()

    def eq(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.eq()

    def neq(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.neq()

    def lt(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.lt()

    def lte(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.lte()

    def gt(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.gt()

    def gte(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.gte()

    def is_(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.is_()

    def in_(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.in_()

    def or_(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.or_()

    def and_(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.and_()

    def not_(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.not_()

    def print(self, inst: 'Instruction', vm: 'VM'):
        """"""
        vm.print(inst.idx)


e = Executes()

opcodes = [
    # ('idx 8bit ', 'opcode 7bit', 'type 1bit', 'name', 'do', 'desc', 'idx type'),

    (0b00000000, 0b0000000, 0b0, 'nop', e.nop, '', ''),

    (0b00000000, 0b0000001, 0b0, 'add', e.add, '', ''),
    (0b00000000, 0b0000010, 0b0, 'sub', e.sub, '', ''),
    (0b00000000, 0b0000011, 0b0, 'mul', e.mul, '', ''),
    (0b00000000, 0b0000100, 0b0, 'div', e.div, '', ''),
    (0b00000000, 0b0000101, 0b0, 'rem', e.rem, '', ''),

    (0b00000000, 0b0000110, 0b1, 'call', e.call, '', ''),
    (0b00000000, 0b0000111, 0b0, 'ret', e.ret, '', ''),

    (0b00000000, 0b0001000, 0b1, 'lc', e.lc, 'load const', 'const'),
    (0b00000000, 0b0001001, 0b1, 'sc', e.sc, 'store const', 'const'),
    (0b00000000, 0b0001010, 0b1, 'ln', e.ln, 'load name', 'name'),
    (0b00000000, 0b0001011, 0b1, 'sn', e.sn, 'store name', 'name'),
    (0b00000000, 0b0001100, 0b0, 'lp', e.lp, 'load prototype', 'proto'),

    (0b00000000, 0b0001101, 0b1, 'j', e.j, 'jmp', ''),
    (0b00000000, 0b0001110, 0b1, 'jif', e.jif, 'jmp if false', ''),

    (0b00000000, 0b0001111, 0b1, 'ml', e.ml, 'make list', ''),
    (0b00000000, 0b0010000, 0b1, 'mf', e.mf, 'make function', ''),

    (0b00000000, 0b0010001, 0b1, 'push', e.push, 'push', ''),
    (0b00000000, 0b0010010, 0b0, 'pop', e.pop, 'pop', ''),

    (0b00000000, 0b0010011, 0b0, 'eq', e.eq, 'equal', ''),
    (0b00000000, 0b0010100, 0b0, 'neq', e.neq, 'not equal', ''),
    (0b00000000, 0b0010101, 0b0, 'lt', e.lt, 'less than', ''),
    (0b00000000, 0b0010110, 0b0, 'lte', e.lte, 'less than or equal', ''),
    (0b00000000, 0b0010111, 0b0, 'gt', e.gt, 'greater than', ''),
    (0b00000000, 0b0011000, 0b0, 'gte', e.gte, 'greater than or equal', ''),

    (0b00000000, 0b0011001, 0b0, 'is', e.is_, 'is', ''),
    (0b00000000, 0b0011010, 0b0, 'in', e.in_, 'in', ''),
    (0b00000000, 0b0011011, 0b0, 'or', e.or_, 'or', ''),
    (0b00000000, 0b0011100, 0b0, 'and', e.and_, 'and', ''),
    (0b00000000, 0b0011101, 0b0, 'not', e.not_, 'not', ''),

    (0b00000000, 0b0011110, 0b1, 'print', e.print, 'print', ''),

    (0b00000000, 0b0011111, 0b1, 'sm', e.sm, 'store member', 'member'),
    (0b00000000, 0b0100000, 0b1, 'lm', e.lm, 'load member', 'member'),

    (0b00000000, 0b0100001, 0b1, 'lmd', e.lmd, 'load module', 'module'),
]

opcode_map: Dict[int, Tuple[int, int, int, str, Callable, str, str]] = {opcode[1]: opcode for opcode in opcodes}


# opcode_map_2 = {opcode[3]: opcode for opcode in opcodes}


class Instruction(object):
    def __init__(self, x: int):
        # print(type(x))
        assert isinstance(x, int)
        self._data: int = x

    def __str__(self):
        return str(self.view)

    def __repr__(self):
        return repr(self.view)

    def bit_length(self) -> int:
        return self._data.bit_length()

    def to_bytearray(self) -> bytearray:
        """"""
        bb = struct.pack('<i', self._data)
        bbb = bytearray(bb)
        return bbb

    @classmethod
    def from_bytearray(cls, ba: bytearray) -> 'Instruction':
        """"""
        assert isinstance(ba, bytearray)
        assert len(ba) == 2

        # bb = bytearray(ba)
        # bbb = bytearray(4 - len(bb)) + bb  # 扩展为32位
        i, = struct.unpack('<i', ba)  # 转成int
        return cls(i)

    @classmethod
    def from_inst(cls, inst: "Instruction"):
        assert isinstance(inst, Instruction)
        assert inst.bit_length() <= 16
        return cls(inst.data)

    @classmethod
    def build_type_0(cls, opcode: int) -> "Instruction":
        # print("build_type_0<<", opcode)
        assert isinstance(opcode, int)
        assert opcode.bit_length() <= 7
        return cls((opcode << 1) + 0b0)

    @classmethod
    def build_type_1(cls, opcode: int, idx: int) -> "Instruction":
        # print("build_type_1<<", opcode, idx)
        assert isinstance(opcode, int)
        assert opcode.bit_length() <= 7
        assert isinstance(idx, int)
        assert idx.bit_length() <= 8

        return cls((idx << 8) + (opcode << 1) + 0b1)

    @property
    def type(self) -> int:
        return self._data & 0b1

    @property
    def opcode(self) -> int:
        return (self._data >> 1) & 0b1111111

    @property
    def idx(self) -> int:
        return self._data >> 8

    @property
    def name(self) -> str:
        return opcode_map[self.opcode][3]

    @property
    def view(self) -> str:
        if self.type == 0b0:
            return self.name
        elif self.type == 0b1:
            return f"{self.name} {self.idx}"

    @property
    def idx_type(self) -> str:
        return opcode_map[self.opcode][6]

    def view_2(self, vm: 'VM') -> str:
        if self.type == 0b0:
            return self.name
        elif self.type == 0b1:

            if self.name == 'lc':
                a = vm.frame.proto.load_constant(self.idx)
                return f"{self.name} {self.idx}({a})"

            elif self.name == 'sn':
                n = vm.frame.proto.get_name(self.idx)
                a = vm.frame.top()
                return f"{self.name} {self.idx}({n}) (top {a})"
            elif self.name == 'ln':
                n = vm.frame.proto.get_name(self.idx)
                a = vm.frame.closure.load_name(self.idx)
                return f"{self.name} {self.idx}({n} {a}) (top)"

            return f"{self.name} {self.idx}"

    @property
    def data(self) -> int:
        return self._data

    def fix(self, inst: 'Instruction'):
        assert isinstance(inst, Instruction)
        self._data = inst.data

    def fix_idx(self, idx: int):
        self._data = (idx << 8) + (self.opcode << 1) + self.type

    def execute(self, vm: 'VM') -> None:
        # print("Instruction.execute <<", self)
        logger.debug("<<", self.view_2(vm))
        return opcode_map[self.opcode][4](self, vm)


class Builder(object):
    def __init__(self):
        d = {
            opcode[3]: functools.partial(self.get_func(opcode[2]), opcode[1])
            for opcode in opcodes
        }
        self.__dict__.update(d)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __getattr__(self, item):
        return self.__dict__[item]

    def get_func(self, t: int) -> Callable:
        if t == 0b0:
            return self.build_type_0
        elif t == 0b1:
            return self.build_type_1
        else:
            raise Exception("error type", t)

    def build_type_0(self, opcode: int) -> Instruction:
        return Instruction.build_type_0(opcode)

    def build_type_1(self, opcode: int, idx: int) -> Instruction:
        return Instruction.build_type_1(opcode, idx)


builder: Builder = Builder()


def NOP() -> Instruction:
    """"""
    return builder.nop()


def ADD() -> Instruction:
    return builder.add()


def SUB() -> Instruction:
    return builder.sub()


def MUL() -> Instruction:
    return builder.mul()


def DIV() -> Instruction:
    return builder.div()


def REM() -> Instruction:
    return builder.rem()


def CALL(length: int) -> Instruction:
    """

    """
    return builder.call(length)


def RET() -> Instruction:
    return builder.ret()


def LC(idx: int) -> Instruction:
    """

    """
    return builder.lc(idx)


def SC(idx: int) -> Instruction:
    return builder.SC(idx)


def LN(idx: int) -> Instruction:
    """

    """
    return builder.ln(idx)


def SN(idx: int) -> Instruction:
    return builder.sn(idx)


def LM(idx: int) -> Instruction:
    return builder.lm(idx)


def SM(idx: int) -> Instruction:
    """
    store member
    """
    return builder.sm(idx)


def LP() -> Instruction:
    """
    load prototype
    """
    return builder.lp()


def LMD(idx: int) -> Instruction:
    """
    load module
    """
    return builder.lmd(idx)


def J(idx: int) -> Instruction:
    return builder.j(idx)


def JIF(idx: int) -> Instruction:
    """
    jmp is false
    """
    return builder.jif(idx)


def ML(length: int) -> Instruction:
    """

    """
    return builder.ml(length)


def MF(idx: int) -> Instruction:
    return builder.mf(idx)


def PUSH(obj: int) -> Instruction:
    """

    """
    return builder.push(obj)


def POP() -> Instruction:
    return builder.pop()


def EQ() -> Instruction:
    """
    Equal
    """
    return builder.eq()


def NEQ() -> Instruction:
    """
    not equal
    """
    return builder.neq()


def LT() -> Instruction:
    """
    less than
    """
    return builder.lt()


def LTE() -> Instruction:
    """
    less than or equal
    """
    return builder.lte()


def GT() -> Instruction:
    """
    greater than
    """
    return builder.gt()


def GTE() -> Instruction:
    """
    greater than or equal
    """
    return builder.gte()


def IS() -> Instruction:
    """
    is
    """
    return builder['is']()


def IN() -> Instruction:
    """
    in
    """
    return builder['in']()


def OR() -> Instruction:
    """
    or
    """
    return builder['or']()


def AND() -> Instruction:
    """
    And
    """
    return builder['and']()


def NOT() -> Instruction:
    """
    not
    """
    return builder['not']()


def PRINT(length: int) -> Instruction:
    """
    print
    """
    return builder.print(length)


def __print_md():
    f = lambda idx, opcode, type, name, do, desc, idx_type: \
        '{idx}|{opcode}|{type}|{name}|{do}|{desc}|{idx_type}'.format(
            idx=format(idx, '#010b'), opcode=format(opcode, '#09b'), type=bin(type), name=name, do='vm', desc=desc,
            idx_type=idx_type)

    title = '|'.join(['idx 8bit ', 'opcode 7bit', 'type 1bit', 'name', 'do', 'desc', 'idx type'])
    table = '|'.join([':----'] * 7)

    lines = [title, table]

    lines += [f(*op) for op in opcodes]

    md = '\n'.join(lines)
    print(md)


if __name__ == '__main__':
    __print_md()
