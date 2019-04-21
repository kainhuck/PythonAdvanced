#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 枚举(enumerate)是Python内置函数。它的用处很难在简单的一行中说明，但是大多数的新人，甚至一些高级程序员都没有意识到它。
# 枚举可以在打印的时候自动计数
# 举个例子
my_list = [1,2,3,4,5,6,7,8,9,0]
# for counter, value in enumerate(my_list, 1):
#     print(counter, value)

# 在举个例子
counter_list = list(enumerate(my_list, 1))
print(counter_list)