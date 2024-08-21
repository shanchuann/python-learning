import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Hello, World', size=(300, 200))
        pl = wx.Panel(self)
        staticText = wx.StaticText(pl, label='Hello, World!', pos=(100, 50))
        btn = wx.Button(pl, label='Ok', pos=(100, 100))
# 创建应用程序对象
app = wx.App()
# 创建窗口
frm = MyFrame()
# 显示窗口
frm.Show()

# 窗口一直显示
app.MainLoop()