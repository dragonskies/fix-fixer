#!/usr/bin/python

import fixfixergui 
import wx

app = wx.SimpleApp()
wx.InitAllImageHandlers()
frame_1 = MyFrame(None, -1, "")
app.SetTopWindow(frame_1)
frame_1.Show()
app.MainLoop()

