#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(91, 431), size=wx.Size(402, 313),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Header Section')
        self.SetClientSize(wx.Size(394, 286))

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Next',
              name='button1', parent=self, pos=wx.Point(40, 232),
              size=wx.Size(75, 23), style=0)
        self.button1.SetDefault()

        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Cancel',
              name='button2', parent=self, pos=wx.Point(272, 232),
              size=wx.Size(75, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
