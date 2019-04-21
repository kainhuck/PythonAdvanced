#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.简易的Web Sever
# 你是否想过通过网络快速共享文件？好消息，Python为你提供了这样的功能。进入到你要共享文件的目录下并在命令行中运行下面的代码：

# python2
# python -m SimpleHTTPServer
# python3
# python -m http.server

# 2.漂亮的打印
# 你可以在Python REPL漂亮的打印出列表和字典。这里是相关的代码：
# from pprint import pprint
#
# my_dict = {"name": "kain", "age": 18, "personality": "awesome"}
# pprint(my_dict)

# 这种方法在字典上更为有效。此外，如果你想快速漂亮的从文件打印出json数据，那么你可以这么做：
# cat file.json | python -m json.tool

# 3.脚本性能分析
# python -m cProfile my_script.py
# 备注：cProfile是一个比profile更快的实现，因为它是用c写的

# 4.csv转换为json
#     python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

# 5.列表辗平
# 您可以通过使用itertools包中的itertools.chain.from_iterable轻松快速的辗平一个列表。下面是一个简单的例子：
import itertools
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))

# or
print(list(itertools.chain(*a_list)))

# 6.一行式的构造器
# 避免类初始化时大量重复的赋值语句
class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
