#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 装饰器(Decorators)是Python的一个重要部分。简单地说：他们是修改其他函数的功能的函数。他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。

# 一.先来了解一下Python中的函数
# def fun():
#     return "hello world"
#
# print(fun())
#
# # 可以将函数赋值给一个变量
# another_fun = fun
# print(another_fun())
#
# # 删掉原来的函数，不会影响新的函数
# del fun
# print(another_fun())

# 二.在函数中定义函数
# def fun1():
#     print("在fun1函数中")
#     def fun2():
#         return "在fun1函数中的fun2函数中"
#
#     def fun3():
#         return "在fun1函数中的fun3函数中"
#
#     print(fun2())
#     print(fun3())
#     print("在fun1函数中")

# fun1()
# 也就是说：我们可以创建嵌套的函数。

# 三.从函数中返回函数
# 其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

# def fun1():
#     def fun2():
#         return "在fun1函数中的fun2函数中"
#
#     return fun2
#
# f = fun1()
# print(f)    # <function fun1.<locals>.fun2 at 0x7f7aa4dffc80>
# print(f()) # 在fun1函数中的fun2函数中

# 四.将函数作为参数传递给另一个函数
# def base():
#     return "I am Base function"
#
# def doSomethingBeforeBase(func):
#     print("在Base函数调用之前")
#     print(func())
#
# doSomethingBeforeBase(base)
# 在Base函数调用之前
# I am Base function

# 五.来写第一个装饰器
# def MyFirstDecorator(func):
#     def wrapTheFunction():
#         print("我装饰前面")
#         func()
#         print("我装饰后面")
#     return wrapTheFunction
#
# @MyFirstDecorator
# def needDecoration():
#     print("我需要装饰")
#
# needDecoration()
# 等价于执行了下面两句：
# tempFun = MyFirstDecorator(needDecoration)
# tempFun()

# 如果我们运行如下代码会存在一个问题：
# print(needDecoration.__name__)  # wrapTheFunction

# 这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。

# from functools import wraps
#
# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_func()")
#     return wrapTheFunction
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey yo! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
# print(a_function_requiring_decoration.__name__)
# # Output: a_function_requiring_decoration

# 六.带参数的装饰器
# 因为装饰器函数的参数只能写一个，所以可以考虑多加一层函数,但在装饰时得运行函数，而不是写函数名
# 注意：如果被装饰的函数需要参数，那么装饰器里的函数必须也要有参数

from functools import wraps

def logit(logfile='out.log'):
    def log(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            log_string = func.__name__ + " log."
            print(log_string)
            with open(logfile, "a") as f:
                f.write(log_string + "\n")

            # return func(*args, **kwargs)
        return wrapped
    return log

@logit()
def MyFunc(name):
    print("hello", name)

@logit()
def YourFunc(name):
    print("hi", name)

MyFunc("kain")
YourFunc("huck")