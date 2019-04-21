#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 推导式（又称解析式）是Python的一种独有特性

# 1.列表推导式
#列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。
#它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是0个或多个for或者if语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以if和for语句为上下文的表达式运行完成之后产生

# 规范
# variable = [out_exp for out_exp in input_list if out_exp == 2]

# multiples = [i for i in range(30) if i % 3 is 0]
# print(multiples)
#
# # 普通表达式
# squared = []
# for x in range(10):
#     squared.append(x**2)
#
# # 使用列表推导式
# squared = [x**2 for x in range(10)]

# 2.字典推导式
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase_frequency = {
#     k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
#     for k in mcase.keys()
# }
# print(mcase_frequency)
# # get()方法第二个参数是找不到值时的默认参数
#
# # 快速对换一个字典的键和值
# ncase = {v:k for k,v in mcase.items()}
# print(ncase)

# 3.集合推导式
# 类似以列表的推导式区别在于集合使用{}
squared = {x**2 for x in range(10)}
print(squared)