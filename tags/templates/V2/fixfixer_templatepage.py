# various pages for templates and repeating groups


import wx

class MarketDataPage(wx.Window):
    def __init__(parent):
        self.scrolledWindow1 = wx.ScrolledWindow(id=1,
              name='scrolledWindow1', parent=parent, pos=wx.Point(0, 0),
              size=wx.Size(336, 214), style=wx.HSCROLL | wx.VSCROLL)

        self.staticText2 = wx.StaticText(id=2,
              label=u'Entry Action', name='staticText2',
              parent=self.scrolledWindow1, pos=wx.Point(0, 16), size=wx.Size(59,
              13), style=0)

        self.choice1 = wx.Choice(choices=['New', 'Change', 'Delete'],
              id=3, name='choice1', parent=self.scrolledWindow1,
              pos=wx.Point(80, 8), size=wx.Size(130, 21), style=0)
        self.choice1.SetLabel(u'')

        self.choice2 = wx.Choice(choices=['Bid', 'Ask', 'Trade', 'Empy Book'],
              id=4, name='choice2', parent=self.scrolledWindow1,
              pos=wx.Point(80, 40), size=wx.Size(136, 21), style=0)

        self.staticText3 = wx.StaticText(id=5,
              label=u'Entry Type', name='staticText3',
              parent=self.scrolledWindow1, pos=wx.Point(0, 40), size=wx.Size(53,
              13), style=0)

        self.staticText4 = wx.StaticText(id=6,
              label=u'Entry Price', name='staticText4',
              parent=self.scrolledWindow1, pos=wx.Point(0, 72), size=wx.Size(56,
              13), style=0)

        self.staticText5 = wx.StaticText(id=7,
              label=u'Entry Quantity', name='staticText5',
              parent=self.scrolledWindow1, pos=wx.Point(0, 104),
              size=wx.Size(71, 16), style=0)

        self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=8,
              name='numCtrl1', parent=self.scrolledWindow1, pos=wx.Point(80,
              72), size=wx.Size(99, 22), style=0, value=0)
        self.numCtrl1.SetAllowNegative(False)
        self.numCtrl1.SetDefaultValue(u'0.0')
        self.numCtrl1.SetHelpText(u'Price for security')

        self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=9,
              limited=False, max=None, min=None, name='intCtrl1',
              oob_color=wx.RED, parent=self.scrolledWindow1, pos=wx.Point(80,
              104), size=wx.Size(132, 21), style=0, value=0)

        self.staticText6 = wx.StaticText(id=10,
              label=u'Security', name='staticText6',
              parent=self.scrolledWindow1, pos=wx.Point(0, 136),
              size=wx.Size(39, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=11, name='textCtrl1',
              parent=self.scrolledWindow1, pos=wx.Point(80, 136),
              size=wx.Size(100, 21), style=0, value=u'Tag 55')
