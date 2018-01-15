# -*- coding: utf-8 -*-
import socket
 
Sockin = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #新建socket
Sockin.bind(('192.168.199.134',23000))   #socket绑定该主机的ip和端口

while True:             #循环中执行收发功能
    text = raw_input('> ')
    Sockin.sendto(text,(('192.168.199.124',23000)))     #将 'text’ 发送给对方
    if text == 'q':
        Scokin.close()  #退出时关闭socket
        break
    msg,(addr,port) = Sockin.recvfrom(100)    # 接受数据
    if msg == 'q':
        Sockin.close()
        break
    print msg
