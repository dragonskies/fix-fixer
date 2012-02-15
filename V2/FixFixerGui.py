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
import fixfixer_customtemplate
import FixFixerProperties
import fixfixer_template1
import fixfixer_template2
import fixfixer_template3
import fixfixer_template4


# begin wxGlade: extracode
# end wxGlade


class FixFixerFrame(wx.Frame):
    
    default_tags = FixFixerProperties.DefaultTags()
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: FixFixerFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.AboutDialog = fixfixer_about.AboutFixFixer(self)
        self.ActionHistory = fixfixer_actionhistory.FixActionHistory(self)

        self.undo_enabled = False
        self.redo_enabled = False
        
        # Menu Bar
        self.menubar = wx.MenuBar()

        # File Menu
        self.FileMenu = wx.Menu()
        self.FileMenu_Load = wx.MenuItem(self.FileMenu, 1, 
                                "&Load\tCtrl-O", "Load a Market Data message from a file.", wx.ITEM_NORMAL)
        self.FileMenu_Save = wx.MenuItem(self.FileMenu, 2, 
                                "&Save\tCtrl-S", "Save Market Data message to a file.", wx.ITEM_NORMAL)
        self.FileMenu_Wizard = wx.MenuItem(self.FileMenu, 10, "Message &Wizard", "Create a FIX message easily", wx.ITEM_NORMAL)
        self.FileMenu_Exit = wx.MenuItem(self.FileMenu, wx.ID_EXIT, 
                                "&Exit\tCtrl-Q", "Exit the application.", wx.ITEM_NORMAL)
        self.FileMenu.AppendItem(self.FileMenu_Load)
        self.FileMenu.AppendItem(self.FileMenu_Save)
        self.FileMenu.AppendItem(self.FileMenu_Wizard)
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
        self.EditMenu_Preferences = wx.MenuItem(self.EditMenu, 9, "&Preferences\tCtrl-P", "Change program settings", wx.ITEM_NORMAL)
        self.EditMenu.AppendItem(self.EditMenu_Undo)
        self.EditMenu.AppendItem(self.EditMenu_Redo)
        self.EditMenu.AppendSeparator()
        self.EditMenu.AppendItem(self.EditMenu_Preferences)
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

        # Tool Bar
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.TB_FLAT 
                                                  | wx.TB_DOCKABLE)
        self.SetToolBar(self.toolbar)

        self.NewIcon = wx.Bitmap(os.path.join('resources', "new.png"), wx.BITMAP_TYPE_ANY)
        self.OpenIcon = wx.Bitmap(os.path.join('resources', "open.png"), wx.BITMAP_TYPE_ANY)
        self.SaveIcon = wx.Bitmap(os.path.join('resources', "save.png"), wx.BITMAP_TYPE_ANY)
        self.UndoIcon = wx.Bitmap(os.path.join('resources', "undo.png"), wx.BITMAP_TYPE_ANY)
        self.RedoIcon = wx.Bitmap(os.path.join('resources', "redo.png"), wx.BITMAP_TYPE_ANY)
        self.CutIcon = wx.Bitmap(os.path.join('resources', "cut.png"), wx.BITMAP_TYPE_ANY)
        self.CopyIcon = wx.Bitmap(os.path.join('resources', "copy.png"), wx.BITMAP_TYPE_ANY)
        self.PasteIcon = wx.Bitmap(os.path.join('resources', "paste.png"), wx.BITMAP_TYPE_ANY)
        self.ClearIcon = wx.Bitmap(os.path.join('resources', "clear.png"), wx.BITMAP_TYPE_ANY)
        self.PreferencesIcon = wx.Bitmap(os.path.join('resources', "preferences.png"), wx.BITMAP_TYPE_ANY)
        
        self.button_new = self.toolbar.AddLabelTool(wx.ID_ANY, "Open New Window", 
                           self.NewIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Open New Window", "Open New Window")
        self.button_open = self.toolbar.AddLabelTool(wx.ID_ANY, "Load Message", 
                           self.OpenIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Load Message", "Load Message")
        self.button_save = self.toolbar.AddLabelTool(wx.ID_ANY, "Save Message", 
                           self.SaveIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Save Message", "Save Message")
        self.toolbar.AddSeparator()
        self.button_undo = self.toolbar.AddLabelTool(wx.ID_ANY, "Undo", 
                           self.UndoIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Undo", "Undo")
        self.button_redo = self.toolbar.AddLabelTool(wx.ID_ANY, "Redo", 
                           self.RedoIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Redo", "Redo")
        self.button_undo.Enable(False)
        self.button_redo.Enable(False)
        self.toolbar.AddSeparator()
        self.button_cut = self.toolbar.AddLabelTool(wx.ID_ANY, "Cut", 
                           self.CutIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Cut", "Cut")
        self.button_copy = self.toolbar.AddLabelTool(wx.ID_ANY, "Copy", 
                           self.CopyIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Copy", "Copy")
        self.button_paste = self.toolbar.AddLabelTool(wx.ID_ANY, "Paste", 
                           self.PasteIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Paste", "Paste")
        self.toolbar.AddSeparator()
        self.button_clear = self.toolbar.AddLabelTool(wx.ID_ANY, "Clear Contents", 
                           self.ClearIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Clear Contents", "Clear the contents of the Market Data Pastebin and the Message Tree.")
        self.toolbar.AddSeparator()
        self.button_preferences = self.toolbar.AddLabelTool(wx.ID_ANY, "Preferences", 
                           self.PreferencesIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Preferences", "Configure Fix Message Fixer")
        # Tool Bar end
        
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
        
        #properties
        
        

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
        self.toolbar.Realize()
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
        self.Bind(wx.EVT_MENU, self.onDoWizard, self.FileMenu_Wizard)
        self.Bind(wx.EVT_MENU, self.onExit, self.FileMenu_Exit)

        # Edit Menu
        self.Bind(wx.EVT_MENU, self.onUndo, self.EditMenu_Undo)
        self.Bind(wx.EVT_MENU, self.onRedo, self.EditMenu_Redo)
        self.Bind(wx.EVT_MENU, self.onPreferences, self.EditMenu_Preferences)
        self.Bind(wx.EVT_MENU, self.onClear, self.EditMenu_Clear)

        # Help Menu
        self.Bind(wx.EVT_MENU, self.onShowHelp, self.HelpMenu_Help)
        self.Bind(wx.EVT_MENU, self.onShowAbout, self.HelpMenu_About)

        # Toolbar
        self.Bind(wx.EVT_TOOL, self.onNew, self.button_new)
        self.Bind(wx.EVT_TOOL, self.onLoadMessage, self.button_open)
        self.Bind(wx.EVT_TOOL, self.onSaveMessage, self.button_save)
        self.Bind(wx.EVT_TOOL, self.onUndo, self.button_undo)
        self.Bind(wx.EVT_TOOL, self.onRedo, self.button_redo)
        self.Bind(wx.EVT_TOOL, self.onCut, self.button_cut)
        self.Bind(wx.EVT_TOOL, self.onCopy, self.button_copy)
        self.Bind(wx.EVT_TOOL, self.onPaste, self.button_paste)
        self.Bind(wx.EVT_TOOL, self.onClear, self.button_clear)
        self.Bind(wx.EVT_TOOL, self.onPreferences, self.button_preferences)

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

    def onNew(self, event):
        wx.MessageBox("'New Window' has not yet been implemented.")

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

    def onPreferences(self, event):
        personal_tags = fixfixer_customtemplate.create(self)
        print self.default_tags.GetProperties()
        personal_tags.editableListBox1.SetStrings(self.default_tags.GetProperties())
        response = personal_tags.ShowModal()
        if response == wx.ID_OK:
            print "save tags"
            tags = personal_tags.editableListBox1.Strings
            for tag in tags:
                tag_number, tag_value = tag.split("=")
                self.default_tags.SetProperty(tag_number,tag_value)
        personal_tags.Destroy()

    def onDoWizard(self, event):
        wizard_dialog1 = fixfixer_template1.create(self)
        wizard_dialog1.Center()
        wizard_dialog2 = fixfixer_template2.create(self)
        wizard_dialog2.Center()
        wizard_dialog3 = fixfixer_template3.create(self)
        wizard_dialog3.Center()
        wizard_dialog4 = fixfixer_template4.create(self)
        wizard_dialog4.Center()
        wizard_dialog1.ShowModal()
        if wizard_dialog1.GetReturnCode() == wx.ID_OK:
            selected_message = wizard_dialog1.choice1.GetSelection()
            if selected_message == 0:
                wizard_dialog2.ShowModal()
                if wizard_dialog2.GetReturnCode() ==wx.CANCEL:
                    return 0
            elif (selected_message == 1) or (selected_message ==2):
                wizard_dialog4.ShowModal()
                if wizard_dialog4.GetReturnCode() == wx.CANCEL:
                    return 0
                if wizard_dialog4.GetReturncode() == 2:
                    wizard_dialog3.ShowModal()
                    if wizard_dialog3.GetReturnCode() == wx.CANCEL:
                        return 0

    def onCut(self, event):
        focus = self.FindFocus()
        try:
            focus.doCut(event)
        except AttributeError:
            focus.doCutChild(event)

    def onCopy(self, event):
        focus = self.FindFocus()
        try:
            focus.doCopy(event)
        except AttributeError:
            focus.doCopyChild(event)

    def onPaste(self, event):
        focus = self.FindFocus()
        try:
            focus.doPaste(event)
        except AttributeError:
            focus.doPasteChild(event)
        
        
# ---------------------------------------------------------------------------- #

# ----- Functions ------------------------------------------------------------ #

    def EnableUndo(self, enabled):
        if self.undo_enabled != enabled:
            self.undo_enabled = enabled
            self.EditMenu_Undo.Enable(enabled)
            self.button_undo.Enable(enabled)
            self.toolbar.Realize()

    def EnableRedo(self, enabled):
        if self.redo_enabled != enabled:
            self.redo_enabled = enabled
            self.EditMenu_Redo.Enable(enabled)
            self.button_redo.Enable(enabled)
            self.toolbar.Realize()

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

