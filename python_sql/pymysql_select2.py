""""""
import pymysql

# 获取数据库连接
db = pymysql.connect("localhost", "root", "123456", "python_test")
# 获取数据库操作的游标
cursor = db.cursor()
# SQL语句
sql = "select * from user"

try:
    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        uid = row[0]
        uname = row[1]
        upassword = row[2]
        print(uid, uname, upassword)
        print("uid=%s,uname=%s,upassword=%s" % (uid, uname, upassword))
        print("-------------------")
except:
    print("Error:unable to fetch data")

#     关闭数据库连接
db.close()
