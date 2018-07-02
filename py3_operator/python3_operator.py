"""
算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
"""
"""
Python算术运算符
以下假设变量a为10，变量b为21：
运算符	描述	实例
+	加 - 两个对象相加	a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
"""
a = 21
b = 10
c = 0
c = a + b
print("a=", a, " b=", b)
print("c=a + b的值为：", c)
c = a - b
print("c=a - b的值为：", c)
c = a * b
print("c=a * b的值为：", c)
c = a / b
print("c=a / b的值为：", c)
c = a % b
print("c=a % b的值为：", c)
print("-----------------------------")
# 修改变量abc
a = 2
b = 3
c = a ** b
print("a=", a, " b=", b)
print("c= a** b的值为：", c)
print("-----------------------------")
a = 11
b = 5
print("a=", a, " b=", b)
c = a // b
print("c=a//b值为：", c)
print("-----------------------------")
"""
Python比较运算符
以下假设变量a为10，变量b为20：

运算符	描述	实例
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 True。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。
"""
a = 21
b = 10
c = 0
if (a == b):
    print("a==b")
else:
    print("a!=b")
if (a != b):
    print("a!=b")
else:
    print("a==b")
if (a < b):
    print("a<b")
else:
    print("a>=b")
if (a > b):
    print("a>b")
else:
    print("a<=b")
# 修改变量 ab
a = 5
b = 20
if (a <= b):
    print("a<=b")
else:
    print("a>b")
if (a >= b):
    print("a>=b")
else:
    print("a<b")
print("-----------------------------")
