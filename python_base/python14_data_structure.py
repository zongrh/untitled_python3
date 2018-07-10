""""""
from collections import deque

"""
Python3 数据结构
本章节我们主要结合前面所学的知识点来介绍Python数据结构。
"""
"""
列表
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
以下是 Python 中列表的方法：
方法	描述
list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。
"""
a = [66.25, 333, 333, 1, 1234.5]
print(a)
print(a.count(333), a.count(66.25), a.count("x"))  # 返回 x 在列表中出现的次数。
# 	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
a.insert(2, -11)
print(a)
# 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
a.append(33337)
print(a)
# 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
print(a.index(333))
print(a)
# 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
a.remove(333)
print(a)
# 倒排列表中的元素。
a.reverse()
print(a)
# 对列表中的元素进行排序。
a.sort()
print(a)
"""
将列表当做堆栈使用
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：
"""
# 后进先出
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print("---------------------")
"""
将列表当作队列使用
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
"""
queue = deque(["eric", "john", "mchael"])
print(queue)
queue.append("terry")
print(queue)
queue.append("graham")
print(queue)
queue.append("erer")
print(queue)
queue.append("laj")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
print("---------------------")
"""
列表推导式
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
如果希望表达式推导出一个元组，就必须使用括号。
这里我们将列表中每个数值乘三，获得一个新的列表：
"""
vec = [2, 4, 6]
print(vec)
print([3 * x for x in vec])
print("------------")
# 现在我们玩一点小花样：
print([[x, x ** 2] for x in vec])
# 这里我们对序列里每一个元素逐个调用某方法：
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print("------------")

# 我们可以用 if 子句作为过滤器：
print([3 * x for x in vec if x > 3])
print([3 * x for x in vec if x < 2])
print("------------")

# 以下是一些关于循环和其它技巧的演示：
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])
print([str(round(355 / 133, i)) for i in range(1, 6)])
print("------------")
"""
嵌套列表解析
Python的列表还可以嵌套。
"""
# 以下实例展示了3X4的矩阵列表：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
print("------------")
"""
del 语句
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。
可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
"""
# 例如：
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[1:4]
print(a)
del a[:]
print(a)
# 也可以用 del 删除实体变量：
del a

print("---------------------")

"""
元组和序列
元组由若干逗号分隔的值组成，例如：
"""
t = 12345, 54321, "hello"
print(t[0])
u = t, (1, 2, 3, 4, 5)
print(u)
# 如你所见，元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
print("---------------------")

"""
集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
"""
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # 删除重复的
print("orange" in basket)  # 检测成员

a = set("fdjhs")
b = set("dfe")
print(a)  # 去掉重复的元素
print(b)  # 去掉重复的元素
print(b - a)  # 在a中的字母，但不在b中
print(a | b)  # 在a 或b 中的字母
print(a & b)  # a b中都有的字母
print(a ^ b)  # 在ab中的字母，但不同时在a和b中
# 集合也支持推导式
e = {x for x in "adafdgxgfgh" if x not in "abc"}
print(e)
print("---------------------")
"""
字典
另一个非常有用的 Python 内建数据类型是字典。
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
"""
# 这是一个字典运用的简单例子：
tel = {"jack": 4098, "sape": 4139}
print(tel)
tel["guolin"] = 4122
tel["zhang"] = 1111
print(tel)
print(tel["jack"])
del tel["sape"]
print(tel)
print(tel["zhang"])
print("guolin" in tel)
print("guolin" not in tel)
print(list(tel.keys()))
print(list(tel.values()))
# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
dect = ([("sape", 4139), ("guolin", 4127), ("zhang", 1111)])
print(dect)
# 此外，字典推导可以用来创建任意键和值的表达式词典：
print({x: x ** 2 for x in (2, 4, 6)})
"""
遍历技巧
在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
"""
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)
"""
在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
"""
for i, v in enumerate(["tic", "tac", "top"]):
    print(i, v)
print("------------------")
"""
同时遍历两个或更多的序列，可以使用 zip() 组合：
"""
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print(q, a)
"""
要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
"""
for i in reversed(range(1, 10, 2)):
    print(i)
print("---------------------------------------------------TEST")
# 元组不可变，若元组的成员可变类型，则成员可编辑。
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
t = a, b, c
print(t)
del b[1:4]
print(t)

print("---------------------------------------------------TEST")
# 列表推导式的执行顺序：
# 各语句之间是嵌套关系，
# 左边第二个语句是最外层，
# 依次往右进一层，
# 左边#第一条语句是最后一层。
# print([x * y for x in range[1:5] if x > 2 for y in range[1:4] if x < 3])

print("---------------------------------------------------TEST")
# 有多个列表需要遍历时，需要zip，除了用'{0}{1}'.format(q,a)的方法，还可以使用%s方法（两者效果一样一样的）：
questions=['name','quest','favorite color']
answers=['qinshihuang','the holy','blue']
for q,a in zip(questions,answers):
    print('what is your %s? it is %s' %(q,a))
    print('what is your {0}? it is {1}'.format(q,a))