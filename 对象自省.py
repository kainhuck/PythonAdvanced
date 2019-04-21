#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自省(introspection)，在计算机编程领域里，是指在运行时来判断一个对象的类型的能力。

# 1.dir
# 他返回一个列表，列出了一个对象所拥有的属性和方法

my_list = [1, 2, 3]
print(dir(my_list))
print(dir())
# 上面的自省给了我们一个列表对象的所有方法的名字。当你没法回忆起一个方法的名字，这会非常有帮助。如果我们运行dir()而不传入参数，那么它会返回当前作用域的所有名字。

# 2.type和id
# type()函数返回一个对象的类型
# id()函数返回任意不同种类对象的唯一id

# 3.inspect模块
# inspect模块提供了许多有用的函数，来获取活跃对象的信息。比方说，你可以查看一个对象的成员，只需运行：
import inspect
print(inspect.getmembers(str))