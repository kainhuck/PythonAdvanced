#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 循环是任何语言的一个必备要素。同样地，for循环就是Python的一个重要组成部分。然而还有一些东西是初学者并不知道的。我们将一个个讨论一下。
#
# 我们先从已经知道的开始。我们知道可以像这样使用for循环：
#
# fruits = ['apple', 'banana', 'mango']
# for fruit in fruits:
#     print(fruit.capitalize())

# Output: Apple
#         Banana
#         Mango
# 这是一个for循环非常基础的结构。现在我们继续看看，Python的for循环的一些鲜为人所知的特性。

# else从句
# 这个else从句会在循环正常结束时执行。这意味着，循环没有遇到任何break. 一旦你掌握了何时何地使用它，它真的会非常有用。
# 有个常见的构造是跑一个循环，并查找一个元素。如果这个元素被找到了，我们使用break来中断这个循环。有两个场景会让循环停下来。 - 第一个是当一个元素被找到，break被触发。 - 第二个场景是循环结束。
#
# 现在我们也许想知道其中哪一个，才是导致循环完成的原因。一个方法是先设置一个标记，然后在循环结束时打上标记。另一个是使用else从句。

#
# for item in containers:
#     if search_something(item):
#         # Found it!
#         process(item)
#         break
# else:
#     # Didn't find anything..
#     not_found_in_container()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        print(n, "is a prime number")
