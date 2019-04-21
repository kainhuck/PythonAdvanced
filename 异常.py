#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个简单的例子
# try:
#     file = open('test.txt', 'rb')
# except IOError as e:
#     print('An IOError occurred {}'.format(e.args[-1]))

# 处理多个异常
# 方法一:把所有可能的异常放在一个元组里
# try:
#     file = open('test.txt', 'rb')
# except (IOError, EOFError) as e:
#     print("An error occurred {}".format(e.args[-1]))

# 方法二:分开处理
# try:
#     file = open('test.txt', 'rb')
# except EOFError as e:
#     print("An EOF error occurred")
#     raise e
# except IOError as e:
#     print("An IO error occurred")
#     raise e

# 方法三:捕获所有异常
# try:
#     file = open('test.txt', 'rb')
# except Exception:
#     # 打印一些日志，或者任何你想要做的事
#     raise

# finally从句
# 包裹到finally从句中的代码不管异常是否触发都将会被执行。这可以被用来在脚本执行之后做清理工作
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# try/else从句
# 我们常常想在没有触发异常的时候执行一些代码。这可以很轻松地通过一个else从句来达到。
#
# 有人也许问了：如果你只是想让一些代码在没有触发异常的情况下执行，为啥你不直接把代码放在try里面呢？
# 回答是，那样的话这段代码中的任意异常都还是会被try捕获，而你并不一定想要那样。
#
# 大多数人并不使用else从句，而且坦率地讲我自己也没有大范围使用。这里是个例子：

try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')