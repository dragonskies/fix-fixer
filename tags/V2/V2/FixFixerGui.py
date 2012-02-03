################################################################################
# Copyright (c) 2012  Timothy Davis
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
################################################################################

#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Fri Feb 03 08:38:38 2012

import wx
import threading
import time
import sys
import os

import fixfixer_actionhistory
import fixfixer_marketdata
import fixfixer_about
import fixfixer_messagetree
import fixfixer_help

# begin wxGlade: extracode
# end wxGlade


class FixFixerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FixFixerFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.AboutDialog = fixfixer_about.AboutFixFixer(self)
        self.ActionHistory = fixfixer_actionhistory.FixActionHistory(self)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        
        # File Menu
        self.FileMenu = wx.Menu()
        self.FileMenu_Load = wx.MenuItem(self.FileMenu, 1, 
                                "&Load\tCtrl-O", "Load a Market Data message from a file.", wx.ITEM_NORMAL)
        self.FileMenu_Save = wx.MenuItem(self.FileMenu, 2, 
                                "&Save\tCtrl-S", "Save Market Data message to a file.", wx.ITEM_NORMAL)
        self.FileMenu_Exit = wx.MenuItem(self.FileMenu, wx.ID_EXIT, 
                                "&Exit\tCtrl-Q", "Exit the application.", wx.ITEM_NORMAL)
        self.FileMenu.AppendItem(self.FileMenu_Load)
        self.FileMenu.AppendItem(self.FileMenu_Save)
        self.FileMenu.AppendSeparator()
        self.FileMenu.AppendItem(self.FileMenu_Exit)
        self.menubar.Append(self.FileMenu, "File")

        # Edit Menu
        self.EditMenu = wx.Menu()
        self.EditMenu_Undo = wx.MenuItem(self.EditMenu, 4, 
                                "&Undo\tCtrl-Z", "Undo the previous action.", wx.ITEM_NORMAL)
        self.EditMenu_Undo.Enable(False)
        self.EditMenu_Redo = wx.MenuItem(self.EditMenu, 5, 
                                "&Redo\tCtrl-Y", "Redo the previously undone action.", wx.ITEM_NORMAL)
        self.EditMenu_Redo.Enable(False)
        self.EditMenu_Clear = wx.MenuItem(self.EditMenu, 6, 
                                "&Clear", "Clear the Market Data and Message Tree.", wx.ITEM_NORMAL)
        self.EditMenu.AppendItem(self.EditMenu_Undo)
        self.EditMenu.AppendItem(self.EditMenu_Redo)
        self.EditMenu.AppendSeparator()
        self.EditMenu.AppendItem(self.EditMenu_Clear)
        self.menubar.Append(self.EditMenu, "Edit")

        # Help Menu
        self.HelpMenu = wx.Menu()
        self.HelpMenu_Help = wx.MenuItem(self.HelpMenu, 7, 
                                "&Help\tF1", "Get help with Fix Message Fixer.", wx.ITEM_NORMAL)
        self.HelpMenu_About = wx.MenuItem(self.HelpMenu, 8, 
                                "&About", "About Fix Message Fixer.", wx.ITEM_NORMAL)
        self.HelpMenu.AppendItem(self.HelpMenu_Help)
        self.HelpMenu.AppendItem(self.HelpMenu_About)
        self.menubar.Append(self.HelpMenu, "Help")
        
        self.SetMenuBar(self.menubar)
        # Menu Bar end
        
        self.statusbar = self.CreateStatusBar(1, wx.ST_SIZEGRIP)
        self.splitterWindow = wx.SplitterWindow(self, -1, style=wx.SP_3D | wx.SP_BORDER | wx.SP_3DBORDER | wx.SP_3DSASH | wx.SP_NO_XP_THEME | wx.SP_LIVE_UPDATE)
        self.splitterWindow_pane_1 = wx.Panel(self.splitterWindow, -1)
        self.MarketData = fixfixer_marketdata.MarketData(self.splitterWindow_pane_1, 
                                                         -1, self.ActionHistory, self)
        self.pane_1_sizer_staticbox = wx.StaticBox(self.splitterWindow_pane_1, -1, "Market Data Pastebin")
        self.splitterWindow_pane_2 = wx.Panel(self.splitterWindow, -1)
        self.pushButton_toMessageTree = wx.BitmapButton(self.splitterWindow_pane_2, -1, wx.Bitmap( os.path.join('resources', 'next.png'), wx.BITMAP_TYPE_ANY), style=wx.NO_BORDER)
        self.pushButton_toMarketData = wx.BitmapButton(self.splitterWindow_pane_2, -1, wx.Bitmap( os.path.join('resources', 'prev.png'), wx.BITMAP_TYPE_ANY), style=wx.NO_BORDER)
        self.MessageTree = fixfixer_messagetree.MessageTree(
                            self.splitterWindow_pane_2, -1, self.ActionHistory, self)
        self.messageTree_sizer_staticbox = wx.StaticBox(self.splitterWindow_pane_2, -1, "Fix Message Tree")

        self.__set_properties()
        self.__do_layout()
        self.__do_bindings()
        
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FixFixerFrame.__set_properties
        self.SetTitle("Fix Message Fixer")
        self.SetIcon( wx.Icon(os.path.join('resources', 'fix-fixer.ico'), wx.BITMAP_TYPE_ICO) )
        self.SetSize((640, 480))
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields
        statusbar_fields = [""]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        self.MarketData.SetMinSize((200, 388))
        self.MarketData.SetFocus()
        self.splitterWindow_pane_1.SetMinSize((239, 410))
        self.pushButton_toMessageTree.SetToolTipString("Sort into MessageTree")
        self.pushButton_toMessageTree.SetSize(self.pushButton_toMessageTree.GetBestSize())
        self.pushButton_toMarketData.SetToolTipString("Write to Market Data")
        self.pushButton_toMarketData.SetSize(self.pushButton_toMarketData.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FixFixerFrame.__do_layout
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        pane_2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.messageTree_sizer_staticbox.Lower()
        messageTree_sizer = wx.StaticBoxSizer(self.messageTree_sizer_staticbox, wx.VERTICAL)
        pushButton_sizer = wx.BoxSizer(wx.VERTICAL)
        self.pane_1_sizer_staticbox.Lower()
        pane_1_sizer = wx.StaticBoxSizer(self.pane_1_sizer_staticbox, wx.HORIZONTAL)
        pane_1_sizer.Add(self.MarketData, 1, wx.EXPAND, 0)
        self.splitterWindow_pane_1.SetSizer(pane_1_sizer)
        pushButton_sizer.Add(self.pushButton_toMessageTree, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        pushButton_sizer.Add(self.pushButton_toMarketData, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        pane_2_sizer.Add(pushButton_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        messageTree_sizer.Add(self.MessageTree, 1, wx.EXPAND, 0)
        pane_2_sizer.Add(messageTree_sizer, 1, wx.EXPAND, 0)
        self.splitterWindow_pane_2.SetSizer(pane_2_sizer)
        self.splitterWindow.SplitVertically(self.splitterWindow_pane_1, self.splitterWindow_pane_2, 241)
        mainSizer.Add(self.splitterWindow, 1, wx.EXPAND, 0)
        self.SetSizer(mainSizer)
        self.Layout()
        self.Centre()
        # end wxGlade

    def __do_bindings(self):
        # File Menu
        self.Bind(wx.EVT_MENU, self.onLoadMessage, self.FileMenu_Load)
        self.Bind(wx.EVT_MENU, self.onSaveMessage, self.FileMenu_Save)
        self.Bind(wx.EVT_MENU, self.onExit, self.FileMenu_Exit)

        # Edit Menu
        self.Bind(wx.EVT_MENU, self.onUndo, self.EditMenu_Undo)
        self.Bind(wx.EVT_MENU, self.onRedo, self.EditMenu_Redo)
        self.Bind(wx.EVT_MENU, self.onClear, self.EditMenu_Clear)

        # Help Menu
        self.Bind(wx.EVT_MENU, self.onShowHelp, self.HelpMenu_Help)
        self.Bind(wx.EVT_MENU, self.onShowAbout, self.HelpMenu_About)

        # Splitter Window
        self.Bind(wx.EVT_SPLITTER_DCLICK, self.onSplitterWindowUnsplit, self.splitterWindow)

        # Buttons
        self.Bind(wx.EVT_BUTTON, self.onPushButton_toMessageTree, self.pushButton_toMessageTree)
        self.Bind(wx.EVT_BUTTON, self.onPushButton_toMarketData, self.pushButton_toMarketData)

        # Exit
        self.Bind(wx.EVT_CLOSE, self.onExit)

        # Key bindings
        self.key_load = wx.NewId()
        self.key_save = wx.NewId()
        self.key_quit = wx.NewId()
        self.key_undo = wx.NewId()
        self.key_redo = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onLoadMessage, id=self.key_load)
        self.Bind(wx.EVT_MENU, self.onSaveMessage, id=self.key_save)
        self.Bind(wx.EVT_MENU, self.onExit, id=self.key_quit)
        self.Bind(wx.EVT_MENU, self.onUndo, id=self.key_undo)
        self.Bind(wx.EVT_MENU, self.onRedo, id=self.key_redo)
        self.Bind(wx.EVT_KEY_UP, self.onKeyPress)
        self.accel_tbl = wx.AcceleratorTable(
                                    [(wx.ACCEL_CTRL, ord('o'), self.key_load),
                                     (wx.ACCEL_CTRL, ord('s'), self.key_save),
                                     (wx.ACCEL_CTRL, ord('q'), self.key_quit),
                                     (wx.ACCEL_CTRL, ord('z'), self.key_undo),
                                     (wx.ACCEL_CTRL, ord('y'), self.key_redo),
                                    ])
        self.SetAcceleratorTable(self.accel_tbl)

# ----- Events --------------------------------------------------------------- #

    def onKeyPress(self, event):
        """Event handler for detecting special key presses."""
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_F1:
            self.onShowHelp(event)
        event.Skip()

    def onLoadMessage(self, event):
        """Load message from .TXT file."""
        LoadFileDialog = wx.FileDialog(self) 
        if (LoadFileDialog.ShowModal() == wx.ID_CANCEL): return
        message_file = LoadFileDialog.GetFilename()
        if (LoadFileDialog.GetFilename()==""): return
        message_file_dir = LoadFileDialog.GetPath()
        f = file(message_file_dir, 'r')
        self.MarketData.SetMessage(f.read())
        f.close()
        self.ActionHistory.ClearHistory()
        self.SetStatusbar("Loaded file %s" % message_file_dir, 3)

    def onSaveMessage(self, event):
        """Save message to .TXT file."""
        filters = 'All files (*.*)|*.*|Text files (*.txt)|*.txt'
        SaveFileDialog = wx.FileDialog(self, message = 'Save message as...'
                                            , wildcard=filters, style= wx.SAVE |
                                            wx.OVERWRITE_PROMPT) 
        if (SaveFileDialog.ShowModal() == wx.ID_CANCEL): return
        message_file = SaveFileDialog.GetFilename()
        if (SaveFileDialog.GetFilename()==""): return
        message_file_dir = SaveFileDialog.GetPath()
        f = file(message_file_dir, 'w')
        f.write(self.MarketData.GetMessage())
        f.close()
        self.SetStatusbar("Saved file %s" % message_file_dir, 3)

    def onExit(self, event):
        """Event handler to exit the application."""
        dlg = wx.MessageDialog(self, "Are you sure you wish to exit?",
                               "Confirm Exit", wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK: sys.exit()

    def onUndo(self, event):
        """Event handler for Undo action."""
        self.ActionHistory.Undo()

    def onRedo(self, event):
        """Event handler for Redo action."""
        self.ActionHistory.Redo()

    def onClear(self, event):
        """Event handler for clearing MarketData and MessageTree contents."""
        self.ActionHistory.Write('clear', (self.MarketData.GetValue(), 
                                           self.MessageTree.GetMessage()))
        self.MarketData.Clear()
        self.MessageTree.Clear()

    def onShowHelp(self, event):
        """Event handler to show the Help Dialog."""
        HelpDialog = fixfixer_help.FixFixerHelpFrame(self)
        HelpDialog.show()

    def onShowAbout(self, event):
        """Event handler to show the About Dialog."""
        self.AboutDialog.show()

    def onSplitterWindowUnsplit(self, event):
        """Event handler to prevent SplitterWindow from unsplitting."""
        event.Veto()

    def onPushButton_toMessageTree(self, event):
        """Event handler for pushing data from MarketData to MessageTree."""
        MarketDataText = self.MarketData.GetMessage()
        self.MessageTree.SetMessage(MarketDataText)
        self.MessageTree.SetFocus()

    def onPushButton_toMarketData(self, event):
        """Event handler for pushing data from MessageTree to MarketData."""
        MessageTreeText = self.MessageTree.GetMessage()
        self.MarketData.SetMessage(MessageTreeText)
        self.MarketData.SetFocus()

# ---------------------------------------------------------------------------- #

# ----- Functions ------------------------------------------------------------ #

    def SetStatusbar(self, msg, timeout=0):
        """Set the statusbar text to 'msg' with an optional timeout (in seconds)."""
        self.statusmsg = self.statusbar.GetStatusText()
        self.statusbar.SetStatusText(msg, 0)
        self.statusmsgTimeout = timeout
        if timeout != 0:
            WT = WorkerThread(self.StatusbarTimer, self)
            WT.start()

    def StatusbarTimer(self):
        """Threaded function which waits for a given time and then restores the 
        previously stored statusbar message."""
        time.sleep(self.statusmsgTimeout)
        self.statusbar.SetStatusText(self.statusmsg)

# ---------------------------------------------------------------------------- #

class WorkerThread(threading.Thread):

    def __init__ (self, function, parent):
        threading.Thread.__init__(self)
        self.function = function
        self.parent = parent

    def run(self): # when does "run" get executed?
        self.parent.still_working = True
        self.function()
        self.parent.still_working = False

    def stop(self):
        self = None

# end of class FixFixerFrame
class FixFixerGui(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrame = FixFixerFrame(None, -1, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        return 1

# end of class FixFixerGui

