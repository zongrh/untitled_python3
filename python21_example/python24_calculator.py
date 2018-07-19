""""""
"""
Python 简单计算器实现
Document 对象参考手册 Python3 实例
以下代码用于实现简单计算器实现，包括两个数基本的加减乘除运输：
"""


# 定义函数
def add(x, y):
    "相加"
    return x + y


def subtract(x, y):
    "相减"
    return x - y


def multiply(x, y):
    "相乘"
    return x * y


def divide(x, y):
    "相除"
    return x / y


"用户输入"
print("选择运算符：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
choice = input("输入你的选择（1/2/3/4）:")
num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "+", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("非法输入")
print("---------------------------------------------------")
def divide(x,y):
    #相除
    if y ==0:
        print('0不能做为分母')
        return
    else:
        return x/y

choice =int(input("请选择运算:\n1,相加\n2,相减\n3,相乘\n4,相除\n请输入运算(1/2/3/4):"))
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
if choice ==1:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif choice ==2:
    print("{}-{}={}".format(num1,num2,num1-num2))
elif choice ==3:
    print("{}x{}={}".format(num1,num2,num1*num2))
elif choice ==4:
    print("{}/{}={}".format(num1,num2,divide(num1,num2)))
else:
    print("选择的运算为非法输入")