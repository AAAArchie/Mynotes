# !/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8000))
client.send(b'i want you')
reply = client.recv(1024)
print('收到服务端回复：', reply)
client.close()
