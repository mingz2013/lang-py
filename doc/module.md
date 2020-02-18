# module设计

每一个module，就是一个prototype。默认在代码的最外层包裹一个prototype

import module, 就是引入了prototype。此时，应当将prototype生成closure对象，存储到env。


import语句，负责的是，
- env中能否找到对应的module实例化的closure？
    - 否，将module中的prototype实例化成closure，并存储到env。
- 将closure赋值给var内的变量。

- 使用name，就是从var中读取closure。



closure对象中，
- var里面，在每次函数执行的时候，都会由代码进行初始化。
- member里面，在对象模式中，当做对象的属性存在。

- 所以，module中的member是全局的对象，因为全局存储到env中。




也可以用闭包的形式，实现全局变量。




