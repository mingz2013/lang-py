# -*- coding:utf-8 -*-
"""
语法分析，生成抽象语法树
"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

from ast import ast
from scanner.scanner import Scanner
from token import token


class Parser(object):
    """
    Parser
    """

    def __init__(self, filename, src):
        self.file = token.File(filename)

        self.scanner = Scanner(self.file, src)

        # self.pos = None
        # self.tok = None
        # self.lit = None
        self.token = None
        self.line_num = 0
        self.next_token()

    @property
    def pos(self):
        return self.token.pos

    @property
    def tok(self):
        return self.token.tok

    @property
    def lit(self):
        return self.token.lit

    def skip_newlines(self):
        while self.tok == token.tk_newline:
            self.skip(token.tk_newline)
            self.line_num += 1

    def skip(self, tok):
        """跳过"""
        print("parser.skip....", tok)
        if self.tok == tok:
            self.next_token()
        else:
            self.error("parser.skip  bad skip...", self.tok, tok)  # 非预期

    def next_token(self):
        """获取下一个token"""
        print("next_token...")
        self.token = self.scanner.scan()
        # self.pos, self.tok, self.lit = self.scanner.scan()
        print('parser.next_token--------------------', self.pos, self.tok, self.lit)
        # if self.tok == token.EOF:
        #     pass
        # else:
        #
        #     # self.next_token()
        #     pass

    def error(self, *args):
        """error"""
        print("Parser.error >>", self.pos, ", ", self.tok, ", ", self.lit, ",", *args)
        exit(1)

    def parse_file(self):
        """parse_file"""
        print('parse_file.....')

        file_node = ast.File()

        self.skip_newlines()

        while self.tok != token.EOF:
            node = self.statement()
            file_node.append_statements(node)
            # self.next_token()
            self.skip_newlines()

        if self.tok != token.EOF:
            self.error("parse_file >> bad end...")  # 解析完一个完整的表达式后，没有结束

        print("File... >>", file_node)

        return file_node

    def statement(self):
        """语句"""
        print("statement...")
        node = self.compound_statement()
        # print("statement...>>", node)
        return node

    def compound_statement(self):
        """复合语句"""
        print("compound_statement...")

        self.skip_newlines()

        if self.tok == token.kw_def:
            node = self.function_def_statement()
        elif self.tok == token.kw_if:
            node = self.if_statement()
        elif self.tok == token.kw_for:
            node = self.for_statement()
        else:
            node = self.simple_statement()

        self.skip_newlines()

        # print("compound_statement...>>", node)

        return node

    def function_def_statement(self):
        """
        function_def_statement
        """
        print("function_def_statement....", self.tok, self.lit)
        self.skip(token.kw_def)

        # ident = self.tok
        ident = ast.Identifier(self.pos, self.tok, self.lit)

        self.next_token()

        self.skip(token.tk_left_parenthesis)

        # if self.tok == token.tk_right_parenthesis:
        #     param_list = None
        # else:
        param_list = self.param_list()
        # self.next_token()

        self.skip(token.tk_right_parenthesis)

        block = self.statement_block()

        node = ast.DefStatement(ident, param_list, block)

        print("function_def_statement....>>", node)
        return node

    def param_list(self):
        """
        param list, 函数形参列表
        """
        print("param_list....", self.tok, self.lit)
        node = ast.ParamList()

        if self.tok == token.tk_identifier:
            node.append_identifier(ast.Identifier(self.pos, self.tok, self.lit))
            self.next_token()
            while self.tok == token.tk_comma:
                self.skip(token.tk_comma)

                if self.tok == token.tk_identifier:
                    node.append_identifier(ast.Identifier(self.pos, self.tok, self.lit))
                    self.next_token()
                else:
                    break
                    # self.error("param error")
        else:
            pass
        print("param_list...>", node)
        return node

    def statement_block(self):
        """
        语句块
        """
        print("statement_block....", self.tok, self.lit)

        self.skip(token.tk_left_braces)

        self.skip_newlines()

        node = ast.StatementBlock()

        while self.tok != token.tk_right_braces:
            node1 = self.statement()
            node.append_statement(node1)

        self.skip(token.tk_right_braces)

        return node

    def for_statement(self):
        """

        :return:
        """
        print("for_statement....", self.tok, self.lit)

        self.skip(token.kw_for)

        expression = self.expression_statement()
        block = self.statement_block()
        node = ast.ForStatement(expression, block)
        return node

    def if_statement(self):
        """

        :return:
        """
        print("if_statement....", self.tok, self.lit)
        self.skip(token.kw_if)

        node = ast.IfStatement()
        expression = self.expression_statement()
        block = self.statement_block()

        node.append_elif(expression, block)

        while self.tok == token.kw_elif:
            self.skip(token.kw_elif)
            expression = self.expression_statement()
            block = self.statement_block()
            node.append_elif(expression, block)

        if self.tok == token.kw_else:
            self.skip(token.kw_else)
            block = self.statement_block()
            node.set_else_block(block)

        return node

    def simple_statement(self):
        """
        简单语句
        :return:
        """
        print("simple_statement...")

        node = ast.SimpleStatement()

        node1 = self.small_statement()
        node.append_small_statement(node1)
        # self.next_token()

        while self.tok == token.tk_semicolon:

            self.skip(token.tk_semicolon)

            if self.tok == token.EOF:
                break

            if self.tok == token.tk_newline:
                break

            node1 = self.small_statement()
            node.append_small_statement(node1)

        print("simple_statement...>>", node)
        return node

    def small_statement(self):
        """
        小语句
        :return:
        """
        print("small_statement...")

        if self.tok == token.kw_print:
            node = self.print_statement()
        elif self.tok == token.kw_import:
            node = self.import_statement()
        elif self.tok == token.kw_return:
            node = self.return_statement()

        elif self.tok == token.kw_break:

            node = self.break_statement()

        elif self.tok == token.kw_continue:
            node = self.continue_statement()
        else:

            node = self.expression_statement()

            if isinstance(node, ast.Identifier) or isinstance(node, ast.PeriodForm):

                if self.tok == token.tk_assign:
                    self.skip(token.tk_assign)
                    node2 = self.expression_statement()
                    node = ast.AssignmentStatement(node, node2)

        print("small_statement...>>", node)
        return node

    def import_statement(self):
        """
        import
        """
        print("import statement...")
        self.skip(token.kw_import)
        node = self.path_statement()
        if self.tok == token.kw_as:
            self.skip(token.kw_as)
            if self.tok == token.tk_identifier:
                identifier = ast.Identifier(self.pos, self.tok, self.lit)
            else:
                self.error("as error")
                return
        else:
            identifier = None
        print("import statement ....>>")
        return ast.ImportStatement(node, identifier)

    def path_statement(self):
        print("path statement....")
        identifier_list = []
        identifier = ast.Identifier(self.pos, self.tok, self.lit)
        identifier_list.append(identifier)
        self.next_token()

        while self.tok == token.tk_period:
            self.skip(token.tk_period)
            if self.tok == token.tk_identifier:
                identifier = ast.Identifier(self.pos, self.tok, self.lit)
                identifier_list.append(identifier)
                self.next_token()
            else:
                self.error("path statement...")
        print("path statement....>>")
        return ast.PathStatement(identifier_list)

    def return_statement(self):
        """

        :return:
        """
        self.skip(token.kw_return)
        if self.tok == token.tk_semicolon or self.tok == token.tk_newline:
            node = None
        else:
            node = self.expression()
        node = ast.ReturnStatement(node)
        return node

    def continue_statement(self):
        """

        :return:
        """
        node = ast.ContinueStatement()
        self.skip(token.kw_continue)
        return node

    def break_statement(self):
        """

        :return:
        """
        node = ast.BreakStatement()
        self.skip(token.kw_break)
        return node

    def print_statement(self):
        """print"""
        self.skip(token.kw_print)
        self.skip(token.tk_left_parenthesis)
        node = self.expression_list()
        self.skip(token.tk_right_parenthesis)

        return ast.PrintStatement(node)

    def expression_list(self):
        """表达式列表"""
        node = ast.ExpressionList()

        node1 = self.expression_statement()
        node.append_expression(node1)

        while self.tok == token.tk_comma:
            self.skip(token.tk_comma)

            node1 = self.expression_statement()
            node.append_expression(node1)

        return node

    def expression_statement(self):
        """
        表达式语句
        :return:
        """
        print("expression_statement...")
        node = self.expression()
        print("expression_statement...>>", node)
        return node

    def expression(self):
        """
        表达式
        :return:
        """
        return self.boolean_expression()

    def boolean_expression(self):
        """
        布尔表达式
        :return:
        """
        return self.or_operation_expression()

    def or_operation_expression(self):
        """
        or操作表达式
        :return:
        """
        node = self.and_operation_expresion()

        # self.next_token()

        while self.tok == token.kw_or:
            self.skip(token.kw_or)
            node2 = self.and_operation_expresion()
            node = ast.OrExpression(node, node2)

        return node

    def and_operation_expresion(self):
        """
        and操作表达式
        :return:
        """
        node = self.not_operation_expression()

        while self.tok == token.kw_and:
            self.skip(token.kw_and)
            node2 = self.not_operation_expression()
            node = ast.AndExpression(node, node2)

        return node

    def not_operation_expression(self):
        """
        not操作表达式
        :return:
        """
        if self.tok == token.kw_not:
            self.skip(token.kw_not)
            node2 = self.not_operation_expression()
            node = ast.NotExpression(node2)
        else:
            node = self.comparison_expression()
        #
        # node = self.comparison_expression()
        # while self.tok == token.kw_not:
        #     self.skip(token.kw_not)
        #     node2 = self.not_operation_expression()
        #     node = ast.NotExpression(node2)

        return node

    def comparison_expression(self):
        """
        比较运算表达式
        :return:
        """
        print("comparison_expression...")
        node = self.binary_operation_expression()

        while self.tok in (
                token.tk_equal,
                token.tk_not_equal,
                token.tk_less_than,
                token.tk_less_than_or_equal,
                token.tk_greater_than,
                token.tk_greater_than_or_equal,
                token.kw_is,
                token.kw_in,):
            tok2 = self.tok
            self.skip(tok2)
            print('tok2', tok2)
            node2 = self.binary_operation_expression()
            print('tok2', tok2)
            if tok2 == token.tk_equal:
                node = ast.EqualExpression(node, node2)
            elif tok2 == token.tk_not_equal:
                node = ast.NotEqualExpression(node, node2)
            elif tok2 == token.tk_less_than:
                node = ast.LessThanExpression(node, node2)
            elif tok2 == token.tk_less_than_or_equal:
                node = ast.LessThanOrEqualExpression(node, node2)
            elif tok2 == token.tk_greater_than:
                node = ast.GreaterThanExpression(node, node2)
            elif tok2 == token.tk_greater_than_or_equal:
                node = ast.GreaterThanOrEqualExpression(node, node2)
            elif tok2 == token.kw_is:
                node = ast.IsExpression(node, node2)
            elif tok2 == token.kw_in:
                node = ast.InExpression(node, node2)
            else:
                self.error("comparison_expression unexcept tok", tok2)

        print("comparison_expression...>>", node)
        return node

    def binary_operation_expression(self):
        """
        二元操作运算符
        :return:
        """
        print("binary_operation_expression...")
        node = self.relational_expression()
        print("binary_operation_expression...>>", node)
        return node

    def relational_expression(self):
        """加减类表达式"""
        print("relational_expression....")
        node = self.multiplicative_expression()

        while self.tok == token.tk_plus or self.tok == token.tk_minus_sign:

            tok1 = self.tok

            self.skip(tok1)
            node2 = self.multiplicative_expression()

            if tok1 == token.tk_plus:
                node = ast.PlusExpression(node, node2)
            elif tok1 == token.tk_minus_sign:
                node = ast.MinusSignExpression(node, node2)
            else:
                Exception("")

        print("relational_expression...>", node)
        return node

    def multiplicative_expression(self):
        """乘除类表达式"""
        print("multiplicative_expression....")
        node = self.unary_expression()

        while self.tok == token.tk_divide or self.tok == token.tk_star:
            tok1 = self.tok

            self.next_token()
            node2 = self.unary_expression()

            if tok1 == token.tk_divide:
                node = ast.DivideExpression(node, node2)
            elif tok1 == token.tk_star:
                node = ast.StarExpression(node, node2)
            else:
                Exception("multiplicative_expression unexcept tok1 ", tok1)

        print("multiplicative_expression...>", node)
        return node

    def unary_expression(self):
        """一元表达式"""
        print("unary_expression....")

        # node = self.atom()
        if self.tok == token.tk_plus or self.tok == token.tk_minus_sign:  # + -

            tok1 = self.tok

            self.next_token()
            node = self.unary_expression()
            node = ast.UnaryExpression(tok1, node)

        else:
            node = self.atom()

        print("unary_expression...>", node)
        return node

    def atom(self):
        """原子"""
        print("atom....", self.tok, self.lit)

        if self.tok == token.tk_left_parenthesis:  # (
            self.skip(token.tk_left_parenthesis)
            node = self.boolean_expression()
            node = ast.ParenthForm(node)
            self.skip(token.tk_right_parenthesis)

        elif self.tok == token.tk_left_middle_bracket:  # [
            self.skip(token.tk_left_middle_bracket)
            node = self.expression_list()
            node = ast.ListDisplay(node)
            self.skip(token.tk_right_middle_bracket)

        elif self.tok == token.tk_identifier:  #
            node = ast.Identifier(self.pos, self.tok, self.lit)
            self.next_token()

        elif self.tok == token.kw_self:  # self
            node = ast.Self()
            self.skip(token.kw_self)

        elif self.tok == token.tk_string:
            node = ast.StringLiteral(self.pos, self.tok, self.lit)
            self.next_token()

        elif self.tok == token.tk_floatnumber:
            node = ast.FloatNumber(self.pos, self.tok, self.lit)
            self.next_token()

        elif self.tok == token.tk_integer:
            node = ast.Integer(self.pos, self.tok, self.lit)
            self.next_token()

        else:
            node = None
            self.error('atom unexcept >>', self.pos, self.tok, self.lit, node)

        while self.tok == token.tk_left_parenthesis \
                or self.tok == token.tk_period:

            if self.tok == token.tk_left_parenthesis:
                self.skip(token.tk_left_parenthesis)
                if self.tok == token.tk_right_parenthesis:
                    node2 = None
                else:
                    node2 = self.expression_list()
                node = ast.Call(node, node2)
                self.skip(token.tk_right_parenthesis)

            elif self.tok == token.tk_period:

                self.skip(token.tk_period)
                if self.tok == token.tk_identifier:
                    node = ast.PeriodForm(node, ast.Identifier(self.pos, self.tok, self.lit))
                    self.next_token()
                else:
                    node = None
                    self.error('atom unexcept parse periodform >>', self.pos, self.tok, self.lit, node)

            else:
                self.error("atom unexcept, in while....>>")

        return node


if __name__ == '__main__':
    import codecs

    filename = '1.script'
    with codecs.open(filename, encoding='utf-8') as f:
        ast = Parser(filename, f.read()).parse_file()
        print('ast-->>>', ast)
        print('ast.execute-->>', ast.execute())
