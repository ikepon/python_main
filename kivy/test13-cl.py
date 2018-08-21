# coding: utf-8

# 必要なモジュールの読込み
import socket

# 通信先(サーバー)の情報
host = '127.0.0.1'
port = 8001

# 接続処理
cSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSock.settimeout(3.0)
print('Connecting...')
cSock.connect((host, port))
print('Connection accepted!')

# サーバーへの送信
msg = '受信できていますか?'.encode('utf-8')
cSock.send(msg)

# サーバーから受信
r = cSock.recv(4096)
print('サーバーから> ', r.decode('utf-8'))

# ソケットを終了する
cSock.close()
