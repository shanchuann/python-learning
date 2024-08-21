import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, title='simple calculator', pos = (400,100),size = (465,590))
        self.pl = wx.Panel(self,pos = (0,0),size = (465,590))
        self.entry = wx.TextCtrl(self.pl, pos = (10,10),size = (430,80),style = wx.TE_RIGHT)
        self.btn_1 = wx.Button(self.pl,label = '1',pos = (10,100),size = (100,100))
        self.btn_2 = wx.Button(self.pl,label = '2',pos = (120,100),size = (100,100))
        self.btn_3 = wx.Button(self.pl,label = '3',pos = (230,100),size = (100,100))
        self.btn_4 = wx.Button(self.pl,label = '4',pos = (10,210),size = (100,100))
        self.btn_5 = wx.Button(self.pl,label = '5',pos = (120,210),size = (100,100))
        self.btn_6 = wx.Button(self.pl,label = '6',pos = (230,210),size = (100,100))
        self.btn_7 = wx.Button(self.pl,label = '7',pos = (10,320),size = (100,100))
        self.btn_8 = wx.Button(self.pl,label = '8',pos = (120,320),size = (100,100))
        self.btn_9 = wx.Button(self.pl,label = '9',pos = (230,320),size = (100,100))
        self.btn_0 = wx.Button(self.pl,label = '0',pos = (120,430),size = (100,100))
        self.btn_plus = wx.Button(self.pl,label = '+',pos = (340,100),size = (100,100))
        self.btn_minus = wx.Button(self.pl,label = '-',pos = (340,210),size = (100,100))
        self.btn_multiply = wx.Button(self.pl,label = '*',pos = (340,320),size = (100,100))
        self.btn_divide = wx.Button(self.pl,label = '/',pos = (340,430),size = (100,100))
        self.btn_equal = wx.Button(self.pl,label = '=',pos = (230,430),size = (100,100))
        self.btn_clear = wx.Button(self.pl,label = 'C',pos = (10,430),size = (100,100))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_1)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_2)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_3)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_4)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_5)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_6)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_7)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_8)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_9)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_0)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_plus)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_minus)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_multiply)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_divide)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_equal)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.btn_clear)
        self.equation = ''
    def OnClick(self,event):
        label = event.GetEventObject().GetLabel()
        if label == '=':
            try:
                result = eval(self.equation)
                self.entry.SetValue(str(result))
            except:
                self.entry.SetValue('error')
        elif label == 'C':
            self.entry.SetValue('')
            self.equation = ''
        else:
            self.equation += label
            self.entry.SetValue(self.equation)


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame()
    frm.Show()
    app.MainLoop()