# instruction

目前的指令长度为16bit


```
16       8       1 0
^11111111^1111111^1^
| [16:9] | [8:1] | |
```




|interval | len | name | desc |
|:--------|:----|:-----|:-----|
|[0, 1)   |1bit |type  | 表示是否需要idx参数
|[1, 8)   |7bit |opcode|
|[8, 15)  |8bit |idx   |






idx 8bit |opcode 7bit|type 1bit|name|do|desc|idx type
:----|:----|:----|:----|:----|:----|:----
0b00000000|0b0000000|0b0|nop|vm||
0b00000000|0b0000001|0b0|add|vm||
0b00000000|0b0000010|0b0|sub|vm||
0b00000000|0b0000011|0b0|mul|vm||
0b00000000|0b0000100|0b0|div|vm||
0b00000000|0b0000101|0b0|rem|vm||
0b00000000|0b0000110|0b1|call|vm||
0b00000000|0b0000111|0b0|ret|vm||
0b00000000|0b0001000|0b1|lc|vm|load const|const
0b00000000|0b0001001|0b1|sc|vm|store const|const
0b00000000|0b0001010|0b1|ln|vm|load name|name
0b00000000|0b0001011|0b1|sn|vm|store name|name
0b00000000|0b0001100|0b0|lp|vm|load prototype|proto
0b00000000|0b0001101|0b1|j|vm|jmp|
0b00000000|0b0001110|0b1|jif|vm|jmp if false|
0b00000000|0b0001111|0b1|ml|vm|make list|
0b00000000|0b0010000|0b1|mf|vm|make function|
0b00000000|0b0010001|0b1|push|vm|push|
0b00000000|0b0010010|0b0|pop|vm|pop|
0b00000000|0b0010011|0b0|eq|vm|equal|
0b00000000|0b0010100|0b0|neq|vm|not equal|
0b00000000|0b0010101|0b0|lt|vm|less than|
0b00000000|0b0010110|0b0|lte|vm|less than or equal|
0b00000000|0b0010111|0b0|gt|vm|greater than|
0b00000000|0b0011000|0b0|gte|vm|greater than or equal|
0b00000000|0b0011001|0b0|is|vm|is|
0b00000000|0b0011010|0b0|in|vm|in|
0b00000000|0b0011011|0b0|or|vm|or|
0b00000000|0b0011100|0b0|and|vm|and|
0b00000000|0b0011101|0b0|not|vm|not|
0b00000000|0b0011110|0b1|print|vm|print|