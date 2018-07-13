""""""
"""以下实例为通过用户输入三角形三边长度，并计算三角形的面积："""
a = float(input("三角形第一边长："))
b = float(input("三角形第二边长："))
c = float(input("三角形第三边长："))
# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("三角形面积为：%0.2f" % area)
print("---------------------------------------")
a = float(input("三角形第一边长："))
b = float(input("三角形第二边长："))
c = float(input("三角形第三边长："))
while a + b < c or a + c < b or b + c < a:
    print('输入的边构不成三角形，请重新输入！')
    a = float(input('输入三角形第一边长：'))
    b = float(input('输入三角形第二边长：'))
    c = float(input('输入三角形第三边长：'))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为：%0.2f' % area)
