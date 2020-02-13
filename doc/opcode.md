# instruction

目前的指令长度为16bit


```
16       8       1 0
^11111111^1111111^1^
| [16:9] | [8:1] | |
```




|区间 | len | 表意 | desc |
|:---|:----|:-----|:-----|
|0   |1bit |type  | 表示是否需要idx参数
|1-8 |7bit |opcode|
|9-16|8bit |idx   |






idx 8bit |opcode 7bit|type 1bit|name|do|desc|idx type
:----|:----|:----|:----|:----|:----|:----
0b000000|0b00000|0b0|nop|vm||
0b000000|0b00001|0b0|add|vm||
0b000000|0b00010|0b0|sub|vm||
0b000000|0b00011|0b0|mul|vm||
0b000000|0b00100|0b0|div|vm||
0b000000|0b00101|0b0|rem|vm||
0b000000|0b00110|0b1|call|vm||
0b000000|0b00111|0b0|ret|vm||
0b000000|0b01000|0b1|lc|vm|load const|const
0b000000|0b01001|0b1|sc|vm|store const|const
0b000000|0b01010|0b1|ln|vm|load name|name
0b000000|0b01011|0b1|sn|vm|store name|name
0b000000|0b01100|0b0|lp|vm|load prototype|proto
0b000000|0b01101|0b1|j|vm|jmp|
0b000000|0b01110|0b1|jif|vm|jmp if false|
0b000000|0b01111|0b1|ml|vm|make list|
0b000000|0b10000|0b1|mf|vm|make function|
0b000000|0b10001|0b1|push|vm|push|
0b000000|0b10010|0b0|pop|vm|pop|
0b000000|0b10011|0b0|eq|vm|equal|
0b000000|0b10100|0b0|neq|vm|not equal|
0b000000|0b10101|0b0|lt|vm|less than|
0b000000|0b10110|0b0|lte|vm|less than or equal|
0b000000|0b10111|0b0|gt|vm|greater than|
0b000000|0b11000|0b0|gte|vm|greater than or equal|
0b000000|0b11001|0b0|is|vm|is|
0b000000|0b11010|0b0|in|vm|in|
0b000000|0b11011|0b0|or|vm|or|
0b000000|0b11100|0b0|and|vm|and|
0b000000|0b11101|0b0|not|vm|not|
0b000000|0b11110|0b1|print|vm|print|