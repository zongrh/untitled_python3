""""""
"""
Python 文件 IO
Document 对象参考手册 Python3 实例

以下代码演示了Python基本的文件操作，包括 open，read，write.txt：
"""
# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)