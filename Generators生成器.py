#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 可迭代对象
# Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法(这些双下划线方法会在其他章节中全面解释)，那么它就是一个可迭代对象。简单说，可迭代对象就是能提供迭代器的任意对象。

# 迭代器
# 任意对象，只要定义了next(Python2) 或者__next__方法，它就是一个迭代器。

# 迭代
# 用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。

# 生成器
# 生成器也是一种迭代器，但是你只能对其迭代一次。
# 这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值。

def generators_test():
    for i in range(10):
        yield i

# for i in generators_test():
#     print(i)

# 输出:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# 生成器实现斐波那契数列
def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# for x in fib(100):
#     print(x)

# next()函数
# f = fib(20)
# print(next(f))  # 输出 1
# print(next(f))  # 输出 1
# print(next(f))  # 输出 2
# print(next(f))  # 输出 3
# 注： 最后会引发异常

# iter()函数
# my_string = "helloworld"
# next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator

# 可迭代对象不等于迭代器
my_string = "helloworld"
my_iter = iter(my_string)
print(next(my_iter))