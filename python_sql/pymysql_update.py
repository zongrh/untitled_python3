"""数据库更新操作"""
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "python_test")
# 使用cursor()方法获取数据库操作游标
cursor = db.cursor()
# sql更新语句
sql = "update Employee set age=age+5 where sex ='%c'" % ('M')
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
