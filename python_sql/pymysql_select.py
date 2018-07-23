""""""
import pymysql

# 获取数据库连接
db = pymysql.connect("localhost", "root", "123456", "python_test")
# 获取数据库操作的游标
cursor = db.cursor()
# SQL语句
sql = "select * from employee where income> '%d'" % (1000)

try:
    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))
except:
    print("Error:unable to fetch data")

#     关闭数据库连接
db.close()
