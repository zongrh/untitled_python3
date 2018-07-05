""""""
"""
Python3 集合
集合（set）是一个无序不重复元素的序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
# 创建格式：
"""
parame = {value01,value02,...}
或者
set(value)
"""
basket = {"apple", "orange", "apple", "pear", "orange", "banna"}
print(basket)  # 去重功能
if "orange" in basket:
    print("orange 在basket")
else:
    print("orange 不在basket")
# 下边展示两个集合间的运算-----------集合中带有去重功能
a = set("abrsfdsfd")
b = set("sdfdfdsffdeeeewrweqwfsdfdsfdssdf")
print("集合 a 中包含的元素", a)  # 集合a中包含的元素
print("集合 b 中包含的元素", b)  # 集合b中包含的元素
print("集合 ab 中包含的元素", a | b)  # 集合ab中包含的元素
print("集合a和b中都包含的元素", a & b)  # 集合a和b中都包含的元素
print("不同时包含ab的元素", a ^ b)  # 不同时包含ab的元素
# print("----------------------------------------------")
"""
集合的基本操作
"""
print("-------------------------------------1、添加元素")
# 语法格式如下：
# s.add( x )
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
thisset = set(("google", "runoob", "taobao"))
thisset.add("facebook")  # 插入数据-----------随机插入
print(thisset)
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
thisset.update({1: 5, 3: 2})  # 插入字典数据-----------随机插入
# [11, 22, 33, 44, 55] 列表
thisset.update([11, 22, 33, 44, 55])  # 插入列表数据-----------随机插入
# (11, 22, 33, 44, 55) 元组
thisset.update((11, 22, 33, 44, 55))  # 插入元组数据-----------随机插入
print(thisset)
print("-------------------------------------2、移除元素")
# s.remove( x )
thisset = set(("google", "runoob", "taobao"))
print(thisset)
thisset.remove("google")  # 移除集合中的元素
# 移除集合中的元素时报错
# thisset.remove("faceook")
print(thisset)
# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
thisset.discard("taobao")
thisset.discard("taosdbao")
print(thisset)
# 我们也可以设置随机删除集合中的一个元素，语法格式如下：
# s.pop()
thisset = set(("google", "runoob", "taobao"))
thisset.pop()
print(thisset)
print("-------------------------------------3、计算集合元素个数")
thisset = set(("google", "runoob", "taobao"))
print(len(thisset))
print("-------------------------------------4、清空集合")
thisset = set(("google", "runoob", "taobao"))
print(thisset)
thisset.clear()
print(thisset)
print("-------------------------------------5、判断元素是否在集合中存在")
thisset = set(("google", "runoob", "taobao"))
if "google" in thisset:
    print("google 在 thisset")
else:
    print("google 不在thisset")

print("-------------------------------------Test测试")
# s.update( {"字符串"} ) 将字符串添加到集合中。
thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
thisset.update({"facebook"})
print(thisset)
# s.update("字符串") 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
thisset.update("yahoo")
print(thisset)
print("------------------------")
# 1.创建一个含有一个元素的集合
my_set = set(("apple",))
print(my_set)
# 2.创建一个含有多个元素的集合
my_set = set(("apple", "pear", "banana"))
print(my_set)
# 3.如无必要，不要写成如下形式
my_set = set(("apple"))
print(my_set)
my_set1 = set("apple")
print(my_set1)
