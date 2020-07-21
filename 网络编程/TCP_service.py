# -*- coding: utf-8 -*-
# @Author       :   Zhongwj
# @DATE         :2020/7/20  9:41 
# @Version      :
# @Description  :

import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('starting service...')

def tcplink(sock,addr):
    print('Accpet new connection from %s %s ...' % addr)
    sock.send(b'Welcome,connection complete!')
    try:
        while True:

            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            sock.send(('Hello ,%s!' %data.decode('utf-8')).encode('utf-8'))
            print('Connection from %s:%s closed' %addr)
    except ConnectionResetError:
        print('Connection is over!')
    except ConnectionAbortedError:
        print('ww')

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
