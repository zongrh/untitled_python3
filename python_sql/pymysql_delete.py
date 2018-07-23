"""删除操作"""
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "python_test")
# 获取数据库操作的游标
cursor = db.cursor()
# sql 删除语句
sql = "delete from user where uname='%s'" % ('zhangsan')
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 事务回滚
    db.rollback()
# 关闭连接
db.close()
