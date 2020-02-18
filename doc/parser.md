# parser

## 表达式

### 表达式列表
用于列表的中间状态，也用于函数调用的参数列表
```bnf

<表达式列表> ::= <表达式>{<逗号><表达式>}[<逗号>]

```
```bnf
<expression_list> ::= <expression>{<tk_comma><expression>}[<tk_comma>]
```


### 列表的显示

参考python的列表

```bnf

<列表显示> ::= <左中括号>[<表达式列表>]<右中括号>

```

```bnf
<list_display> ::= <tk_left_middle_bracket>[<expression_list>]<tk_right_middle_bracket>
```


### 调用
```bnf
<调用> ::= (<点号形式> | <标识符>)<左小括号>[<表达式列表>]<右小括号>
```
```bnf
<call> ::= (<period_form> | <identifier>)<tk_left_parenthesis>[<expression_list>]<tk_right_parenthesis>
```



### 原子

原子代表 一个基本单元

```bnf
<原子> ::= <标识符> 
            | <字面值> 
            | <列表显示> 
            | <圆括号形式>
            | <点号形式>
            | <self>
            | <调用>
            | <self>           

<圆括号形式> ::= <左小括号><布尔运算表达式><右小括号>
<点号形式> ::= <原子><点号><标识符>
<self> ::= <self关键字>
```

```bnf
<atom> ::= <identifier>
            | <literal>
            | <list_display>
            | <parenth_form>
            | <period_form>
            | <self>
            | <call>

<parenth_form> ::= <tk_left_parenthesis><boolean_expression><tk_right_parenthesis>
<period_form> ::= <atom><tk_period><identifier>
<self> ::= <kw_self>
```



### 一元运算符

负数，正数

```bnf
<一元运算表达式> ::= <原子> 
                    | <减号><一元运算表达式>
                    | <加号><一元运算表达式>
```
```bnf
<unary_expression> ::= <atom>
                    | <tk_minus_sign><unary_expression>
                    | <tk_plus><unary_expression>
```
### 二元运算符

乘除类，加减类

```bnf
<乘除类运算表达式> ::= <一元运算表达式> 
                    | <乘除类运算表达式><乘号><一元运算表达式> 
                    | <乘除类运算表达式><除号><一元运算表达式> 
<加减类运算表达式> ::= <乘除类运算表达式> 
                    | <加减类运算表达式><加号><乘除类运算表达式>
                    | <加减类运算表达式><减号><乘除类运算表达式>
<二元运算表达式> ::= <加减类运算表达式>
```

```bnf
<multiplicative_expression> ::= <unary_expression>
                    | <multiplicative_expression><tk_star><unary_expression>
                    | <multiplicative_expression><tk_divide><unary_expression>
<relational_expression> ::= <multiplicative_expression>
                    | <relational_expression><tk_plus><multiplicative_expression>
                    | <relational_expression><tk_minus_sign><multiplicative_expression>
<binary_operation_expression> ::= <relational_expression>
```

### 比较运算

这里参考python的比较运算, eg: a < b < c


```bnf
<比较运算表达式> ::= <二元运算表达式> {<比较运算符><二元运算表达式>}
<比较运算符> ::= <等于号>
                |<不等于号>
                |<小于号>
                |<小于等于号>
                |<大于号>
                |<大于等于号>
                |<is关键字> [<not关键字>]
                |[<not关键字>] <in关键字>
<等于号> ::= "=="
<不等于号> ::= "!="
<小于号> ::= "<"
<小于等于号> ::= "<="
<大于号> ::= ">"
<大于等于号> ::= ">="

```

```bnf
<comparison_expression> ::= <binary_operation_expression>{<comparison_expression><binary_operation_expression>}
<comparison_operator> ::= <tk_equal>
                            | <tk_not_equal>
                            | <tk_less_than>
                            | <tk_less_than_or_equal>
                            | <tk_greater_than>
                            | <tk_greater_than_or_equal>
                            | <kw_is> [<kw_not>]
                            | [<kw_not>] <kw_in> 
<tk_equal> ::= "=="
<tk_not_equal> ::= "!="
<tk_less_than> ::= "<"
<tk_less_than_or_equal> ::= "<="
<tk_greater_than> ::= ">"
<tk_greater_than_or_equal> ::= ">="
```


