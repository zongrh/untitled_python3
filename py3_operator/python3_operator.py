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
"""
Python赋值运算符
以下假设变量a为10，变量b为20：

运算符	描述	实例
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
"""
a = 21
b = 10
c = 0
c = a + b
print(c)
c += a
print("c+=a ---- c=c+a", c)
c *= a
print("c*=a ---- c=c*a", c)
c /= a
print("c/=a ---- c=c/a", c)
c %= a
print("c%=a ---- c=c%a", c)
c **= a
print("c**=a ---- c=c**a", c)
c //= a
print("c//=a ---- c=c//a", c)
print("-----------------------------")
"""
Python位运算符
运算符	描述	实例
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
"""
a = 60  # 60= 0011 1100
b = 13  # 13= 0000 1101
c = 0
c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)
c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)
print("-----------------------------")
"""
Python逻辑运算符
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符	逻辑表达式	描述	实例
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
"""
a = 10
b = 20
if (a and b):
    print("ab都为true")
else:
    print("ab有一个不为true")

if (a or b):
    print("ab都为true或者其中一个为true")
else:
    print("ab都不为true")
# 修改变量值 a
a = 0
if (a and b):
    print("ab都为true")
else:
    print("ab有一个不为true")

if (a or b):
    print("ab都为true，或者其中一个为true")
else:
    print("ab都不为true")

if not (a and b):
    print("ab都为false，或者其中一个变量为false")
else:
    print("ab都为true")
print("-----------------------------")

"""
Python成员运算符
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
"""
a = 10
b = 20
list = [1, 2, 3, 4, 5]
if (a in list):
    print("list in a")
else:
    print("list not in a ")
