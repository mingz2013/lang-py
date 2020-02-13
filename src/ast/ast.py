# -*- coding:utf-8 -*-
"""

ast相关定义

"""
__date__ = "16/12/2017"
__author__ = "zhaojm"

from context import context
from instructions import instruction
from prototype.prototype import ProtoType
from token import token


class Node(object):
    """节点基类"""

    def __get_d(self):
        d = self.__dict__

        d['name'] = self.__class__.__name__

        return d

    def __str__(self):
        return str(self.__get_d())

    def __repr__(self):
        return repr(self.__get_d())

    def execute(self):
        """exe"""
        raise NotImplemented()

    def to_bin(self, proto):
        """
        to bin
        """
        print(self)
        raise NotImplemented()


class EndNode(Node):
    """终结符，叶子节点"""

    def __init__(self, pos, tok, lit):
        self.pos = pos
        self.tok = tok
        self.lit = lit


class StringLiteral(EndNode):
    """字符串字面值"""

    def execute(self):
        """exe"""
        return self.lit[1:-1]  # 去掉双引号

    def to_bin(self, proto):
        # print("to_bin<<", self)
        idx = proto.add_constant(self.lit[1:-1])

        inst = instruction.LC(idx)

        proto.add_code(inst)


class DigitLiteral(EndNode):
    """数字字面值"""


class Integer(DigitLiteral):
    """整数字面值"""

    def execute(self):
        """exe"""
        return int(self.lit)

    def to_bin(self, proto):
        # print("to_bin<<", self)
        idx = proto.add_constant(int(self.lit))
        inst = instruction.LC(idx)

        proto.add_code(inst)


class FloatNumber(DigitLiteral):
    """小数字面值"""

    def execute(self):
        """exe"""
        return float(self.lit)

    def to_bin(self, proto):
        # print("to_bin<<", self)
        idx = proto.add_constant(float(self.lit))
        inst = instruction.LC(idx)

        proto.add_code(inst)


class Identifier(EndNode):
    """标识符"""

    def execute(self):
        """execute"""
        # return self.expression.execute()
        # 从环境变量，符号表管理里面，获取当前标识符所对应的值
        return context.Symtab.get_var(self.lit).init_data

    def to_bin(self, proto):
        # print("to_bin<<", self)
        idx = self.get_idx(proto)

        inst = instruction.LN(idx)

        proto.add_code(inst)

        return idx

    def get_idx(self, proto):
        idx = proto.add_name(self.lit)
        return idx


class Atom(Node):
    """原子"""


class ExpressionList(Atom):
    """表达式列表"""

    def __init__(self):
        self.expression_list = []

    def __len__(self):
        return len(self.expression_list)

    def append_expression(self, expression):
        """execute"""
        self.expression_list.append(expression)

    def execute(self):
        """execute"""
        return [expression.execute() for expression in self.expression_list]

    def to_bin(self, proto):
        # print("to_bin<<", self)
        return [expression.to_bin(proto) for expression in self.expression_list]


class ListDisplay(Atom):
    """列表显示"""

    def __init__(self, expression_list):
        self.expression_list = expression_list

    def execute(self):
        """exe"""
        return self.expression_list.execute()

    def to_bin(self, proto):
        """

        """
        # print("to_bin<<", self)
        self.expression_list.to_bin(proto)

        length = len(self.expression_list)

        inst = instruction.ML(length)

        proto.add_code(inst)


class ParenthForm(Atom):
    """
    圆括号形式
    """

    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        """exe"""
        return self.expression.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        return self.expression.to_bin(proto)


class Call(Atom):
    """调用"""

    def __init__(self, identifier, expression_list):
        self.identifier = identifier
        self.expression_list = expression_list

    def execute(self):
        """exe"""
        func = self.identifier.execute()
        return func(self.expression_list.execute())

    def to_bin(self, proto):
        if self.expression_list:
            self.expression_list.to_bin(proto)

        self.identifier.to_bin(proto)  # 加载了原型idx

        inst = instruction.LP()  # 加载原型到栈顶
        proto.add_code(inst)
        idx = len(self.expression_list) if self.expression_list else 0
        inst = instruction.CALL(idx)
        proto.add_code(inst)


class Expression(Node):
    """表达式"""


class UnaryExpression(Expression):
    """一元运算符"""

    def __init__(self, tok, expression):
        self.tok = tok
        self.expression = expression

    def execute(self):
        """exe"""
        if self.tok == token.tk_plus:
            return self.expression.execute()
        elif self.tok == token.tk_minus_sign:
            return -self.expression.execute()
        else:
            raise Exception('UnaryExpression >> error tok', self.tok)
            # return None

    def to_bin(self, proto):
        """

        """
        # print("to_bin<<", self)
        proto.add_code(instruction.PUSH(0))
        self.expression.to_bin(proto)

        if self.tok == token.tk_plus:
            proto.add_code(instruction.ADD())
        elif self.tok == token.tk_minus_sign:
            proto.add_code(instruction.SUB())


