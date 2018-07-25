""""""
import os

"""
Python3 File(文件) 方法
"""
"""
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

序号	方法及描述
1	
file.close()
关闭文件。关闭后文件不能再进行读写操作。

2	
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3	
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4	
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。

5	
file.next()
返回文件下一行。

6	
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。

7	
file.readline([size])
读取整行，包括 "\n" 字符。

8	
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

9	
file.seek(offset[, whence])
设置文件当前位置

10	
file.tell()
返回文件当前位置。

11	
file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

12	
file.write.txt(str)
将字符串写入文件，返回的是写入的字符长度。

13	
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
"""
print("------------------------------TEST")
# 检索指定路径下后缀是 py 的所有文件：
ls = []


def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == 'PY':
                ls.append(pathTmp)
    except PermissionError:
        pass


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path, ls)
    # print(len(ls))
    print(ls)
    print(len(ls))


main()
"""
获取文件后缀：
"""


def getfile_fix(filename):
    return filename[filename.rfind('.') + 1:]


print(getfile_fix('runoob.txt'))
"""
用户输入"xxx.txt"类文档文件名

用户输入被替换的"待替换字"

用户输入替换目标"新的字"

用户判断是否全部替换 yes/no
"""

#
# def file_replace(file_name, rep_word, new_word):
#     f_read = open(file_name)
#
#     content = []
#     count = 0
#
#     for eachline in f_read:
#         if rep_word in eachline:
#             count = count + eachline.count(rep_word)
#             eachline = eachline.replace(rep_word, new_word)
#         content.append(eachline)
#
#     decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
#                    % (file_name, count, rep_word, rep_word, new_word))
#
#     if decide in ['YES', 'Yes', 'yes']:
#         f_write = open(file_name, 'w')
#         f_write.writelines(content)
#         f_write.close()
#
#     f_read.close()
#
#
# file_name = input('请输入文件名：')
# rep_word = input('请输入需要替换的单词或字符：')
# new_word = input('请输入新的单词或字符：')
# file_replace(file_name, rep_word, new_word)
"""
在上面的例子中，write.txt(),read() 方法默认是写入到当前 .py 同文件夹下面的，此外 w+ 的使用方法：不能直接 write.txt() 后，在进行读取，这样试读不到数据的，因为数据对象到达的地方为文件最后，读取是向后读的，因此，会读到空白，应该先把文件对象移到文件首位
"""
f = open("forwrite.txt", "w+", encoding='utf-8')
f.write("可以 ，你做的很好！ 6666")  # 此时文件对象在最后一行，如果读取，将读不到数据
s = f.tell()  # 返回文件对象当前位置
f.seek(0, 0)  # 移动文件对象至第一个字符
str = f.read()
print(s, str, len(str))
"""
看上面分享的笔记，有个大佬打开文件然后没有关闭。。。

一般来说推荐以下方法：
"""
# 写
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('test')
# 读
with open('test.txt', 'r', encoding='utf-8') as f:
    # f.readlines()
    print(f.readlines())
