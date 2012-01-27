#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Jan 10 16:12:16 2012

import wx
import os

import fixfixer_actionhistory
import fixfixer_marketdata
import fixfixer_about
import fixfixer_messagetree
import fixfixer_help

# begin wxGlade: extracode
# end wxGlade



class FixFixerGui(wx.Frame):
	"""GUI application for handling FIX messages."""
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.AboutDialog = fixfixer_about.AboutFixFixer(self)
		self.ActionHistory = fixfixer_actionhistory.FixActionHistory(self)
		self.window_1 = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER|wx.SP_LIVE_UPDATE)
		self.window_1_pane_2 = wx.Panel(self.window_1, -1)
		self.window_1_pane_1 = wx.Panel(self.window_1, -1, style=wx.TAB_TRAVERSAL|wx.FULL_REPAINT_ON_RESIZE)
		_icon = wx.Icon("fix-fixer.ico", wx.BITMAP_TYPE_ICO)
		self.SetIcon(_icon)
		
		self.market_data_text = ""
		
		# Menu Bar
		self.frame_1_menubar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		wxglade_edit_menu = wx.Menu()
		wxglade_help_menu = wx.Menu()
		self.Undo = wx.MenuItem(wxglade_edit_menu, 5, "Undo\tCtrl-Z", "Undo_Action", wx.ITEM_NORMAL)
		self.Undo.Enable(False)
		self.Redo = wx.MenuItem(wxglade_edit_menu, 6, "Redo\tCtrl-Y", "Undo_Action", wx.ITEM_NORMAL)
		self.Redo.Enable(False)
		self.ClearMessage = wx.MenuItem(wxglade_edit_menu, 0, "Clear", "Clear_Message", wx.ITEM_NORMAL)
		self.LoadMessage = wx.MenuItem(wxglade_tmp_menu, 1, "&Load\tCtrl-O", "Load_message", wx.ITEM_NORMAL)
		self.SaveMessage = wx.MenuItem(wxglade_tmp_menu, 2, "&Save\tCtrl-S", "Save_message", wx.ITEM_NORMAL)
		self.ExitProgram = wx.MenuItem(wxglade_tmp_menu, wx.ID_EXIT, "&Exit\tCtrl-Q", "Quit", wx.ITEM_NORMAL)
		self.ShowHelp = wx.MenuItem(wxglade_help_menu, 3, "Help", "Help Dialog", wx.ITEM_NORMAL)
		self.ShowAbout = wx.MenuItem(wxglade_help_menu, 4, "About", "About Dialog", wx.ITEM_NORMAL)
		wxglade_edit_menu.AppendItem(self.Undo)
		wxglade_edit_menu.AppendItem(self.Redo)
		wxglade_edit_menu.AppendSeparator()
		wxglade_edit_menu.AppendItem(self.ClearMessage)
		wxglade_tmp_menu.AppendItem(self.LoadMessage)
		wxglade_tmp_menu.AppendItem(self.SaveMessage)
		wxglade_tmp_menu.AppendSeparator()
		wxglade_tmp_menu.AppendItem(self.ExitProgram)
		wxglade_help_menu.AppendItem(self.ShowHelp)
		wxglade_help_menu.AppendItem(self.ShowAbout)
		self.frame_1_menubar.Append(wxglade_tmp_menu, "File")
		self.frame_1_menubar.Append(wxglade_edit_menu, "Edit")
		self.frame_1_menubar.Append(wxglade_help_menu, "Help")
		
		self.SetMenuBar(self.frame_1_menubar)
		# Menu Bar end

		
		self.market_data = fixfixer_marketdata.MarketData(self.window_1_pane_1, -1, "")
		self.sort_button = wx.Button(self.window_1_pane_1, -1, "Sort message", style=wx.BU_BOTTOM)
		self.message_tree = fixfixer_messagetree.MessageTree(self.window_1_pane_2, -1, self.ActionHistory)
		self.but = wx.Button(self.window_1_pane_2, -1, "Create message")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_MENU, self.quit_app, self.ExitProgram)
		self.Bind(wx.EVT_MENU, self.undo_action, self.Undo)
		self.Bind(wx.EVT_MENU, self.redo_action, self.Redo)
		self.Bind(wx.EVT_MENU, self.message_clear, self.ClearMessage)
		self.Bind(wx.EVT_MENU, self.message_clear, self.ClearMessage)
		# end wxGlade
		self.Bind(wx.EVT_BUTTON, self.message_sort, self.sort_button)
		self.Bind(wx.EVT_BUTTON, self.message_create, self.but)
		self.Bind(wx.EVT_MENU, self.load_message, self.LoadMessage)
		self.Bind(wx.EVT_MENU, self.save_message, self.SaveMessage)
		self.Bind(wx.EVT_MENU, self.show_help, self.ShowHelp)
		self.Bind(wx.EVT_MENU, self.show_about, self.ShowAbout)
		
		self.Bind(wx.EVT_TEXT, self.onSetText, self.market_data)
		
		self.key_load = wx.NewId()
		self.key_save = wx.NewId()
		self.key_quit = wx.NewId()
		self.key_undo = wx.NewId()
		self.key_redo = wx.NewId()
		
		self.Bind(wx.EVT_MENU, self.load_message, id=self.key_load)
		self.Bind(wx.EVT_MENU, self.save_message, id=self.key_save)
		self.Bind(wx.EVT_MENU, self.quit_app, id=self.key_quit)
		self.Bind(wx.EVT_MENU, self.undo_action, id=self.key_undo)
		self.Bind(wx.EVT_MENU, self.redo_action, id=self.key_redo)

		self.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('O'), self.key_load),
                                              (wx.ACCEL_CTRL, ord('S'), self.key_save),
                                              (wx.ACCEL_CTRL, ord('q'), self.key_quit),
											  (wx.ACCEL_CTRL, ord('z'), self.key_undo),
											  (wx.ACCEL_CTRL, ord('y'), self.key_redo)
                                              ])
		self.SetAcceleratorTable(self.accel_tbl)
		
		

		
	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle("Fix Message fixer")
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_3 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.GridSizer(2, 1, 5, 6)
		sizer_2.Add(self.market_data, 0, wx.ALL|wx.EXPAND, 0)
		sizer_2.Add(self.sort_button, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0)
		self.window_1_pane_1.SetSizer(sizer_2)
		sizer_3.Add(self.message_tree, 1, wx.EXPAND, 0)
		sizer_3.Add(self.but, 0, 0, 0)
		self.window_1_pane_2.SetSizer(sizer_3)
		self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)
		sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade
		
		

	def quit_app(self, event): # wxGlade: MyFrame.<event_handler>
		"""Event handler to exit the application."""
		self.Close()
		
	def undo_action(self, event):
		self.ActionHistory.Undo()
		
	def redo_action(self, event):
		self.ActionHistory.Redo()
		
	def show_about(self, event):
		"""Event handler to show the About Dialog."""
		self.AboutDialog.show()
		
	def show_help(self, event):
		"""Event handler to show the Help Dialog."""
		self.HelpDialog = fixfixer_help.FixFixerHelpFrame(self)
		self.HelpDialog.show()
		
	def onSetText(self, event):
		self.ActionHistory.Write('market_data_edit', [self.market_data_text, self.market_data.GetValue()])
		self.market_data_text = self.market_data.GetValue()
		
	def load_message(self, event):
		"""Load message from .TXT file."""
		message_file_dialog = wx.FileDialog(self) 
		if (message_file_dialog.ShowModal() == wx.ID_CANCEL):
			return
		message_file = message_file_dialog.GetFilename()
		if (message_file_dialog.GetFilename()==""):
			return
		message_file_dir = message_file_dialog.GetPath()
		f = file(message_file_dir, 'r')
		self.market_data.SetMessage(f.read())
		f.close()
		self.ActionHistory.ClearHistory()
		
	def save_message(self, event):
		"""Save message to .TXT file."""
		filters = 'All files (*.*)|*.*|Text files (*.txt)|*.txt'
		message_file_dialog = wx.FileDialog(self, message = 'Save message as...', wildcard=filters, style= wx.SAVE | wx.OVERWRITE_PROMPT) 
		if (message_file_dialog.ShowModal() == wx.ID_CANCEL):
			return
		message_file = message_file_dialog.GetFilename()
		if (message_file_dialog.GetFilename()==""):
			return
		message_file_dir = message_file_dialog.GetPath()
		f = file(message_file_dir, 'w')
		f.write(self.market_data.GetMessage())
		f.close()
		
	def message_create(self, event):
		"""Updates the market data field to reflect the contents of the MessageTree."""
		# Do not clear market_data unless MessageTree is valid.
		try:
			message = self.message_tree.get_message()
			self.market_data.SetMessage(message)
		except: 
			pass

		
	def message_sort(self, event):
		"""Updates the MessageTree to reflect the contents of the market data field."""
		market_data = self.market_data.GetMessage()
		self.message_tree.set_message(market_data)
		
	def message_clear(self, event):
		"""Clears the MessageTree contents."""
		self.ActionHistory.Write('clear',
								  (self.market_data.GetValue(), self.message_tree.get_message()))
		self.market_data.ChangeValue("")
		self.message_tree.clear()
	
# end of class MyFrame