class NegativeExpression(UnaryExpression):
    """负数"""


class PositiveExpression(UnaryExpression):
    """正数"""


class BinaryOperationExpression(Expression):
    """二元运算符"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self):
        """exe"""
        raise NotImplemented()


class RelationalExpression(BinaryOperationExpression):
    """加减类运算表达式"""


class MultiplicativeExpression(BinaryOperationExpression):
    """乘除类运算表达式"""


class PlusExpression(BinaryOperationExpression):
    """add"""

    def execute(self):
        """exe"""
        return self.left.execute() + self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)

        proto.add_code(instruction.ADD())


class MinusSignExpression(RelationalExpression):
    """sub"""

    def execute(self):
        """exe"""
        return self.left.execute() - self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.SUB())


class StarExpression(RelationalExpression):
    """mul"""

    def execute(self):
        """exe"""
        return self.left.execute() * self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.MUL())


class DivideExpression(MultiplicativeExpression):
    """div"""

    def execute(self):
        """exe"""
        return self.left.execute() / self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.DIV())


class RemainderExpression(BinaryOperationExpression):
    """求余"""

    def execute(self):
        """exe"""
        return self.left.execute() % self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.REM())


class ComparisonExpression(BinaryOperationExpression):
    """比较运算表达式"""


class EqualExpression(ComparisonExpression):
    """等于"""

    def execute(self):
        """exe"""
        return self.left.execute() == self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.EQ())


class NotEqualExpression(ComparisonExpression):
    """不等于"""

    def execute(self):
        """exe"""
        return self.left.execute() != self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.NEQ())


class LessThanExpression(ComparisonExpression):
    """小于"""

    def execute(self):
        """exe"""
        return self.left.execute() < self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.LT())


class LessThanOrEqualExpression(ComparisonExpression):
    """小于等于"""

    def execute(self):
        """exe"""
        return self.left.execute() <= self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.LTE())


class GreaterThanExpression(ComparisonExpression):
    """大于"""

    def execute(self):
        """exe"""
        return self.left.execute() > self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.GT())


class GreaterThanOrEqualExpression(ComparisonExpression):
    """大于等于"""

    def execute(self):
        """exe"""
        return self.left.execute() >= self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.GTE())


class IsExpression(ComparisonExpression):
    """is表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() is self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.IS())


class InExpression(ComparisonExpression):
    """in表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() in self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.IN())


class BooleanExpression(BinaryOperationExpression):
    """布尔运算表达式"""


class OrExpression(BooleanExpression):
    """or运算表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() or self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.OR())