### 布尔运算
```bnf
<or运算表达式> ::= <and运算表达式> 
                | <or运算表达式> <or关键字> <and运算表达式>
<and运算表达式> ::= <not运算表达式> 
                | <and运算表达式> <and关键字> <not运算表达式>
<not运算表达式> ::= <比较运算表达式> 
                | <not关键字> <not运算表达式>
<布尔运算表达式> ::= <or运算表达式>
```

```bnf
<or_operation_expression> ::= <and_operation_expression>
                            | <or_operation_expression> <kw_or> <and_operation_expression>
<and_operation_expression> ::= <not_operation_expression>
                            | <and_operation_expression><kw_and><not_operation_expression>
<not_operation_expression> ::= <comparison_expression>
                            | <kw_not> <not_operation_expression>
<boolean_expression> ::= <or_operation_expression>
```

### 表达式
```bnf
<表达式> ::= <布尔运算表达式>
```
```bnf
<expression> ::= <boolean_expression>
```




### 简单语句
简单语句由一个单独的逻辑构成，多条简单语句可以存在于同一行内并以分号分割。


```bnf
<小语句> ::= <表达式语句>  
                |<return语句>
                |<break语句>
                |<continue语句>
                |<赋值语句>
                | <print语句>
<return语句> ::= <return关键字>[表达式]
<break语句> ::= <break关键字>
<continue语句> ::= <continue关键字>
<简单语句> ::= <小语句> {<分号><小语句>}[<分号>]
```

```bnf
<small_statement> ::= <expression_statement>
                    | <return_statement>
                    | <break_statement>
                    | <continue_statement>
                    | <assignment_statement>
                    | <print_statement>
<return_statement> ::= <kw_return>[expression]
<break_statement> ::= <kw_break>
<continue_statement> ::= <kw_continue>
<simple_statement> ::= <small_statement>{<tk_semicolon><small_statement>}[<tk_semicolon>]
```

#### 表达式语句
```bnf
<表达式语句> ::= <表达式>
```
```bnf
<expression_statement> ::= <expression>
```





#### 赋值语句

目前，赋值语句，只支持单个的赋值，不支持多个的同时赋值

```bnf
<赋值语句> ::= (<点号形式> | <标识符>) <赋值等号> <表达式>
```
```bnf
<assignment_statement> ::= (<period_form> | <identifier>)<tk_assign><expression>
```

#### print语句
```bnf
<print语句> ::= <print关键字><左小括号><表达式列表><右小括号>
```

```bnf
<print_statement> ::= <kw_print><tk_left_parenthesis><expression_list><tk_right_parenthesis>
```

#### import语句
```bnf
<import语句> ::= <import关键字><路径>[<as语句>] 
<from语句> ::= <from关键字><路径><import关键字><标识符>[<as语句>] 
<as语句> ::= <as关键字><标识符>
<路径> ::= <标识符>{<点号><标识符>}
```

```bnf

```

### 复合语句

```bnf
<复合语句> ::= <简单语句> |<函数定义语句> | <if分支语句> | <for循环语句>
```

```bnf
<compound_statement> ::= <simple_statement> | <function_def_statement> | <if_statement> | <for_statement>
```


#### 函数定义语句
```bnf
<函数定义语句> ::= <def关键字> <标识符> <左小括号>[<形参列表>]<右小括号><语法块>
<形参列表> ::= <标识符>{<逗号><标识符>}[<逗号>]
<语句块> ::= <左大括号>{<语句>}<右大括号> 
```

```bnf
<function_def_statement> ::= <kw_def> <identifier> <tk_left_parenthesis> [<param_list>] <tk_right_parenthesis> <statement_block>
<param_list> ::= <identifier> {<tk_comma><identifier>}[<tk_comma>]
<statement_block> ::= <tk_left_braces>{<statement>}<tk_right_braces>
```


#### if分支语句
```bnf
<if分支语句> ::= <if关键字> <表达式语句> <语句块> {<elif关键字><语句块>}[<else关键字><语句块>]
```

```bnf
<if_statement> ::= <kw_if> <expression_statement> <statement_block> {<kw_elif> <statement_block>} [<kw_else> <statement_block>]
```

#### for循环语句
```bnf
<for循环语句> ::= <for关键字> <表达式语句> <语句块>
```

```bnf
<for_statement> ::= <kw_for> <expression_statement> <statement_block>
```



### 语句

```bnf
<语句> ::= <复合语句>
```

```bnf
<statement> ::= <compound_statement>
```


## 最高层级组件

```bnf
<文件> ::= {{<新的一行>}<语句>{<新的一行>}}
```

```bnf
<file> ::= {{<tk_newline>}<statement>{<tk_newline>}}
```

