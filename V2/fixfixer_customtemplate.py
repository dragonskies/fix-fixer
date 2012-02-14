#Boa:Dialog:Dialog1

import wx
import wx.gizmos

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, 
 wxID_DIALOG1EDITABLELISTBOX1, wxID_DIALOG1LISTBOOK1, wxID_DIALOG1LISTBOOK2, 
 wxID_DIALOG1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(956, 384), size=wx.Size(526, 401),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Template Information')
        self.SetClientSize(wx.Size(518, 374))
        self.SetToolTipString(u'Basic information that you want to reuse')
        self.Center(wx.BOTH)
        self.SetThemeEnabled(True)

        self.editableListBox1 = wx.gizmos.EditableListBox(id=wxID_DIALOG1EDITABLELISTBOX1,
              label=u'Default tag values', name='editableListBox1', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(472, 312))

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'Save',
              name='button1', parent=self, pos=wx.Point(24, 344),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Cancel',
              name='button2', parent=self, pos=wx.Point(408, 344),
              size=wx.Size(75, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG1BUTTON2)

        self.button3 = wx.Button(id=wxID_DIALOG1BUTTON3, label=u'Load',
              name='button3', parent=self, pos=wx.Point(224, 344),
              size=wx.Size(75, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_DIALOG1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
        event.Skip()
        
    def OnButton1Button(self, event):
        #save the tag list
        self.EndModal(1)

    def OnButton3Button(self, event):
        event.Skip()
