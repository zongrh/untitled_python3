"""插入数据"""
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "python_test")
# 使用cursor()方法获取 数据库操作游标
cursor = db.cursor()
# SQL 插入语句
sql = "insert into EMPLOYEE(first_name," \
      "last_name,age,sex,income)" \
      "values ('%s','%s','%d','%c','%d')" % \
      ('mac4', 'mouse', 20, 'M', 2000)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
