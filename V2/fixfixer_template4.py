#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, 
 wxID_DIALOG1NOTEBOOK1, wxID_DIALOG1SPINCTRL1, wxID_DIALOG1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog1(wx.Dialog):
 
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit
        new_page = Panel1(parent, 11, "Page 1" )
        parent.AddPage(imageId=-1, page=new_page, select=True, text=u'Security 1')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(386, 441), size=wx.Size(350,400),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Security Definition')
        #self.SetClientSize(wx.Size(298, 241))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'Number of definitions', name='staticText1', parent=self,
              pos=wx.Point(8, 16), size=wx.Size(102, 13), style=0)

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_DIALOG1SPINCTRL1, initial=0,
              max=100, min=0, name='spinCtrl1', parent=self, pos=wx.Point(120,
              8), size=wx.Size(117, 21), style=wx.SP_ARROW_KEYS)
        self.spinCtrl1.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl1TextEnter,
            id=wxID_DIALOG1SPINCTRL1)
        self.spinCtrl1.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl1Spinctrl,
            id=wxID_DIALOG1SPINCTRL1)

        self.notebook1 = wx.Notebook(id=wxID_DIALOG1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(16, 40), size=wx.Size(264, 300),
              style=0)

        self.button1 = wx.Button(id=wx.ID_OK, label=u'Next', name='button1',
              parent=self, pos=wx.Point(8,358), size=wx.Size(75, 23), style=0)
        self.button1.SetDefault()

        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Previous',
              name='button2', parent=self, pos=wx.Point(104, 358),
              size=wx.Size(75, 23), style=0)

        self.button3 = wx.Button(id=wx.ID_CANCEL, label=u'Cancel',
              name='button3', parent=self, pos=wx.Point(200, 358),
              size=wx.Size(75, 23), style=0)
        
        self.notebook1.SetFitToCurrentPage(False)

        self._init_coll_notebook1_Pages(self.notebook1)
        
    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnSpinCtrl1TextEnter(self,event):
        event.Skip()
    
    def OnSpinCtrl1Spinctrl(self, event):
        event.Skip()
        
#Boa:FramePanel:Panel1

import wx
import wx.lib.masked.numctrl

[wxID_PANEL1, wxID_PANEL1DATEPICKERCTRL1, wxID_PANEL1NUMCTRL1, 
 wxID_PANEL1STATICTEXT1, wxID_PANEL1STATICTEXT2, wxID_PANEL1STATICTEXT3, 
 wxID_PANEL1STATICTEXT4, wxID_PANEL1STATICTEXT5, wxID_PANEL1STATICTEXT6, 
 wxID_PANEL1STATICTEXT7, wxID_PANEL1STATICTEXT8, wxID_PANEL1TEXTCTRL1, 
 wxID_PANEL1TEXTCTRL2, wxID_PANEL1TEXTCTRL3, wxID_PANEL1TEXTCTRL4, 
 wxID_PANEL1TEXTCTRL5, wxID_PANEL1TEXTCTRL6, wxID_PANEL1SCROLLEDWINDOW1 
] = [wx.NewId() for _init_ctrls in range(18)]


class Panel1(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_PANEL1, name='', parent=prnt,
              pos=wx.Point(1009, 395), size=wx.Size(305, 341),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(297, 314))

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_PANEL1SCROLLEDWINDOW1,
            name='scrolledWindow1', parent=self, pos=wx.Point(0, 0),
            size=wx.Size(336, 214), style=wx.HSCROLL | wx.VSCROLL)

        self.staticText1 = wx.StaticText(id=wxID_PANEL1STATICTEXT1,
              label=u'Symbol', name='staticText1', parent=self.scrolledWindow1, pos=wx.Point(24,
              32), size=wx.Size(72, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2,
              label=u'Security Group', name='staticText2', parent=self.scrolledWindow1,
              pos=wx.Point(24, 64), size=wx.Size(71, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3,
              label=u'Product', name='staticText3', parent=self.scrolledWindow1,
              pos=wx.Point(24, 96), size=wx.Size(72, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4,
              label=u'Security Type', name='staticText4', parent=self.scrolledWindow1,
              pos=wx.Point(24, 128), size=wx.Size(72, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_PANEL1STATICTEXT5,
              label=u'Maturity Date', name='staticText5', parent=self.scrolledWindow1,
              pos=wx.Point(24, 160), size=wx.Size(72, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_PANEL1STATICTEXT6,
              label=u'Price Type', name='staticText6', parent=self.scrolledWindow1,
              pos=wx.Point(24, 192), size=wx.Size(72, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_PANEL1STATICTEXT7,
              label=u'Currency', name='staticText7', parent=self.scrolledWindow1,
              pos=wx.Point(24, 224), size=wx.Size(72, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_PANEL1STATICTEXT8,
              label=u'Coupon Rate', name='staticText8', parent=self.scrolledWindow1,
              pos=wx.Point(24, 256), size=wx.Size(72, 16), style=0)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_PANEL1DATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self.scrolledWindow1, pos=wx.Point(112, 152),
              size=wx.Size(104, 21), style=wx.DP_SHOWCENTURY)

        self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL1, name='textCtrl1',
              parent=self.scrolledWindow1, pos=wx.Point(112, 24), size=wx.Size(100, 21),
              style=0, value='textCtrl1')

        self.textCtrl2 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL2, name='textCtrl2',
              parent=self.scrolledWindow1, pos=wx.Point(112, 56), size=wx.Size(100, 21),
              style=0, value='textCtrl2')

        self.textCtrl3 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL3, name='textCtrl3',
              parent=self.scrolledWindow1, pos=wx.Point(112, 88), size=wx.Size(100, 21),
              style=0, value='textCtrl3')

        self.textCtrl4 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL4, name='textCtrl4',
              parent=self.scrolledWindow1, pos=wx.Point(112, 120), size=wx.Size(100, 21),
              style=0, value='textCtrl4')

        self.textCtrl5 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL5, name='textCtrl5',
              parent=self.scrolledWindow1, pos=wx.Point(112, 248), size=wx.Size(104, 21),
              style=0, value='textCtrl5')

        self.textCtrl6 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL6, name='textCtrl6',
              parent=self.scrolledWindow1, pos=wx.Point(112, 216), size=wx.Size(104, 21),
              style=0, value='textCtrl6')

        self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_PANEL1NUMCTRL1,
              name='numCtrl1', parent=self.scrolledWindow1, pos=wx.Point(112, 184),
              size=wx.Size(104, 22), style=0, value=0)

    def __init__(self, parent, id, name):
        self._init_ctrls(parent)
