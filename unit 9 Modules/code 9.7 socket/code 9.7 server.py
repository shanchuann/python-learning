import socket
# 创建一个socket对象
sk = socket.socket()
# 绑定IP和端口
sk.bind(('0.0.0.0', 8995))
# 监听
sk.listen(5)
# 等待连接
conn, addr = sk.accept()

print(addr)
print(conn)

while True:
    accept_data = conn.recv(1024)
    print("接收到的数据：", accept_data.decode('utf-8'))
    send_data = "服务器已经收到了你发送的数据"
    conn.send(send_data.encode('utf-8'))