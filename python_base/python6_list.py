""""""
import copy
from inspect import Traceback

"""
Python3 列表
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
"""
list1 = ["google", "runoob", 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
"""
访问列表中的值
使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
"""
list1 = ["google", "runoob", 1997, 2000]
list2 = [1, 2, 3, 4, 5]
print("list1[0]=", list1[0])
print("list2[1:5]=", list2[1:5])
print("----------------------------------")
"""
更新列表
你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：
"""
list = ["google", "runoob", 1997, 2000]
print("第三个元素为：", list[2])
list[2] = 200001
print(list)
list.append("666666")  # 在list后边 添加列表项
print("666666append", list)
list.insert(0, "555")  # 下标为 0 处 插入数据
print("5555insert", list)
print("----------------------------------")
"""
删除列表元素
可以使用 del 语句来删除列表的的元素，如下实例：
"""
list = ["google", "runoob", 19977, 2000]
print("原始列表：", list)
del list[2]
print("删除第三个元素", list)
print("----------------------------------")
"""
Python列表脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：
Python 表达式	结果	描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
"""
# list 长度为
list1 = ["google", "runoob", 19977, 2000]
list2 = ["-----------", "runoob", 19977, 2000]
print("list1长度为：", len(list1))
print("list1+list2：", list1 + list2)
print("list1 * 5：", list1 * 5)
print("7 in list1：", 7 in list1)
for x in list1:  # 遍历数据----迭代
    print("遍历结果：", x)
print("----------------------------------")
"""
Python列表截取与拼接
Python的列表截取与字符串操作类型，如下所示：
"""
# Python 表达式	结果	描述
# L[2]	'Taobao'	读取第三个元素
# L[-2]	'Runoob'	从右侧开始读取倒数第二个元素: count from the right
# L[1:]	['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素
L = ["google", "runoob", "taobao", "jd", "facebook", "ali"]
N = [1, 11, 111, 1111, 11111]
print("原数据", L)
print("从左开始读取第三个元素", L[2])
# print("从右开始读取第三个元素", L[-2])  # -x  时下标从-1 开始
print("输出从第二个元素开始的所有元素：", L[1:])
print("拼接 L + N", L + N)
print("----------------------------------")
"""
Python列表函数&方法
Python包含以下函数:

序号	函数
1	len(list)列表元素个数
2	max(list)返回列表元素最大值
3	min(list)返回列表元素最小值
4	list(seq)将元组转换为列表
------------------------------------------------常用
序号	方法
1	list.append(obj)在列表末尾添加新的对象
2	list.count(obj)统计某个元素在列表中出现的次数
3	list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)将对象插入列表
6	list.pop([index=-1]])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)移除列表中某个值的第一个匹配项
8	list.reverse()反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)对原列表进行排序
10	list.clear()清空列表
11	list.copy()复制列表
"""
list1 = ["google", 11111, 11111, "ali"]
list2 = [1, 2, 3.2, 4, 5.9, 2, 2, 1, 7]

# 1	len(list)列表元素个数
print("len(list)=", len(list))
# 2	max(list)返回列表元素最大值
print("max(list2)=", max(list2))
# 3	min(list)返回列表元素最小值
print("min(list2)=", min(list2))
# 4	list(seq)将元组转换为列表
# ------------------------------------------------常用
# 序号	方法
# 1	list.append(obj)在列表末尾添加新的对象
list2.append(11111111)
print("list2.append(11111111)=", list2)
# 2	list.count(obj)统计某个元素在列表中出现的次数
print("list2.count(2)=", list2.count(2))
# 3	list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)从列表中找出某个值第一个匹配项的索引位置
print("列表中第一次出现2的位置list2.index(2)=", list2.index(2))
# 5	list.insert(index, obj)将对象插入列表
list2.insert(0, "555")
print("list2.insert(0,xxx)=", list2)
# 6	list.pop([index=-1]])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list2.pop()  # 默认移除最后一个元素
list2.pop(0)  # 设置移除某一个元素
print("移除列表中的一个元素", list2)
# 7	list.remove(obj)移除列表中某个值的第一个匹配项
list2.remove(2)
print("删除列表中某个数据的第一个匹配项", list2)
# 8	list.reverse()反向列表中元素
list2.reverse()
print("反向列表中的元素", list2)
# 9	list.sort(cmp=None, key=None, reverse=False)对原列表进行排序
list2.sort()
print("对原列表进行排序", list2)
# 10	list.clear()清空列表
print("清空列表list1前：", list1)
list1.clear()
print("清空列表list1后：", list1)
# 11	list.copy()复制列表
list3 = []
print(list3)
list3 = list2.copy()
print(list3)

print("----------------------------------", "Test1")
list_2d = [
    [11 for col in range(2)]
    for row in range(5)
]
print(list_2d)
list_2d[0].append(3)
list_2d[0].append(1999)
list_2d[2].append(333333333)
print(list_2d)
print("----------------------------------", "Test2")
"""
我理解为:
l[start:end:span]
遍历 [start,end)，间隔为 span，当 span>0 时顺序遍历, 当 span<0 时，逆着遍历。
start 不输入则默认为 0，end 不输入默认为长度。
"""
l = [i for i in range(0, 15)]
print(l[::2])
print(l[1:11:2])
print("----------------------------------", "Test3")
"""
列表的复制
可以看到a b c 三个是同一id值，当改变当中任一列表元素的值后，三者会同步改变。
但d的元素值不会变，改变d的元素值其它三个变量内的元素值也不会变。
从a b c d 的id值来看，a b c 地址全一样，唯有d分配了新地址。
所以一般情况下想复制得到一个新列表并改变新列表内元素而不影响原列表，可以采用d的赋值方式。
这只是针对这种比较单一的普通列表。
"""
a = [1, 2, 3]
b = a
c = []
c = a
d = a[:]
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
c[0] = "A"
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
c[0] = "AA"
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
c[0] = "AAAA"
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))

print("----------------------------------", "Test4")
"""@sm 同学提到的列表的复制问题，其实可以用copy模块里 copy()函数解决，实例如下："""
a = [1, 2, 3, 4]
b = a
d = copy.copy(a)
b[0] = 'b'
print(a, b, d)
print(id(a), id(b), id(d))
print("----------------------------------", "Test5")
"""楼上两位同学说的都对,还有一个就是用list自带的copy()方法,把重新开辟内存空间存储新列表。"""
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
copy_list = original_list.copy()
copy_list = copy_list + ['a', 'b', 'c']
print("original_list:", original_list)
print("copy_list modify:", copy_list)
print("----------------------------------", "Test6")
list_empty = [0] * 10
print(list_empty)
# 这样就可以再去对list的各个元素进行初始化了
