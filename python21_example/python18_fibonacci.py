""""""
"""
Python 斐波那契数列
Document 对象参考手册 Python3 实例

斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。

Python 实现斐波那契数列代码如下：
"""
# Python 斐波那契数列实现

# 获取用户输入数据
nterms = int(input("你需要几项？"))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
print()
print("-----------------------------")
num = int(input("输入一个整数："))
f1 = 0
f2 = 1
if num <= 0:
    print("请输入一个正整数！")
elif num == 1:
    print("斐波拉契数列：%d" % f1)
else:
    print("斐波拉契数列：", end="")
    print(f1, f2, end=" ")
    for n in range(1, num - 1):
        f = f1 + f2
        f1, f2 = f2, f
        print(f, end=" ")
print()
print("-----------------------------")
L = [0, 1]
num = int(input("请输入你要的项数："))
if (num <= 0):
    print("请输入一个正整数！");
elif (num <= 2):
    if (num == 1):
        print("数列是：0")
    else:
        print("数列是：0,1")
else:
    for i in range(2, num):
        f = L[i - 1] + L[i - 2]
        L.append(f)
    print("数组是：")
    print(L)
print()
print("-----------------------------递归")
"""
两种实现方式，第一种是通过循环实现，第二种是通过递归调用来实现。
第二种代码稍显简洁，结构较清晰，但由于递归占用较多资源，对于大规模的计算消耗比较大，
运算比较慢。反而通过循环实现的运算较快。代码如下
"""
num=int(input("请输入要输出多少项："))
print("-------递归-------");
def Count_Function(n):
    if(n<3):
        return(n)
    else:
       return(Count_Function(n-1)+Count_Function(n-2))

i=1
while(i<=num):
    print(Count_Function(i),end="\t")
    i+=1
print()

#计算斐波那契数列，通过循环来实现
num=int(input("请输入您要显示的项数："))
print("-------循环-------");
n=3
a=[1,2]
if(num==1):
    print(a[0],end=" ")
elif(num==2):
    print(a[num-2],a[num-1],end=" ")
else:
    while(n<=num):
        temp=a[n-2]+a[n-3]
        a.append(temp)
        n+=1
    for i in a:
        print(i,end=' ')
print()