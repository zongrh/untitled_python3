""""""

"""
以下实例为通过用户输入数字，并计算二次方程："""
# 二次方程式 ax**2 + bx + c=0
# abc用户提供为实数，a!=0

# 导入cmath(复杂数学运算)模块
import cmath

a = float(input("输入a："))
b = float(input("输入b："))
c = float(input("输入c："))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("结果为{0}和{1}".format(sol1, sol2))
