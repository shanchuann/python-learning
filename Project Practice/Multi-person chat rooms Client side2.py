import wx
from socket import *
import threading

class Client(wx.Frame):
    # 构造方法
    def __init__(self):
        # 实例属性
        self.name = 'bunianjiu'  # 用户名
        self.isConnented = False  # 是否连接
        self.client_socket = None

        # 界面布局
        wx.Frame.__init__(self, None,title = self.name + '聊天室客户端', size=(450, 680),pos =(100,100))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 加入聊天室
        self.conn_btn = wx.Button(self.pl, label='加入聊天室', pos=(10, 10), size=(200, 40))
        # 离开聊天室
        self.dis_conn_btn = wx.Button(self.pl, label='离开聊天室', pos=(220, 10), size=(200, 40))
        # 清空按钮
        self.clear_btn = wx.Button(self.pl, label='清空', pos=(10, 580), size=(200, 40))
        # 发送按钮
        self.send_btn = wx.Button(self.pl, label='发送', pos=(220, 580), size=(200, 40))
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.pl, pos=(10, 60), size=(410, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 创建消息输入框
        self.input_text = wx.TextCtrl(self.pl, pos=(10, 470), size=(410, 100), style=wx.TE_MULTILINE)

        # 绑定事件
        self.Bind(wx.EVT_BUTTON,self.clear,self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.conn, self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.dis_conn, self.dis_conn_btn)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)

    # 加入聊天室
    def conn(self,event):
        if self.isConnented == False:
            self.isConnented = True
            # 创建socket对象
            self.client_socket = socket()
            # 连接服务器
            self.client_socket.connect(('127.0.0.1',8999))

            self.client_socket.send(self.name.encode('utf-8'))

            # 创建线程
            main_thread = threading.Thread(target = self.recv_data)
            # 设置为守护线程
            main_thread.daemon = True
            # 启动线程
            main_thread.start()

    # 接收数据
    def recv_data(self):
        while self.isConnented:
            text = self.client_socket.recv(1024).decode('utf-8')
            self.text.AppendText(text + '\n')

    # 离开聊天室
    def dis_conn(self,event):
        self.client_socket.send('断开链接'.encode('utf-8'))
        self.isConnented = False

    # 清空消息
    def clear(self,event):
        self.text.Clear()

    # 发送消息
    def send(self,event):
        if self.isConnented:
            text = self.input_text.GetValue()
            if text != '':
                self.client_socket.send(text.encode('utf-8'))
                self.input_text.Clear()

# 程序入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建客户端窗口
    client = Client()
    # 显示窗口
    client.Show()
    # 进入主事件循环
    app.MainLoop()
