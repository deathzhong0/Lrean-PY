#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  # 转换，忽视错误

print(len('wo'))  # str 多少字节

print(len(b'ABC'))  # bytes  多少字节 #

print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

print(len('中文'.encode('utf-8')))  # utf-8  多少字节

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
