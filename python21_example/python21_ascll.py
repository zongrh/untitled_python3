""""""
"""Python ASCII码与字符相互转换
Document 对象参考手册 Python3 实例

以下代码用于实现ASCII码与字符相互转换："""

# 用户输入字符
c=input("请输入一个字符：")
# 用户输入ASCLL码，并将输入数字转化为整形
a=int(input("请输入一个ASCLL码："))

print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))