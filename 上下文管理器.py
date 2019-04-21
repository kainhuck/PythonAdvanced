#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 上下文管理器允许你在有需要的时候，精确地分配和释放资源。

# 上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件(with语句)

# 用类实现
# 一个上下文管理器的类，最起码要定义__enter__和__exit__方法。
# 让我们来构造我们自己的开启文件的上下文管理器，并学习下基础知识。
# class File(object):
#     def __init__(self, filename, method):
#         self.file_obj = open(filename, method)
#
#     def __enter__(self):
#         return self.file_obj
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file_obj.close()
# # 通过定义__enter__和__exit__方法，我们可以在with语句里使用它。我们来试试：
# with File('demo.txt', 'w') as f:
#     f.write("Hola!")
# 我们的__exit__函数接受三个参数。这些参数对于每个上下文管理器类中的__exit__方法都是必须的。我们来谈谈在底层都发生了什么。
#
# 1.with语句先暂存了File类的__exit__方法
# 2.然后它调用File类的__enter__方法
# 3.__enter__方法打开文件并返回给with语句
# 4.打开的文件句柄被传递给opened_file参数
# 5.我们使用.write()来写文件
# 6.with语句调用之前暂存的__exit__方法
# 7.__exit__方法关闭了文件

# 异常处理
# 我们还没有谈到__exit__方法的这三个参数：type, value和traceback。
# 在第4步和第6步之间，如果发生异常，Python会将异常的type,value和traceback传递给__exit__方法。
# 它让__exit__方法来决定如何关闭文件以及是否需要其他步骤。在我们的案例中，我们并没有注意它们。

# 我们来列一下，当异常发生时，with语句会采取哪些步骤。
# 1. 它把异常的type,value和traceback传递给__exit__方法
# 2. 它让__exit__方法来处理异常
# 3. 如果__exit__返回的是True，那么这个异常就被优雅地处理了。
# 4. 如果__exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出。
# 在我们的案例中，__exit__方法返回的是None(如果没有return语句那么方法会返回None)。
# 我们尝试下在__exit__方法中处理异常：
# class File(object):
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)
#     def __enter__(self):
#         return self.file_obj
#     def __exit__(self, type, value, traceback):
#         print("Exception has been handled")
#         self.file_obj.close()
#         return True
#
# with File('demo.txt', 'w') as opened_file:
#     opened_file.undefined_function()

# Exception has been handled
# 我们的__exit__方法返回了True,因此没有异常会被with语句抛出。

# 基于生成器的实现


# 我们还可以用装饰器(decorators)和生成器(generators)来实现上下文管理器。
# Python有个contextlib模块专门用于这个目的。我们可以使用一个生成器函数来实现一个上下文管理器，而不是使用一个类。
# 让我们看看一个基本的，没用的例子：
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()

# OK啦！这个实现方式看起来更加直观和简单。然而，这个方法需要关于生成器、yield和装饰器的一些知识。在这个例子中我们还没有捕捉可能产生的任何异常。它的工作方式和之前的方法大致相同。
#
# 让我们小小地剖析下这个方法。
# 1. Python解释器遇到了yield关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。
# 2. 因为这个装饰器，contextmanager会被调用并传入函数名（open_file）作为参数。
# 3. contextmanager函数返回一个以GeneratorContextManager对象封装过的生成器。
# 4. 这个GeneratorContextManager被赋值给open_file函数，我们实际上是在调用GeneratorContextManager对象。
#
# 那现在我们既然知道了所有这些，我们可以用这个新生成的上下文管理器了，像这样：
#
# with open_file('some_file') as f:
#     f.write('hola!')