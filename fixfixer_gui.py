#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Jan 10 16:12:16 2012


import wx
import os

import fixfixer_messagetree


# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.window_1 = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER|wx.SP_LIVE_UPDATE)
		self.window_1_pane_2 = wx.Panel(self.window_1, -1)
		self.window_1_pane_1 = wx.Panel(self.window_1, -1, style=wx.TAB_TRAVERSAL|wx.FULL_REPAINT_ON_RESIZE)
		
		# Menu Bar
		self.frame_1_menubar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		wxglade_edit_menu = wx.Menu()
		self.ClearMessage = wx.MenuItem(wxglade_edit_menu, 0, "Clear", "Clear_Message", wx.ITEM_NORMAL)
		self.LoadMessage = wx.MenuItem(wxglade_tmp_menu, 1, "&Load\tCtrl-O", "Load_message", wx.ITEM_NORMAL)
		self.SaveMessage = wx.MenuItem(wxglade_tmp_menu, 2, "&Save\tCtrl-S", "Save_message", wx.ITEM_NORMAL)
		self.ExitProgram = wx.MenuItem(wxglade_tmp_menu, wx.ID_EXIT, "&Exit\tCtrl-Q", "Quit", wx.ITEM_NORMAL)
		wxglade_edit_menu.AppendItem(self.ClearMessage)
		wxglade_tmp_menu.AppendItem(self.LoadMessage)
		wxglade_tmp_menu.AppendItem(self.SaveMessage)
		wxglade_tmp_menu.AppendSeparator()
		wxglade_tmp_menu.AppendItem(self.ExitProgram)
		self.frame_1_menubar.Append(wxglade_tmp_menu, "File")
		self.frame_1_menubar.Append(wxglade_edit_menu, "Edit")
		
		self.SetMenuBar(self.frame_1_menubar)
		# Menu Bar end
		self.popup = wx.Menu()
		self.copy_popup = wx.MenuItem(self.popup, 0, "Copy", "Copy item", wx.ITEM_NORMAL)
		self.paste_popup =wx.MenuItem(self.popup, 1, "Paste", "Replace item", wx.ITEM_NORMAL)
		self.delete_popup = wx.MenuItem(self.popup, 2, "Delete", "Delete item", wx.ITEM_NORMAL)
		self.insert_popup = wx.MenuItem(self.popup, 3, "Insert", "Insert new item", wx.ITEM_NORMAL)
		self.popup.AppendItem(self.copy_popup)
		self.popup.AppendItem(self.paste_popup)
		self.popup.AppendItem(self.delete_popup)
		self.popup.AppendItem(self.insert_popup)
		
		self.market_data = wx.TextCtrl(self.window_1_pane_1, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE|wx.TE_RICH|wx.TE_LINEWRAP)
		self.sort_button = wx.Button(self.window_1_pane_1, -1, "Sort message", style=wx.BU_BOTTOM)
		self.message_tree = fixfixer_messagetree.MessageTree(self.window_1_pane_2, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER|wx.TR_EDIT_LABELS|wx.TR_MULTIPLE)
		self.but = wx.Button(self.window_1_pane_2, -1, "Create message")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_MENU, self.quit_app, self.ExitProgram)
		self.Bind(wx.EVT_MENU, self.message_clear, self.ClearMessage)
		# end wxGlade
		self.Bind(wx.EVT_BUTTON, self.message_sort, self.sort_button)
		self.Bind(wx.EVT_BUTTON, self.message_create, self.but)
		self.Bind(wx.EVT_MENU, self.load_message, self.LoadMessage)
		self.Bind(wx.EVT_MENU, self.save_message, self.SaveMessage)
		
		self.key_load = wx.NewId()
		self.key_save = wx.NewId()
		self.key_quit = wx.NewId()
		
		self.Bind(wx.EVT_MENU, self.load_message, id=self.key_load)
		self.Bind(wx.EVT_MENU, self.save_message, id=self.key_save)
		self.Bind(wx.EVT_MENU, self.quit_app, id=self.key_quit)
		

		
		self.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('O'), self.key_load),
                                              (wx.ACCEL_CTRL, ord('S'), self.key_save),
                                              (wx.ACCEL_CTRL, ord('q'), self.key_quit)
                                              ])
		self.SetAcceleratorTable(self.accel_tbl)
		
		
		self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.message_tree_popup, self.message_tree)
		
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
		
	def message_create(self, event):
		self.market_data.SetValue("")
		message = self.message_tree.get_message()
		self.market_data.SetValue(message)
		
	def message_sort(self, event):
		market_data = self.market_data.GetValue()
		self.message_tree.set_message(market_data)
		
	def message_clear(self, event):
		self.message_tree.clear()
		

	def quit_app(self, event): # wxGlade: MyFrame.<event_handler>
		self.Close()
		
		
	def load_message(self, event):
		#load a FIX message from a text file
		message_file_dialog = wx.FileDialog(self) 
		if (message_file_dialog.ShowModal() == wx.ID_CANCEL):
			return
		message_file = message_file_dialog.GetFilename()
		if (message_file_dialog.GetFilename()==""):
			return
		message_file_dir = message_file_dialog.GetPath()
		f = file(message_file_dir, 'r')
		self.market_data.SetValue(f.read())
		
	def save_message(self, event):
		filters = 'All files (*.*)|*.*|Text files (*.txt)|*.txt'
		message_file_dialog = wx.FileDialog(self, message = 'Save message as...', wildcard=filters, style= wx.SAVE | wx.OVERWRITE_PROMPT) 
		if (message_file_dialog.ShowModal() == wx.ID_CANCEL):
			return
		message_file = message_file_dialog.GetFilename()
		if (message_file_dialog.GetFilename()==""):
			return
		message_file_dir = message_file_dialog.GetPath()
		f = file(message_file_dir, 'w')
		f.write(self.market_data.GetValue())
			
		
	def message_tree_popup(self, event):
		#do right click on message tree
		#add stuff to copy/paste/add/remove tree items
		self.Bind(wx.EVT_MENU, self.doCopyChild, self.copy_popup)
		self.Bind(wx.EVT_MENU, self.doPasteChild, self.paste_popup)
		self.Bind(wx.EVT_MENU, self.doDeleteChild, self.delete_popup)
		self.Bind(wx.EVT_MENU, self.doInsertChild, self.insert_popup)
		self.PopupMenu(self.popup, event.GetPoint())
		self.resetBindings()
		
	def resetBindings(self):
		# Restore bindings to their initial settings
		self.Bind(wx.EVT_MENU, self.quit_app, self.ExitProgram)
		self.Bind(wx.EVT_MENU, self.message_clear, self.ClearMessage)
		
		self.Bind(wx.EVT_BUTTON, self.message_sort, self.sort_button)
		self.Bind(wx.EVT_BUTTON, self.message_create, self.but)
		self.Bind(wx.EVT_MENU, self.load_message, self.LoadMessage)
		self.Bind(wx.EVT_MENU, self.save_message, self.SaveMessage)
		
		self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.message_tree_popup, self.message_tree)
		
		self.Bind(wx.EVT_MENU, self.load_message, id=self.key_load)
		self.Bind(wx.EVT_MENU, self.save_message, id=self.key_save)
		self.Bind(wx.EVT_MENU, self.quit_app, id=self.key_quit)
		
	def doCopyChild(self, event):
		# Copy the text contents of the selected node.
		self.message_tree.copy_selected()
		
	def doPasteChild(self, event):
		# Paste the contents of the clipboard into the selected node.
		self.message_tree.paste_selected()
		
	def doDeleteChild(self, event):
		# Delete the selected child.
		self.message_tree.delete_selected()
		
	def doInsertChild(self, event):
		# Insert a child item after the selected child.
		self.message_tree.insert_selected()
		
# end of class MyFrame