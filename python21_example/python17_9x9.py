""""""
"""Python 九九乘法表
Document 对象参考手册 Python3 实例

以下实例演示了如何实现九九乘法表：
"""
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}x{}={}\t".format(i, j, j * i), end="")
    print()
print("-----------------------------------")
for 行 in range(1, 10):
    for 列 in range(1, 行 + 1):  # 内循环中，确保列 <= 行。
        print("{}*{}={}\t".format(列, 行, 列 * 行), end="")  # 确保同一行内容连续
        # print(行, 列)
    print()  # 另起一行！！！

input()  # 防止程序一闪而过，不在编译器中也能使用
print("-----------------------------------")
