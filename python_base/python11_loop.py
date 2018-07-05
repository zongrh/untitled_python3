""""""
"""
Python3 循环语句
本章节将为大家介绍Python循环语句的使用。
Python中的循环语句有 for 和 while。
"""
"""
-------------------------while 循环
Python中while语句的一般形式：
while 判断条件：
    语句
"""
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    print(sum)
print("1到%d之和为：%d" % (n, sum))
print("---------------------------------------------")
# var = 1
# while var == 1:
#     num = int(input("输入一个数字"))
#     print("你输入的数字是：", num)
# print("good bye")
# while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块：
count = 0
while count < 5:
    print(count, "小于 5")
    count = count + 1
else:
    print(count, "大于或等于 5")
print("---------------------------------------------")
flag = 1
# while (flag):
#     print("欢迎来到python")
# print("good bye ")
"""
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""
languages = ["c", "c++", "perl", "python"]
for x in languages:
    print(x)
print("----------good bye!")
# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
sites = ["baidu", "google", "runoob", "taobao"]
for site in sites:
    if site == "runoob":
        print("菜鸟教程")
        break
    print("循环数据", site)
else:
    print("没有循环数据")
print("完成循环")
"""
range()函数
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
"""
for i in range(5):
    print(i)
print("--------------------------------------")
# 你也可以使用range指定区间的值：
for i in range(5, 10):
    print(i)
print("--------------------------------------")
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
    print(i)
print("--------------------------------------")
# 负数
for i in range(-10, -100, -12):
    print(i)
print("--------------------------------------")
# 您可以结合range()和len()函数以遍历一个序列的索引,如下所示:
a = ["google", "baidu", "runoob", "taobao", "qq"]
for i in range(len(a)):
    print(i, a[i])
print("--------------------------------------")
# 还可以使用range()函数来创建一个列表：
list = list(range(5))
print(list)
print("--------------------------------------")
# break和continue语句及循环中的else子句
# break 语句可以跳出 for 和 while 的循环体。
# 如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
#  实例如下
for letter in "runoob":  # 第一个实例
    if letter == "b":
        break
    print("当前字母为：", letter)
print("--------------------------------------")

var = 10  # 第二个实例
while var > 0:
    print("当前变量值为：", var)
    var = var - 1
    if var == 5:
        break
print("good bye")
print("--------------------------------------")
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
for letter in "runoob":  # 第一个实例
    if letter == "o":  # 字母为o时跳出输出
        continue
    print("当前字母：", letter)
print("--------------------------------------")
var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为5时跳出输出
        continue
    print("当前变量：", var)
print("--------------------------------------")
# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false
# (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
# 如下实例用于查询质数的循环例子:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "等于", x, "*", n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, "是质数")
print("--------------------------------------")

# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例
"""
while True:
    pass
"""
# 以下实例在字母为 o 时 执行 pass 语句块:
for letter in "runoob":
    if letter == "o":
        pass
        print("执行 pass 块")
    print("当前字母：", letter)
print("good bye")
