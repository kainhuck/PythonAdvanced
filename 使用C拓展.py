#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 开发者有三种方法可以在自己的Python代码中来调用C编写的函数-ctypes，SWIG，Python/C API。每种方式也都有各自的利弊。

# 1.CTypes
# ctypes模块提供了和C语言兼容的数据类型和函数来加载dll文件，因此在调用时不需对源文件做任何的修改。
#For Linux
#$  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c

#For Mac
#$ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c

from ctypes import *

adder = CDLL('./adder.so')

res_int = adder.add_int(4, 5)
print("4 + 5 = " + str(res_int))

a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float

print("5.5 + 4.5 = " + str(add_float(a, b)))

# 在Python文件中，一开始先导入ctypes模块，然后使用CDLL函数来加载我们创建的库文件。这样我们就可以通过变量adder来使用C类库中的函数了。当adder.add_int()被调用时，内部将发起一个对C函数add_int的调用。ctypes接口允许我们在调用C函数时使用原生Python中默认的字符串型和整型。

# 而对于其他类似布尔型和浮点型这样的类型，必须要使用正确的ctype类型才可以。如向adder.add_float()函数传参时, 我们要先将Python中的十进制值转化为c_float类型，然后才能传送给C函数。这种方法虽然简单，清晰，但是却很受限。例如，并不能在C中对对象进行操作。

#+++++++++++++++++++++++++++++++++++++++++++++++++++
# SWIG
# SWIG是Simplified Wrapper and Interface Generator的缩写。是Python中调用C代码的另一种方法。在这个方法中，开发人员必须编写一个额外的接口文件来作为SWIG(终端工具)的入口。

# Python开发者一般不会采用这种方法，因为大多数情况它会带来不必要的复杂。而当你有一个C/C++代码库需要被多种语言调用时，这将是个非常不错的选择。

# C程序源代码
# #include <time.h>
# double My_variable = 3.0;
#
# int fact(int n) {
#     if (n <= 1) return 1;
#     else return n*fact(n-1);
#
# }
#
# int my_mod(int x, int y) {
#     return (x%y);
#
# }
#
# char *get_time()
# {
#     time_t ltime;
#     time(&ltime);
#     return ctime(&ltime);
#
# }

# 编译
# unix % swig -python example.i
# unix % gcc -c example.c example_wrap.c \
#     -I/usr/local/include/python2.1
# unix % ld -shared example.o example_wrap.o -o _example.so

# 输出
# >>> import example
# >>> example.fact(5)
# 120
# >>> example.my_mod(7,3)
# 1
# >>> example.get_time()
# 'Sun Feb 11 23:01:07 1996'
# >>>

# Python/C API
# Python/C API可能是被最广泛使用的方法。它不仅简单，而且可以在C代码中操作你的Python对象。

# 这种方法需要以特定的方式来编写C代码以供Python去调用它。所有的Python对象都被表示为一种叫做PyObject的结构体，并且Python.h头文件中提供了各种操作它的函数。例如，如果PyObject表示为PyListType(列表类型)时，那么我们便可以使用PyList_Size()函数来获取该结构的长度，类似Python中的len(list)函数。大部分对Python原生对象的基础函数和操作在Python.h头文件中都能找到。

# https://docs.pythontab.com/interpy/c_extensions/python_c_api/