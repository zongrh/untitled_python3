""""""
"""
Python 判断奇数偶数
Document 对象参考手册 Python3 实例

以下实例用于判断一个数字是否为奇数或偶数：
"""
# python 判断奇数偶数
# 如果是偶数除以 2 余数为 0
# 如果是奇数除以 2 余数为 1
num = int(input("请输入数字:"))
if (num % 2) == 0:
    print("%s 是偶数!" % (num))
else:
    print("{}是奇数！".format(num))
print("-------------------------TEST")
while True:
    try:
        num = int(input("请输入一个整数："))  # 判断输入是否为整数
    except ValueError:  # 不是纯数字需要重新输入
        print("输入的不是整数")
        continue
    if num % 2 == 0:
        print("偶数")
        break  # 跳出循环，结束循环
    else:
        print("奇数")
