#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, 
 wxID_DIALOG1WINDOW1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(43, 345), size=wx.Size(400, 374),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Trade Message')
        self.SetClientSize(wx.Size(392, 347))

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Next',
              name='button1', parent=self, pos=wx.Point(24, 312),
              size=wx.Size(75, 23), style=0)
        self.button1.SetDefault()

        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Back',
              name='button2', parent=self, pos=wx.Point(160, 312),
              size=wx.Size(75, 23), style=0)

        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=u'Cancel',
              name='button3', parent=self, pos=wx.Point(296, 312),
              size=wx.Size(75, 23), style=0)

        self.window1 = wx.Window(id=wxID_DIALOG1WINDOW1, name='window1',
              parent=self, pos=wx.Point(24, 16), size=wx.Size(352, 280),
              style=0)
        self.tag_window = Panel2(self)
        self.window1.AddChild(self.tag_window)
        
    def __init__(self, parent):
        self._init_ctrls(parent)
#Boa:FramePanel:Panel2

import wx.lib.masked.numctrl
import wx.lib.intctrl

[wxID_PANEL2, wxID_PANEL2DATEPICKERCTRL1, wxID_PANEL2DATEPICKERCTRL2, 
 wxID_PANEL2DATEPICKERCTRL3, wxID_PANEL2INTCTRL1, wxID_PANEL2NUMCTRL1, 
 wxID_PANEL2STATICTEXT1, wxID_PANEL2STATICTEXT2, wxID_PANEL2STATICTEXT3, 
 wxID_PANEL2STATICTEXT4, wxID_PANEL2STATICTEXT5, wxID_PANEL2STATICTEXT6, 
 wxID_PANEL2STATICTEXT7, wxID_PANEL2TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(14)]

class Panel2(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_PANEL2, name='', parent=prnt,
              pos=wx.Point(47, 319), size=wx.Size(321, 250),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(313, 223))

        self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL2TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(168, 88), size=wx.Size(128, 21),
              style=0, value='textCtrl1')

        self.staticText1 = wx.StaticText(id=wxID_PANEL2STATICTEXT1,
              label=u'Price', name='staticText1', parent=self, pos=wx.Point(24,
              24), size=wx.Size(127, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PANEL2STATICTEXT2,
              label=u'Quantity', name='staticText2', parent=self,
              pos=wx.Point(24, 48), size=wx.Size(130, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PANEL2STATICTEXT3,
              label=u'Transaction Time/Date', name='staticText3', parent=self,
              pos=wx.Point(24, 72), size=wx.Size(124, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_PANEL2STATICTEXT4,
              label=u'Symbol', name='staticText4', parent=self, pos=wx.Point(24,
              96), size=wx.Size(122, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_PANEL2STATICTEXT5,
              label=u'Maturity Date', name='staticText5', parent=self,
              pos=wx.Point(24, 128), size=wx.Size(122, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_PANEL2STATICTEXT6,
              label=u'Effective Date', name='staticText6', parent=self,
              pos=wx.Point(24, 160), size=wx.Size(125, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_PANEL2STATICTEXT7,
              label=u'Cash Flow Alignment Date', name='staticText7',
              parent=self, pos=wx.Point(24, 192), size=wx.Size(125, 13),
              style=0)

        self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_PANEL2INTCTRL1,
              limited=False, max=None, min=None, name='intCtrl1',
              oob_color=wx.RED, parent=self, pos=wx.Point(168, 48),
              size=wx.Size(128, 21), style=0, value=0)

        self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_PANEL2NUMCTRL1,
              name='numCtrl1', parent=self, pos=wx.Point(168, 16),
              size=wx.Size(128, 22), style=0, value=0)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_PANEL2DATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(168, 120),
              size=wx.Size(128, 21), style=wx.DP_SHOWCENTURY)

        self.datePickerCtrl2 = wx.DatePickerCtrl(id=wxID_PANEL2DATEPICKERCTRL2,
              name='datePickerCtrl2', parent=self, pos=wx.Point(168, 152),
              size=wx.Size(128, 21), style=wx.DP_SHOWCENTURY)

        self.datePickerCtrl3 = wx.DatePickerCtrl(id=wxID_PANEL2DATEPICKERCTRL3,
              name='datePickerCtrl3', parent=self, pos=wx.Point(168, 192),
              size=wx.Size(128, 21), style=wx.DP_SHOWCENTURY)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
