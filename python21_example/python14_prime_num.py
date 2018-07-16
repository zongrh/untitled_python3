""""""
import math

print("------------------------------------1")
"""
Python 质数判断
Document 对象参考手册 Python3 实例

一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
换句话说就是该数除了1和它本身以外不再有其他的因数。
"""
num = int(input("请输入一个数字："))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘以", num // i, "是", num)
            break
    else:
        print(num, "是质数")
else:
    print(num, "不是质数")
print("------------------------------------2")
"""
原作者的算法基本正确，但时间复杂度较高，在判断一个大数是质数还是合数的情况下，
应该在查看因子那里的循环中使用到平方根。代码如下：
"""
# while True:
# 用户输入数字
num = int(input("TEST2 请输入一个数字："))
# 质数大于1
if num > 1:
    #     找到其平方根减少算法时间
    square_num = math.floor(num ** 0.5)
    print("num ** 0.5  ", num ** 0.5)
    print("square_num ", square_num)
    for i in range(2, (square_num + 1)):
        if (num % i) == 0:
            print(num, "是合数")
            print(i, "乘以", num // i, "是", num)
            break
    else:
        print("是质数")
# 原理是用了开根号法：
# 假如一个数N是合数,它有一个约数a,那么有a×b=N
# 则a、b两个数中必有一个大于或等于根号N,一个小于或等于根号N。
# 因此,只要小于或等于根号N的数（1除外）不能整除N,则N一定是素数。

print("------------------------------------3")
# 用while循环，进行质数判断
# 输入数字

num = int(input("TEST 3 输入一个数字："))
# 定义i
i = 2
while i < num:
    s = num % i
    if s == 0:
        print("{}能被除的数其中有{}".format(num, i))
        break
    else:
        i += 1
if num == i:
    print("是质数")
else:
    print("不是质数")
print("------------------------------------4")

count = 0
for i in range(1, 101):
    for j in range(1, i):
        if j == i // 2 and i % j == 1 or (i <= 3 and i != 1):
            if count == 4:
                print(i)
                count = 0
            else:
                print(i, end='\t')
                count += 1
            break
        if i % j == 0 and j != 1:
            break
print("------------------------------------5")
# -*- coding: UTF-8 -*-
# Python 程序用于检测用户输入的数字是否为质数
# 用户输入数字
num = int(input("请输入一个数字: "))


# 获取小于等于num平方根的质数表
def getPrimeList(n, oldPrimeList):
    for prime in oldPrimeList:
        if (n % prime) == 0:
            break
    if prime == oldPrimeList[-1]:
        oldPrimeList.append(n)


# 2,3是质数
if num == 2 or num == 3:
    print(num, "是质数")
# 对大于3的数用质数表来判断
elif num > 3:
    judge_num = int(num ** 0.5) + 1
    primeList = [2]
    for i in range(2, judge_num):
        getPrimeList(i, primeList)
    for i in primeList:
        if (num % i) == 0:
            print(num, "不是质数")
            break
    else:
        print(num, "是质数")
# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")

print("------------------------------------6")

# 用户输入数字
num = int(input("请输入一个数字: "))
# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, (int(num / 2) + 1)):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")
print("------------------------------------7")