class AndExpression(BooleanExpression):
    """and运算表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() and self.right.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.AND())


class NotExpression(Expression):
    """not运算表达式"""

    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        """exe"""
        return not self.expression.execute()

    def to_bin(self, proto):
        """"""
        # print("to_bin<<", self)
        self.expression.to_bin(proto)
        proto.add_code(instruction.NOT())


class Statement(Node):
    """语句"""


class SimpleStatement(Statement):
    """简单语句"""

    def __init__(self):
        self.small_statements = []

    def append_small_statement(self, node):
        """
        append_small_statement
        :param node:
        :return:
        """
        self.small_statements.append(node)

    def execute(self):
        """exe"""
        result = None
        for statement in self.small_statements:
            result = statement.execute()

        return result

    def to_bin(self, proto):
        # print("to_bin<<", self)
        for s in self.small_statements:
            s.to_bin(proto)


class SmallStatement(Statement):
    """SmallStatement"""


class ReturnStatement(SmallStatement):
    """return"""

    def __init__(self, expression=None):
        self.expression = expression

    def execute(self):
        """exe"""
        raise NotImplemented()

    def to_bin(self, proto):
        if self.expression:
            self.expression.to_bin(proto)
        else:
            proto.add_code(instruction.PUSH(None))
        proto.add_code(instruction.RET())


class PrintStatement(SimpleStatement):
    """print"""

    def __init__(self, expression_list):
        self.expression_list = expression_list

    def execute(self):
        """exe"""
        print("PrintStatement.execute print >>>", self.expression_list.execute())
        return None

    def to_bin(self, proto):
        # print("to_bin<<", self)
        self.expression_list.to_bin(proto)
        proto.add_code(instruction.PRINT(len(self.expression_list)))


class AssignmentStatement(SimpleStatement):
    """赋值语句"""

    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def execute(self):
        """execute"""
        context.Symtab.add_var(self.identifier.lit, self.expression.execute())
        return None

    def to_bin(self, proto):
        """

        """
        # print("to_bin<<", self)
        self.expression.to_bin(proto)

        idx = self.identifier.get_idx(proto)

        proto.add_code(instruction.SN(idx))


class ExpressionStatement(SimpleStatement):
    """表达式语句"""


class CompoundStatement(Statement):
    """复合语句"""


class DefStatement(Statement):
    """
    定义语句，函数定义
    """

    def __init__(self, identifier, param_list, block):
        self.identifier = identifier
        self.param_list = param_list
        self.block = block

    def execute(self):
        """
        exe
        """
        # context.Symtab.add_var(self.ident.lit, )
        return None

    def to_bin(self, proto):
        # print("to_bin<<", self)
        p = ProtoType()
        p.name = self.identifier.lit
        p.proto = proto
        if self.param_list:
            self.param_list.to_bin(p)

        self.block.to_bin(p)

        if p.code_len == 0 or p.get_code(p.code_len - 1) != instruction.RET().opcode:
            p.add_code(instruction.RET())

        idx = proto.add_sub_proto(p)

        proto.add_code(instruction.PUSH(idx))
        # proto.add_code(instruction.MF(idx))

        idx = proto.add_name(p.name)
        proto.add_code(instruction.SN(idx))


class ParamList(Node):
    """
    参数列表
    """

    def __init__(self):
        self.params = []

    def append_identifier(self, identifier):
        self.params.append(identifier)

    def execute(self):
        """"""

    def to_bin(self, proto):
        """"""
        print("to_bin<<", self)
        for i in self.params:
            idx = i.get_idx(proto)
            # proto.add_code(instruction.SN(idx))

class StatementBlock(Node):
    def __init__(self):
        self.statements = []

    def append_statement(self, node):
        self.statements.append(node)

    def execute(self):
        ret = None
        for s in self.statements:
            ret = s.execute()
        return ret

    def to_bin(self, proto):
        # print("to_bin<<", self)
        for s in self.statements:
            s.to_bin(proto)


class ForStatement(Statement):
    """
    for 循环语句
    """

    def __init__(self, expression, block):
        self.expression = expression
        self.block = block

    def execute(self):
        ret = None
        while self.expression.execute():
            ret = self.block.execute()
        return ret

    def to_bin(self, proto):
        """"""
        print("to_bin<<", self)

        # 当前的pc
        begin = proto.code_len

        # 解析条件语句
        self.expression.to_bin(proto)

        # 生成跳转语句， 如果False就跳转
        jmp_to_end = instruction.JIF(0)
        pc = proto.add_code(jmp_to_end)

        # 解析块
        self.block.to_bin(proto)

        # 跳转回begin
        jmp_to_begin = instruction.J(begin - proto.code_len)
        proto.add_code(jmp_to_begin)

        # 修复跳转到结束的指令
        jmp_to_end.fix(instruction.JIF(proto.code_len - pc))


class IfStatement(Statement):
    """
    if 分支语句
    """

    def __init__(self):
        self.elifs = []

        self.else_block = None

    def append_elif(self, expression, block):
        self.elifs.append({
            'expression': expression,
            'block': block
        })

    def set_else_block(self, else_block):
        self.else_block = else_block

    def execute(self):
        for elif_obj in self.elifs:
            if elif_obj['expression'].execute():
                return elif_obj['block'].execute()
        return self.else_block.execute()

    def to_bin(self, proto):
        """

        """
        print("to_bin<<", self)

        jmp_to_end_s = []

        for elif_obj in self.elifs:
            # 解析表达式
            elif_obj['expression'].to_bin(proto)

            # 如果False，跳转到下一个表达式判断

            jmp_to_next = instruction.JIF(0)
            pc = proto.add_code(jmp_to_next)

            # 解析块语句
            elif_obj['block'].to_bin(proto)

            # 跳转到结束
            jmp_to_end = instruction.J(0)
            cur_pc = proto.add_code(jmp_to_end)
            jmp_to_end_s.append((jmp_to_end, cur_pc))

            # 修复跳转到下一条语句
            jmp_to_next.fix(instruction.JIF(proto.code_len - pc))

        # 解析else块语句
        self.else_block.to_bin(proto)

        # 修复所有的跳转到结束的语句
        for jmp_to_end in jmp_to_end_s:
            jmp_to_end[0].fix(instruction.J(proto.code_len - jmp_to_end[1]))


class File(Node):
    """root"""

    def __init__(self):
        self.statements = []  # 语句集合

    def append_statements(self, statement):
        """append statements"""
        self.statements.append(statement)

    def execute(self):
        """execute"""
        context.Symtab.enter()  # 进入0级作用域
        result = None
        for statement in self.statements:
            result = statement.execute()

        context.Symtab.leave()  # 离开0级作用域

        return result

    def to_bin(self, proto):
        # print("to_bin<<", self)
        for s in self.statements:
            s.to_bin(proto)


if __name__ == '__main__':
    f = File()
    # print(str(f.__dict__))
    print(f)
