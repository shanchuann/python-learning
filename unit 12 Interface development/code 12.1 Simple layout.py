import wx

def onClick(event):
    staticText.SetLabel('You clicked the button!')
# 创建一个应用程序对象
app = wx.App()
# 创建一个窗口 size:宽,高 pos:左上角坐标 title:标题
frm = wx.Frame(None,size = (600,500),pos = (400,100),title = 'Simple layout')
# 显示窗口
frm.Show()
# 创建面板
pl = wx.Panel(frm,size = (600,500),pos = (0,0))
# 显示面板
pl.Show()
# 创建一个静态文本
staticText = wx.StaticText(pl,label = 'Hello World!',pos = (250,200))
# 显示静态文本
staticText.Show()
# 创建一个按钮
btn = wx.Button(pl,label = 'OK',pos = (250,250))
# 显示按钮
btn.Show()
# 绑定事件
frm.Bind(wx.EVT_BUTTON,onClick,btn)
# 进入主事件循环
app.MainLoop()