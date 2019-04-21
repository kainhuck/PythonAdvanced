#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(not)的条件判断，在Python 2.4以上才有了三元操作。

# is_fat = True
# state = "fat" if is_fat else "not fat"
# 它允许用简单的一行快速判断，而不是使用复杂的多行if语句。 这在大多数时候非常有用，而且可以使代码简单可维护。


# 配合元组使用
# 这个例子一般不会这么写
# fat = True
# fitness = ("slender", "fat")[fat]
# print(fitness)  # fat， 因为True表示1

condition = True
print(2 if condition else 1/0)  # 输出 2

# print((1/0, 2)[condition])
#输出ZeroDivisionError异常
# 元组条件表达式元组中会把两个条件都执行，而  if-else 的条件表达式不会这样。
# 最好尽量避免使用元组条件表达式。
