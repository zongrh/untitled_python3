"""网络编程"""
import socket

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
print(host)
port = 9998
# 绑定端口号
serversocket.bind((host, port))
# 设置对打连接数
serversocket.listen(5)
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    print("连接地址：%s" % str(addr))
    msg = "欢迎访问菜鸟教程" + "\r\n"
    clientsocket.send(msg.encode("utf-8"))
    clientsocket.close()
