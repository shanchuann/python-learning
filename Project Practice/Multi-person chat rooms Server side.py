import wx
from socket import socket
import threading
from concurrent.futures import ThreadPoolExecutor

class Server(wx.Frame):
    def __init__(self):
        # 实例属性
        self.isOn = False  # 是否开启服务
        # 创建socket对象
        self.server_socket = socket()
        # 绑定地址,端口
        self.server_socket.bind(('0.0.0.0', 8999))
        # 设置监听
        self.server_socket.listen(5)

        # 保存所有的客户端
        self.client_thread_dict = {}
        # 创建线程池,最大线程数为5
        self.pool = ThreadPoolExecutor(5)

        # 界面布局
        # 调用父类init
        wx.Frame.__init__(self, None, title='聊天室服务器端', size=(450, 600), pos=(0, 50))
        # 创建面板
        self.pl = wx.Panel(self)

        # 创建按钮
        # 开启服务
        self.start_server_btn = wx.Button(self.pl, label='开启服务器', pos=(10, 10), size=(200, 40))
        self.save_text_btn = wx.Button(self.pl, label='保存聊天记录', pos=(220, 10), size=(200, 40))

        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.pl, pos=(10, 60), size=(410, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.start_server, self.start_server_btn)
        self.Bind(wx.EVT_BUTTON, self.save_text, self.save_text_btn)

    # 启动服务器
    def start_server(self, event):
        if not self.isOn:
            self.isOn = True
            # 创建线程
            main_thread = threading.Thread(target=self.main_thread_fun)
            # 设置为守护线程
            main_thread.daemon = True
            # 启动线程
            main_thread.start()

    def main_thread_fun(self):
        # 创建线程池
        while self.isOn:
            client_socket, client_addr = self.server_socket.accept()
            print(client_addr)
            client_name = client_socket.recv(1024).decode('utf-8')
            print(client_name)
            # 创建客户端线程
            client_thread = ClientThread(client_socket, client_name, self)
            # 保存客户端
            self.client_thread_dict[client_name] = client_thread
            # 启动线程
            self.pool.submit(client_thread.run)
            self.send(client_name + '加入聊天室')

    # 发送消息
    def send(self, text):
        self.text.AppendText(text + '\n')
        for client in self.client_thread_dict.values():
            if client.isOn:
                client.client_socket.send(text.encode('utf-8'))

    # 保存聊天记录
    def save_text(self, event):
        with open('./聊天记录.txt', 'a+', encoding='utf-8') as f:
            f.write(self.text.GetValue())

class ClientThread(threading.Thread):
    def __init__(self, socket, name, server):
        threading.Thread.__init__(self)
        self.text = None
        self.client_socket = socket
        self.client_name = name
        self.server = server
        self.isOn = True

    def run(self):
        while self.isOn:
            text = self.client_socket.recv(1024).decode('utf-8')
            if text == '断开链接':
                self.isOn = False
                self.server.send(self.client_name + '离开聊天室')
            else:
                self.server.send(self.client_name + ':' + text)
        self.client_socket.close()

# 入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建服务器窗口
    server = Server()
    # 显示窗口
    server.Show()
    # 进入主事件循环
    app.MainLoop()