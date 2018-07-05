""""""
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
import random

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
print("----------------------------")
"""
Python3 条件控制
Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
"""
var1 = 100
if var1:
    print("if表达式为true")
    print(var1)

var2 = 0
if var2:
    print("if表达式为true")
    print(var2)
print("Good Bye!")
print("----------------------------")
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你在逗我吗")
# elif age == 1:
#     print("相当于14岁的人")
# elif age == 0:
#     print("相当于22岁的人")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
# 退出提示
# input("点击enter键退出")
print("----------------------------")
"""
以下为if中常用的操作运算符:
操作符	描述
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较对象是否相等
!=	不等于
"""
# 程序演示了 == 操作符
# 使用数字
print(5 == 6)
# 使用变量
x = 5
y = 8
print(x == y)
print("----------------------------")
# 该实例演示了数字猜谜游戏
# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

"""
------------------if 嵌套
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
"""
# num = int(input("输入一个数字："))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 2 和 3")
#     else:
#         print("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("你输入的数字不能整除 2 和 3")
"""
------------------------------------------- Test
"""
x = random.choice(range(100))
y = random.choice(range(200))
print("x:", x, "y:", y)
if x > y:
    print("x:", x)
elif x == y:
    print("x+y:", x + y)
else:
    print("y:", y)
"""
下表列出了不同数值类型的 true 和 false 情况：
类型	False	True
布尔	False(与0等价)	True(与1等价)
数值	0,   0.0	非零的数值
字符串	'',  ""(空字符串)	非空字符串
容器	[],  (),  {},  set()	至少有一个元素的容器对象
None	None	非None对象
"""
