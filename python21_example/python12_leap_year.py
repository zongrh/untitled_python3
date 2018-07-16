""""""
"""
Python 判断闰年
Document 对象参考手册 Python3 实例

以下实例用于判断用户输入的年份是否为闰年：
"""
year = int(input("输入一个年份："))
if (year % 4 == 0):
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0}输入年份是闰年".format(year))
        else:
            print("{0}输入年份不是闰年".format(year))
    else:
        print("{0}输入年份是闰年".format(year))
else:
    print("{0}输入年份不是闰年".format(year))
print("------------------------------------")
var = True
while var:
    year = int(input("请输入一个年份："))
    if ((year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0):
        print("{0}是闰年".format(year))
    else:
        print("{0}不是是闰年".format(year))
    if year == 2020:
        var = False
