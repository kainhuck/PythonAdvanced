#!/usr/bin/env python
# -*- coding: utf-8 -*-

# map
# Map会将一个函数映射到一个输入列表的所有元素上。
# 这是它的规范：
# map(function_to_apply, list_of_inputs)

# 普通用法
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)

# 使用map的高级用法
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))

# 例2：
# def multiply(x):
#     return (x * x)
#
# def add(x):
#     return (x + x)
#
# funcs = [multiply, add]
# for i in range(5):
#     value = map(lambda x: x(i), funcs)
#     print(list(value))
#     # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
#     #        在python2中map直接返回列表，但在python3中返回迭代器
#     #        因此为了兼容python3, 需要list转换一下

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]


# Filter
# 顾名思义，filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True.

# 从列表里筛选出所有的负数：
# num_list = [-1, -3, 45, 0, 8, -22]
# less_than_zero = map(lambda x: x<0, num_list)
# print(list(less_than_zero))
# 输出：
# [-1, -3, -22]


# Reduce
# 当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数。

# 举个例子，当你需要计算一个整数列表的乘积时。
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)  # 24















