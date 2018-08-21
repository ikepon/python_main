# coding: utf-8
# 必要なモジュールの読込み
import socket

# 通信先(サーバー)の情報
host = '127.0.0.1'
port = 8001

# サービスの準備
sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
sSock.bind((host, port))
sSock.listen()

# 接続の受け付け
print('Waiting for connection...')
(cSock, cAddr) = sSock.accept()
print('Connection accepted!: ', cAddr)

# クライアントから受信
r = cSock.recv(4096)
print('クライアントから> ', r.decode('utf-8') )

# クライアントへ送信
msg = 'はい，届いていますよ.'.encode('utf-8')
cSock.send(msg)

# ソケットを終了する
cSock.close()
sSock.close()
