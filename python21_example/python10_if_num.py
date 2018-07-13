""""""
"""
Python 判断字符串是否为数字
Document 对象参考手册 Python3 实例

以下实例通过创建自定义函数 is_number() 方法来判断字符串是否为数字：
"""


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 测试字符串和数字
print(is_number("foo"))
print(is_number("1"))
print(is_number("1.2"))
print(is_number("1e25"))
print("")
# 测试Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False