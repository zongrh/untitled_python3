"""序列化"""
import json

"""JSON
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下："""
"""JSON类型	Python类型
{}         	dict
[]          	list
"string"	     str
1234.56       	int或float
true/false	     True/False
null	         None
"""
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
d = dict(name="Bob", age="22", score="77")
print(json.dumps(d))
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化：
json_str = '{"name": "Bob", "age": "22", "score": "77"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Bob", 20, 77)


# print("Student--Json:", json.dumps(s))#会报错 TypeError
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.dumps(s, default=lambda obj: obj.__dict__))
