#Boa:FramePanel:Panel1

import wx
import wx.lib.intctrl
import wx.lib.masked.numctrl

[wxID_PANEL1, wxID_PANEL1CHOICE1, wxID_PANEL1CHOICE2, wxID_PANEL1INTCTRL1, 
 wxID_PANEL1NUMCTRL1, wxID_PANEL1SCROLLEDWINDOW1, wxID_PANEL1STATICTEXT2, 
 wxID_PANEL1STATICTEXT3, wxID_PANEL1STATICTEXT4, wxID_PANEL1STATICTEXT5, 
 wxID_PANEL1STATICTEXT6, wxID_PANEL1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Panel1(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_PANEL1, name='', parent=prnt,
              pos=wx.Point(724, 380), size=wx.Size(308, 205),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(300, 178))

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_PANEL1SCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(336, 214), style=wx.HSCROLL | wx.VSCROLL)

        self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_PANEL1NUMCTRL1,
              name='numCtrl1', parent=self.scrolledWindow1, pos=wx.Point(80,
              72), size=wx.Size(99, 22), style=0, value=0)
        self.numCtrl1.SetAllowNegative(False)
        self.numCtrl1.SetDefaultValue(u'0.0')
        self.numCtrl1.SetHelpText(u'Price for security')

        self.staticText6 = wx.StaticText(id=wxID_PANEL1STATICTEXT6,
              label=u'Security', name='staticText6',
              parent=self.scrolledWindow1, pos=wx.Point(0, 136),
              size=wx.Size(39, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4,
              label=u'Entry Price', name='staticText4',
              parent=self.scrolledWindow1, pos=wx.Point(0, 72), size=wx.Size(56,
              13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_PANEL1STATICTEXT5,
              label=u'Entry Quantity', name='staticText5',
              parent=self.scrolledWindow1, pos=wx.Point(0, 104),
              size=wx.Size(71, 16), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2,
              label=u'Entry Action', name='staticText2',
              parent=self.scrolledWindow1, pos=wx.Point(0, 16), size=wx.Size(59,
              13), style=0)

        self.choice1 = wx.Choice(choices=['New', 'Change', 'Delete'],
              id=wxID_PANEL1CHOICE1, name='choice1',
              parent=self.scrolledWindow1, pos=wx.Point(80, 8),
              size=wx.Size(130, 21), style=0)
        self.choice1.SetLabel(u'')

        self.choice2 = wx.Choice(choices=['Bid', 'Ask', 'Trade', 'Empy Book'],
              id=wxID_PANEL1CHOICE2, name='choice2',
              parent=self.scrolledWindow1, pos=wx.Point(80, 40),
              size=wx.Size(136, 21), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3,
              label=u'Entry Type', name='staticText3',
              parent=self.scrolledWindow1, pos=wx.Point(0, 40), size=wx.Size(53,
              13), style=0)

        self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_PANEL1INTCTRL1,
              limited=False, max=None, min=None, name='intCtrl1',
              oob_color=wx.RED, parent=self.scrolledWindow1, pos=wx.Point(80,
              104), size=wx.Size(132, 21), style=0, value=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL1, name='textCtrl1',
              parent=self.scrolledWindow1, pos=wx.Point(80, 136),
              size=wx.Size(100, 21), style=0, value=u'Tag 55')

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
