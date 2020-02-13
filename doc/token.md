## 词法定义
源码应当为utf8字符串。

源码中所有的空格符，制表符，换行等空白部分，都当做空格符处理，只用于源码中的单词的分割，和源码的可读性。


### 关键字

```bnf
<or关键字> ::= "or"
<and关键字> ::= "and"
<not关键字> ::= "not"
<in关键字> ::= "in"
<is关键字> ::= "is"
<False关键字> ::= "False"
<True关键字> ::= "True"
<None关键字> ::= "None"
<print关键字> ::= "print"

<def关键字> ::= "def"
<return关键字> ::= "return"

<if关键字> ::= "if"
<elif关键字> ::= "elif"
<else关键字> ::= "else"


<for关键字> ::= "for"
<continue关键字> ::= "continue"
<break关键字> ::= "break"

```

```bnf
<kw_or> ::= "or"
<kw_and> ::= "and"
<kw_not> ::= "not"
<kw_in> ::= "in"
<kw_is> ::= "is"
<kw_false> ::= "False"
<kw_true> ::= "True"
<kw_none> ::= "None"
<kw_print> ::= "print"

<kw_def> ::= "def"
<kw_return> ::= "return"

<kw_if> ::= "if"
<kw_elif> ::= "elif"
<kw_else> ::= "else"

<kw_for> ::= "for"
<kw_continue> ::= "continue"
<kw_break> ::= "break"

```


### 标识符
```bnf
<标识符> ::= <非数字>{<数字>|<非数字>}
<数字> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<非数字> ::= <下划线>
            |<字母>
<下划线> ::= "_"
<字母> ::= <小写字母> 
            |<大写字母>
<小写字母> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g"
        | "h" | "i" | "j" | "k" | "l" | "m" | "n"
        | "o" | "p" | "q" | "r" | "s" | "t"
        | "u" | "v" | "w"
        | "x" | "y" | "z"

<大写字母> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G"
        | "H" | "I" | "J" | "K" | "L" | "M" | "N"
        | "O" | "P" | "Q" | "R" | "S" | "T"
        | "U" | "V" | "W"
        | "X" | "Y" | "Z"
```

```bnf
<identifier> ::= <non_numeric>{<digit>|<non_numeric>}
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<non_numeric> ::= <tk_underline>|<letter>
<tk_underline> ::= "_"
<letter> ::= <lowercase_letter>|<uppercase_letter>
<lowercase_letter> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g"
        | "h" | "i" | "j" | "k" | "l" | "m" | "n"
        | "o" | "p" | "q" | "r" | "s" | "t"
        | "u" | "v" | "w"
        | "x" | "y" | "z"
<uppercase_letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G"
        | "H" | "I" | "J" | "K" | "L" | "M" | "N"
        | "O" | "P" | "Q" | "R" | "S" | "T"
        | "U" | "V" | "W"
        | "X" | "Y" | "Z"

```


### 字面值

```bnf
<字面值> ::= <数字字面值>
            |<字符串字面值>
```

```bnf
<literal> ::= <digit_literal>|<string_literal>
```

#### 数字字面值的定义

这里的数字，只支持基本的整数和小数，常见的场景。不支持一些非常见的场景。

```bnf
<数字字面值> ::= <整数字面值>
                |<小数字面值>
<整数字面值> ::= <数字>{<数字>}
<小数字面值> ::= <整数字面值><点号><整数字面值>
<数字> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<点号> ::= "."
```
```bnf
<digit_literal> ::= <integer>|<floatnumber>
<integer> ::= <digit>{<digit>}
<floatnumber> ::= <integer><tk_period><integer>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<tk_period> ::= "."
```


#### 字符串字面值的定义

字符串的字面值，应当以双引号包括起来的字符串。


简单起见，只支持双引号的。

```bnf
<字符串字面值> ::= <双引号>{<字符串中的字符>}<双引号>
<双引号> ::= "\""
<字符串中的字符> ::= <转义字符> 
                    |"除双引号字符\",反斜线字符\\或换行符外的任何字符"
<转义字符> ::= "\'"
             |"\""
             |"\a"
             |"\b"
             |"\f"
             |"\n"
             |"\r"
             |"\t"
             |"\v"
             |"\0"
             |"\\"

```

```bnf
<string_literal> ::= <tk_double_quotation_mark>{<characters_in_string>}<tk_double_quotation_mark>
<tk_double_quotation_mark> ::= "\""
<characters_in_string> ::= <escape_character>| "除双引号字符\",反斜线字符\\或换行符外的任何字符"
<escape_character> ::= "\'"
             |"\""
             |"\a"
             |"\b"
             |"\f"
             |"\n"
             |"\r"
             |"\t"
             |"\v"
             |"\0"
             |"\\"
```


### 运算符

```bnf
<加号> ::= "+"
<减号> ::= "-"
<星号> ::= "*"
<除号> ::= "/"
<取余号> ::= "%"

<等于号> ::= "=="
<不等于号> ::= "!="
<小于号> ::= "<"
<小于等于号> ::= "<="
<大于号> ::= ">"
<大于等于号> ::= ">="
```


```bnf
<tk_plus> ::= "+"
<tk_minus_sign> ::= "-"
<tk_star> ::= "*"
<tk_divide> ::= "/"
<tk_remainder> ::= "%"

<tk_equal> ::= "=="
<tk_not_equal> ::= "!="
<tk_less_than> ::= "<"
<tk_less_than_or_equal> ::= "<="
<tk_greater_than> ::= ">"
<tk_greater_than_or_equal> ::= ">="
```

### 分隔符
```bnf
<赋值等号> ::= "="
<点号> ::= "."
<左小括号> ::= "("
<右小括号> ::= ")"
<左中括号> ::= "["
<右中括号> ::= "]"
<左大括号> ::= "{"
<右大括号> ::= "}"
<分号> ::= ";"
<逗号> ::= ","
<单引号> ::= "'"
<双引号> ::= "\""
```
```bnf
<tk_assign> ::= "="
<tk_period> ::= "."
<tk_left_parenthesis> ::= "("
<tk_right_parenthesis> ::= ")"
<tk_left_middle_bracket> ::= "["
<tk_right_middle_bracket> ::= "]"
<tk_left_braces> ::= "{"
<tk_right_braces> ::= "}"
<tk_semicolon> ::= ";"
<tk_comma> ::= ","
<tk_quotation_mark> ::= "'"
<tk_double_quotation_mark> ::= "\""
```

### 空白符

```bnf
<新的一行> ::= "\n"
```

```bnf
<tk_newline> ::= "\n"
```

