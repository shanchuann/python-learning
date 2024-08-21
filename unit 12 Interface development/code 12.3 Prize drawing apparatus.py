import wx
import random
class MyFrame(wx.Frame):
    NameList = ['Tom', 'Jerry', 'Mike', 'John', 'Lily', 'Lucy', 'Jack', 'Rose', 'David', 'Bob']
    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self, None, title='Prize drawing apparatus', pos = (100,100),size=(400,600))
        # 创建面板
        self.pl = wx.Panel(self,pos = (0,0),size=(400,600))
        # 设置背景颜色
        self.pl.SetBackgroundColour(wx.WHITE)
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl, label=random.choice(self.NameList) , pos=(0,50), size=(400,400), style=wx.TE_CENTER)
        # 设置字体
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.staticText.SetFont(font)
        # 创建按钮
        self.btn1 = wx.Button(self.pl, label='Begin', pos=(120,500))
        self.btn2 = wx.Button(self.pl, label='End', pos=(200,500))
        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.StopClick, self.btn2)

    def OnClick(self, event):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_name, self.timer)
        self.timer.Start(100)

    def update_name(self, event):
        self.staticText.SetLabel(random.choice(self.NameList))

    def StopClick(self, event):
        self.timer.Stop()
        self.timer.Destroy()  # 释放定时器对象
        self.timer = None

if __name__ == "__main__":
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()

    # 窗口一直显示
    app.MainLoop()