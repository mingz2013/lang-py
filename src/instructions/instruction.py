# -*- coding: utf-8 -*-
"""
@FileName: instruction
@Time: 2020/2/4 15:37
@Author: zhaojm

Module Description

"""


def new_instruction(opcode):
    """
    factory
    """
    opcode_map = {
        0x11: Nop,
    }
    return opcode_map.get(opcode)


class Instruction(object):
    """

    """

    def __init__(self, opcode):
        self.opcode = opcode  # 指令原始数据
        self.name = None  # name
        self.op_mode = None  # 操作码类型

    def fetch_operands(self):
        """
        从字节码中提取操作数
        """

    def execute(self, vm):
        """
        执行
        """


class Nop(Instruction):
    """
    Nop，
    """


class Push(Instruction):
    """
    Push
    """


class Pop(Instruction):
    """
    Pop
    """


class Add(Instruction):
    """
    Add
    """

    def execute(self, vm):
        """

        """


class Jmp(Instruction):
    """
    跳转
    """

    def execute(self, vm):
        offset = self.opcode << 0xffff
        vm.add_pc(offset)


class Call(Instruction):
    """
    call
    """

    def execute(self, vm):
        nArgs, nResults = self.opcode << 0xff, self.opcode << 0xffff
        vm.call(nArgs, nResults)


class Ret(Instruction):
    """
    return
    """

    def execute(self, vm):
        vm.ret()

