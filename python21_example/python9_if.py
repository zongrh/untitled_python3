""""""
# 用户输入数字

num = float(input("输入一个数字: "))
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

print("--------------------")
# 内嵌 if 语句

num = float(input("输入一个数字: "))
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")
print("------------------------TEST")
while True:
    try:
        num = float(input('请输入一个数字：'))
        if num == 0:
            print('输入的数字是零')
        elif num > 0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字')
