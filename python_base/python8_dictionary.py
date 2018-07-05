""""""
import copy

"""
Python3 字典
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d={key1:value1,key2:value2}
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""
# 一个简单的字典：
dict = {"alice": "2341", "heth": "9210", "cecil": "3285"}
# 也可以如此创建
dict1 = {"abc": 456}
dict2 = {"abc": 123, 98.67: 37}
# ----------------------------访问字典中的值
dict = {"name": "runoob", "age": 17, "class": "first"}
print("名字：", dict["name"], "  年龄：", dict["age"], "  年级：", dict["class"])
print("---------------------------------------------------")
# 如果用字典中没有的键访问数据会报错
# print(dict["alice"])
# ----------------------------修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict = {"name": "runoob", "age": 17, "class": "first"}
print(dict)
dict["age"] = 111  # 更新age
print(dict)
dict["age"] = "2222222222"  # 更新age
print(dict)
dict["school"] = "菜鸟大学"  # 没有字段的话会在原字典中增加
print(dict)
del dict["name"]  # 删除键 “name”及对应值
print(dict)
del dict["age"]  # 删除键“age”及对应值
print(dict)
dict_copy = dict.copy()  # 复制当前字典
print(dict_copy)
dict.clear()  # 清空字典
del dict  # 删除字典
# ----------------------------字典键的特性
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {"name": "laj", "age": 77, "name": "菜鸟"}
print("dict[name]", dict["name"])
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
# dict = {["Name"]: "runoob", "age": 7}
print(dict)
"""
字典内置函数&方法
Python字典包含了以下内置函数：
序号	函数及描述	实例
1	len(dict)
计算字典元素个数，即键的总数。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)
3
2	str(dict)
输出字典，以可打印的字符串表示。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(dict)
<class 'dict'>
"""
dict = {"name": "runoob", "age": 17, "class": "first"}
print(len(dict))  # 计算字典元素个数，即键的总数。
print(str(dict))  # 输出字典，以可打印的字符串表示。
print(type(dict))  # 返回输入的变量类型，如果变量是字典就返回字典类型
# Python字典包含了以下内置方法：
# 序号	函数及描述
# 1	radiansdict.clear()
# 删除字典内所有元素
# dict.clear()
# 2	radiansdict.copy()
# 返回一个字典的浅复制
dict_c1 = dict.copy()  # 对象拷贝，浅拷贝
dict_c1 = copy.copy(dict_c1)  # 对象拷贝，浅拷贝
print("浅复制", dict_c1)
dict_c2 = copy.deepcopy(dict)  # 对象拷贝，深拷贝
print("深度复制", dict_c2)
# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ("name", "age")
dict_new = dict.fromkeys(seq)
print("新的字典为", dict_new)
dict_new = dict.fromkeys(seq, 10)
print("新的字典为", dict_new)
province = dict.fromkeys(["黑龙江", "吉林", "辽宁"], [1, {"Capital": "哈尔滨"}])
print(province)
# 4	radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
print(dict.get("age"))
# 5	key in dict
# 如果键在字典dict里返回true，否则返回false
if "age" in dict:
    print("键age存在")
else:
    print("键age不存在")
# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组
print("dict.items()", dict.items())
# 7	radiansdict.keys()
# 以列表返回一个字典所有的键
print("dict.keys()", dict.keys())
# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict = {"name": "runoob", "age": 17, "class": "first"}
dict.setdefault("age", 1111111)
print(dict)
print(dict.setdefault("age", 1111111))
print(dict.setdefault("age1", 1111111))
print(dict)
# 9	radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female'}
print(dict)
print(dict2)
dict.update(dict2)
print(dict)
# 10	radiansdict.values()
# 以列表返回字典中的所有值
print(dict.values())
# 11	pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = site.pop('name')
print(pop_obj)
# 12	popitem()
# 随机返回并删除字典中的一对键和值(一般删除末尾对)。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)