""""""
import calendar

"""Python 计算每个月天数
Document 对象参考手册 Python3 实例

以下代码通过导入 calendar 模块来计算每个月的天数："""
yy = int(input("年份："))
mm = int(input("月份："))

monthRange = calendar.monthrange(yy, mm)
print(monthRange)
# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），
# 第二个元素是这个月的天数。以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。

print("--------------------")
print(calendar.month(yy, mm))
