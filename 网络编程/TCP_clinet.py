# -*- coding: utf-8 -*-
# @Author       :   Zhongwj
# @DATE         :2020/7/20  10:38 
# @Version      :
# @Description  :

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
while True:
    s.send('中文'.encode())
    print(s.recv(1024).decode('utf-8'))
    if s.recv(1024).decode('utf-8') =='':
        break

s.send(b'exit')
s.close()