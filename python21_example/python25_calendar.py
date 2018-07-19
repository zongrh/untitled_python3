""""""
import calendar

"""Python 生成日历
Document 对象参考手册 Python3 实例

以下代码用于生成指定日期的日历："""
# 引入日历模块
yy = int(input("输入年份："))
mm = int(input("输入月份："))
print(calendar.month(yy, mm))
print()
