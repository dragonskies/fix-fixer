#Boa:FramePanel:Panel1

import wx
import wx.lib.masked.numctrl

[wxID_PANEL1, wxID_PANEL1CHOICE1, wxID_PANEL1DATEPICKERCTRL1, 
 wxID_PANEL1NUMCTRL1, wxID_PANEL1STATICTEXT1, wxID_PANEL1STATICTEXT2, 
 wxID_PANEL1STATICTEXT3, wxID_PANEL1STATICTEXT4, wxID_PANEL1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Panel1(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_PANEL1, name='', parent=prnt,
              pos=wx.Point(606, 566), size=wx.Size(253, 178),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(245, 151))

        self.staticText1 = wx.StaticText(id=wxID_PANEL1STATICTEXT1,
              label=u'Leg Symbol', name='staticText1', parent=self,
              pos=wx.Point(40, 24), size=wx.Size(54, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2,
              label=u'Leg Currency', name='staticText2', parent=self,
              pos=wx.Point(32, 56), size=wx.Size(64, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3,
              label=u'Leg Issue Date', name='staticText3', parent=self,
              pos=wx.Point(24, 88), size=wx.Size(72, 16), style=0)

        self.choice1 = wx.Choice(choices=[], id=wxID_PANEL1CHOICE1,
              name='choice1', parent=self, pos=wx.Point(104, 16),
              size=wx.Size(130, 21), style=0)
        self.choice1.SetStringSelection(u'FIX\nFLOAT')

        self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(104, 48), size=wx.Size(128, 21),
              style=0, value='textCtrl1')

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_PANEL1DATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(104, 80),
              size=wx.Size(128, 21), style=wx.DP_SHOWCENTURY)

        self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_PANEL1NUMCTRL1,
              name='numCtrl1', parent=self, pos=wx.Point(104, 112),
              size=wx.Size(128, 22), style=0, value=0)

        self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4,
              label=u'Leg Purchase Rate', name='staticText4', parent=self,
              pos=wx.Point(8, 120), size=wx.Size(90, 13), style=0)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
