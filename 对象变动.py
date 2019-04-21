#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python中可变(mutable)与不可变(immutable)的数据类型让新手很是头痛。简单的说，可变(mutable)意味着"可以被改动"，而不可变(immutable)的意思是“常量(constant)”。想把脑筋转动起来吗？考虑下这个例子：

# foo = ['hi']
# print(foo)
# # Output: ['hi']
#
# bar = foo
# bar += ['bye']
# print(foo)
# # Output: ['hi', 'bye']

# 刚刚发生了什么？我们预期的不是那样！
# 这不是一个bug。这是对象可变性(mutability)在作怪。每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。

# def add_to(num, target=[]):
#     target.append(num)
#     print(target)
#
# add_to(1)   # [1]
# add_to(2)   # [1, 2]
# add_to(3)   # [1, 2, 3]

# 这次又没有达到预期，是列表的可变性在作怪。在Python中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。你应该永远不要定义可变类型的默认参数，除非你知道你正在做什么。你应该像这样做：

def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target