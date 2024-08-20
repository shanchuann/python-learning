import socket

# 创建一个socket对象
sk = socket.socket()
# 链接服务器
sk.connect(('127.0.0.1', 8995))

while True:
    send_data = input('请输入发送的内容：')
    # 发送数据
    sk.send(send_data.encode('utf-8'))
    # 接收数据
    data = sk.recv(1024)
    print(data.decode('utf-8'))