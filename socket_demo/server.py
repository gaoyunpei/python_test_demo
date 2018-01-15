# -*- coding: utf-8 -*-
# 导入 socket、sys 模块
import socket

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
# 单个主机开两个终端
host = socket.gethostname()

port = 9999

print host
# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
    
    msg='欢迎访问高允沛的服务器！'+ "\r\n"
#    clientsocket.send(msg.encode('utf-8'))
    clientsocket.send(msg)
    clientsocket.close()
