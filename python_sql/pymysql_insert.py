"""
插入数据
"""
import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", db="python_test", port=3306)

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
