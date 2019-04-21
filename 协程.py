#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # 先创建一个生成器
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         a, b = b, a + b
#         yield a
#
#
# # 使用这个生成器
# for i in fib(10):
#     print(i)

# 定义一个协程
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)
# 等等！yield返回了什么？啊哈，我们已经把它变成了一个协程。它将不再包含任何初始值，相反要从外部传值给它。我们可以通过send()方法向它传值。这有个例子：

search = grep("kain")
next(search)

search.send("i love u")
search.send("hello world")
search.send("kain huck")

# 发送的值会被yield接收。我们为什么要运行next()方法呢？这样做正是为了启动一个协程。就像协程中包含的生成器并不是立刻执行，而是通过next()方法来响应send()方法。因此，你必须通过next()方法来执行yield表达式。

# 我们可以通过调用close()方法来关闭一个协程。像这样：
search.close()