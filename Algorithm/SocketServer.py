# !/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 80))  # 注意：请使用80端口
server.listen(5)
# 阻塞，等待客户端连接
conn, address = server.accept()
# 接收到客户端发送的数据
data = conn.recv(1024)
# 给客户端回复数据
tpl = "<h1>高清无码</h1> <div style='color:red'>震惊了，Alex居然...</div> <a href='http://www.pythonav.com'>臭妹妹</a>"
conn.send(tpl.encode('gbk'))
# 关闭与客户端的链接
conn.close()
server.close()
