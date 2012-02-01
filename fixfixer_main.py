#!/usr/bin/python

import wx
import fixfixer_gui
import fixfixer_xml



if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = fixfixer_gui.FixFixerGui(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
