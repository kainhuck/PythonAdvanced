#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 首先让我告诉你, 其实并不是必须写成*args 和**kwargs。 只有变量前面的 *(星号)才是必须的. 你也可以写成*var 和**vars. 而写成*args 和**kwargs只是一个通俗的命名约定。

# *args用于输入不定数量的参数
def args_test(num, *args):
    print("第1个元素： " + str(num))
    for i in range(len(args)):
        print("第" + str(i+2) + "个元素： " + str(args[i]))

# args_test(123,64,12,7,99)
# 输出：
# 第1个元素： 123
# 第2个元素： 64
# 第3个元素： 12
# 第4个元素： 7
# 第5个元素： 99


# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
def kwargs_test_1(name, age, sex):
    print("name:", name)
    print("age:", age)
    print("sex:", sex)

# 普通用法
# kwargs_test_1("kain", 18, "man")

# **kwargs用法
me = {
    "name": "kain",
    "age": 18,
    "sex": "man"
}
kwargs_test_1(**me)

def kwargs_test_2(**kwargs):
    # for item in kwargs:
    #     print("{0} -> {1}".format(item, kwargs[item]))
    for key, value in kwargs.items():
        print("{0} -> {1}".format(key, value))

kwargs_test_2(name="kain", age=18, sex="man")

# 那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
# some_func(fargs, *args, **kwargs)