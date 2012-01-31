#Boa:Dialog:Body1
# Body information for Market Data refresh message

import wx
import wx.lib.intctrl
import wx.lib.masked.numctrl
from wx.lib.anchors import LayoutAnchors
from copy import deepcopy

def create(parent):
    return Body1(parent)

[wxID_BODY1, wxID_BODY1BUTTON1, wxID_BODY1BUTTON2, wxID_BODY1CHOICE1, 
 wxID_BODY1CHOICE2, wxID_BODY1INTCTRL1, wxID_BODY1NOTEBOOK1, 
 wxID_BODY1NUMCTRL1, wxID_BODY1SCROLLEDWINDOW1, wxID_BODY1SPINCTRL1, 
 wxID_BODY1STATICTEXT1, wxID_BODY1STATICTEXT2, wxID_BODY1STATICTEXT3, 
 wxID_BODY1STATICTEXT4, wxID_BODY1STATICTEXT5, wxID_BODY1STATICTEXT6, 
 wxID_BODY1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(17)]

class Body1(wx.Dialog):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.scrolledWindow1, select=True,
              text=u'Data 1')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_BODY1, name=u'Body1', parent=prnt,
              pos=wx.Point(824, 452), size=wx.Size(395, 381),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Body')
        self.SetClientSize(wx.Size(387, 354))

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_BODY1SPINCTRL1, initial=0, max=100,
              min=0, name='spinCtrl1', parent=self, pos=wx.Point(144, 24),
              size=wx.Size(117, 21), style=wx.SP_ARROW_KEYS)
        self.spinCtrl1.SetValue(1)
        self.spinCtrl1.SetRange(1, 10)
        self.spinCtrl1.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl1TextEnter,
              id=wxID_BODY1SPINCTRL1)
        self.spinCtrl1.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl1Spinctrl,
              id=wxID_BODY1SPINCTRL1)

        self.button1 = wx.Button(id=wxID_BODY1BUTTON1, label=u'Next',
              name='button1', parent=self, pos=wx.Point(8, 320),
              size=wx.Size(75, 23), style=0)
        self.button1.SetDefault()
        self.button1.SetConstraints(LayoutAnchors(self.button1, True, True,
              False, False))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_BODY1BUTTON1)

        self.button2 = wx.Button(id=wxID_BODY1BUTTON2, label=u'Cancel',
              name='button2', parent=self, pos=wx.Point(304, 320),
              size=wx.Size(72, 24), style=0)
        self.button2.SetConstraints(LayoutAnchors(self.button2, True, True,
              False, False))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_BODY1BUTTON2)

        self.staticText1 = wx.StaticText(id=wxID_BODY1STATICTEXT1,
              label=u'Number of Market Data', name='staticText1', parent=self,
              pos=wx.Point(24, 32), size=wx.Size(112, 13), style=0)

        self.notebook1 = wx.Notebook(id=wxID_BODY1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(16, 72), size=wx.Size(344, 240),
              style=0)
        self.notebook1.SetFitToCurrentPage(False)

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_BODY1SCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(336, 214), style=wx.HSCROLL | wx.VSCROLL)

        self.staticText2 = wx.StaticText(id=wxID_BODY1STATICTEXT2,
              label=u'Entry Action', name='staticText2',
              parent=self.scrolledWindow1, pos=wx.Point(0, 16), size=wx.Size(59,
              13), style=0)

        self.choice1 = wx.Choice(choices=['New', 'Change', 'Delete'],
              id=wxID_BODY1CHOICE1, name='choice1', parent=self.scrolledWindow1,
              pos=wx.Point(80, 8), size=wx.Size(130, 21), style=0)
        self.choice1.SetLabel(u'')

        self.choice2 = wx.Choice(choices=['Bid', 'Ask', 'Trade', 'Empy Book'],
              id=wxID_BODY1CHOICE2, name='choice2', parent=self.scrolledWindow1,
              pos=wx.Point(80, 40), size=wx.Size(136, 21), style=0)

        self.staticText3 = wx.StaticText(id=wxID_BODY1STATICTEXT3,
              label=u'Entry Type', name='staticText3',
              parent=self.scrolledWindow1, pos=wx.Point(0, 40), size=wx.Size(53,
              13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_BODY1STATICTEXT4,
              label=u'Entry Price', name='staticText4',
              parent=self.scrolledWindow1, pos=wx.Point(0, 72), size=wx.Size(56,
              13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_BODY1STATICTEXT5,
              label=u'Entry Quantity', name='staticText5',
              parent=self.scrolledWindow1, pos=wx.Point(0, 104),
              size=wx.Size(71, 16), style=0)

        self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_BODY1NUMCTRL1,
              name='numCtrl1', parent=self.scrolledWindow1, pos=wx.Point(80,
              72), size=wx.Size(99, 22), style=0, value=0)
        self.numCtrl1.SetAllowNegative(False)
        self.numCtrl1.SetDefaultValue(u'0.0')
        self.numCtrl1.SetHelpText(u'Price for security')

        self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_BODY1INTCTRL1,
              limited=False, max=None, min=None, name='intCtrl1',
              oob_color=wx.RED, parent=self.scrolledWindow1, pos=wx.Point(80,
              104), size=wx.Size(132, 21), style=0, value=0)

        self.staticText6 = wx.StaticText(id=wxID_BODY1STATICTEXT6,
              label=u'Security', name='staticText6',
              parent=self.scrolledWindow1, pos=wx.Point(0, 136),
              size=wx.Size(39, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_BODY1TEXTCTRL1, name='textCtrl1',
              parent=self.scrolledWindow1, pos=wx.Point(80, 136),
              size=wx.Size(100, 21), style=0, value=u'Tag 55')

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnSpinCtrl1TextEnter(self, event):
        event.Skip()
        

    def OnSpinCtrl1Spinctrl(self, event):
        data_page = self.notebook1.GetCurrentPage()
        new_page = data_page
        self.notebook1.DeleteAllPages()
        for i in range(self.spinCtrl1.GetValue()):
            page_name = "Data " + str(i)
            self.notebook1.AddPage(imageId=-1, page=self.scrolledWindow1, select=True,text=page_name)
        
 
    def OnButton1Button(self, event):
        self.EndModal(1)

    def OnButton2Button(self, event):
        self.EndModal(2)
