""""""
import sys

"""
Python3 错误和异常
作为Python初学者，在刚学习Python编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。

Python有两种错误很容易辨认：语法错误和异常。
"""
"""语法错误
Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例"""
# while True  print("hello world")
# 这个例子中，函数print()被检查到有错误，是它前面缺少了一个冒号（:）。
# 语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。
"""异常
即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:"""
# print(10 * (1 / 0))
# print(4+spam*3)
# print("2" + 2)
"""异常处理
以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。
用户中断的信息会引发一个 KeyboardInterrupt 异常。"""
while True:
    try:
        x = int(input("Please enter number:"))
        print(x)
        break
    except ValueError:
        print("Oops! That was no valid number . Try again ")
"""
try语句按照如下方式工作；

首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
except (RuntimeError, TypeError, NameError):
        pass
"""
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise