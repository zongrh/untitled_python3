""""""
"""Python 输出指定范围内的素数
Document 对象参考手册 Python3 实例

素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。

以下实例可以输出指定范围内的素数：
"""
lower = int(input("输入区间最小值："))
upper = int(input("输入区间最大值："))
list_num = []
for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            list_num.append(num)
            print(num)

print(list_num)
print("---------------------------------")
def isprime(x):
    if x == 1:
        return False
    k = int(x**0.5)
    for j in range(2, k + 1):
        if x % j == 0:
            return False
    return True
lower = int(input("请输入区间最小值："))
upper = int(input("请输入区间最大值："))
for i in range(lower, upper):
    if isprime(i):
        print(i, end = " ")