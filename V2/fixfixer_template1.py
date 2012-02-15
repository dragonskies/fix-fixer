#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1CHOICE1, 
 wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, wxID_DIALOG1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(609, 292), size=wx.Size(279, 226),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Header')
        self.SetClientSize(wx.Size(271, 199))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'Sending company', name='staticText1', parent=self,
              pos=wx.Point(8, 24), size=wx.Size(84, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(120, 24), size=wx.Size(100, 21),
              style=0, value=u'Sender')

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u'Message Type', name='staticText2', parent=self,
              pos=wx.Point(16, 64), size=wx.Size(69, 13), style=0)

        self.choice1 = wx.Choice(choices=['X - Incremental Refresh',
              'f - Security definition (dynamic)', 'd - Security definition',
              'V - Market data request', 'R - Quote request'],
              id=wxID_DIALOG1CHOICE1, name='choice1', parent=self,
              pos=wx.Point(120, 64), size=wx.Size(130, 21), style=0)
        self.choice1.SetSelection(0)
        
        self.button1 = wx.Button(id=wx.ID_OK, label=u'Next',
              name='button1', parent=self, pos=wx.Point(56, 160),
              size=wx.Size(75, 23), style=0)
        self.button1.SetDefault()
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

        self.button2 = wx.Button(id=wx.ID_CANCEL, label=u'Cancel',
              name='button2', parent=self, pos=wx.Point(168, 160),
              size=wx.Size(75, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG1BUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.EndModal(1)

    def OnButton2Button(self, event):
        self.EndModal(2)

    def GetMessageType(self):
        return self.choice1.GetCurrentSelection()