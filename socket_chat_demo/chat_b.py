# -*- coding: utf-8 -*-
import socket
Sockin = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sockin.bind(('192.168.199.124',23000))

while True:
    msg,(addr,port) = Sockin.recvfrom(100)
    if msg == 'q':
        Sockin.close()
        break
    else:
        print msg

    text = raw_input('> ')
    Sockin.sendto(text,(('192.168.199.134',23000)))
    if text =='q':
        Sockin.close()
        break
