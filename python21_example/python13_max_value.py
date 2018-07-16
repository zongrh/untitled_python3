""""""
"""
Python 获取最大值函数
Document 对象参考手册 Python3 实例

以下实例中我们使用max()方法求最大值：
"""
# 最简单的
print(max(1, 11, 12))
print(max(22, 22.1, 11))
# 也可以对队列和元组使用
print(max([1, 1.1, 22]))
print(max([55.1, 55.2, 50.9]))
# 更多实例
# 更多实例
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))
print("------------------------------------------")
N = int(input("请输入要比较数字大小个数："))
print("请输入需要对比的数字：")
num = []
for i in range(1, N + 1):
    temp = int(input("输入第%d个数字" % i))
    num.append(temp)
print("您输入的数字为：", num)
print("最大值为：", max(num))
print("------------------------------------------")
N = int(input('输入需要对比大小数字的个数：\n'))

num=[ int(input('请输入第 %d 个对比数字 \n'%(i)))for i in range(1,N+1)]

print('您输入的数字为:',list(num))
print('最大值为: ',max(num))