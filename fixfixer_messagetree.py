import wx
import pyperclip


class MessageTree(wx.TreeCtrl):
	"""An extended wx.TreeCtrl with added functionality."""
	def __init__(self, window, tID, ActionHistory):
		wx.TreeCtrl.__init__(self, window, tID, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER|wx.TR_EDIT_LABELS|wx.TR_MULTIPLE)
		
		self.ActionHistory = ActionHistory
		self.checklabel = 0
		
		# Set up the right-click popup menu.
		self.popup = wx.Menu()
		self.popup_copy = wx.MenuItem(self.popup, 0, "&Copy\tCtrl-C", "Copy item", wx.ITEM_NORMAL)
		self.popup_paste =wx.MenuItem(self.popup, 1, "&Paste\tCtrl-V", "Replace item", wx.ITEM_NORMAL)
		self.popup_delete = wx.MenuItem(self.popup, 2, "&Delete\tDelete", "Delete item", wx.ITEM_NORMAL)
		self.popup_insert = wx.MenuItem(self.popup, 3, "Insert", "Insert new item", wx.ITEM_NORMAL)
		self.popup_edit = wx.MenuItem(self.popup, 4, "Edit", "Edit item", wx.ITEM_NORMAL)
		self.popup.AppendItem(self.popup_edit)
		self.popup.AppendItem(self.popup_copy)
		self.popup.AppendItem(self.popup_paste)
		self.popup.AppendSeparator()
		self.popup.AppendItem(self.popup_delete)
		self.popup.AppendItem(self.popup_insert)
		
		
		# Add bindings for popup menu
		self.Bind(wx.EVT_MENU, self.doCopyChild, self.popup_copy)
		self.Bind(wx.EVT_MENU, self.doPasteChild, self.popup_paste)
		self.Bind(wx.EVT_MENU, self.doDeleteChild, self.popup_delete)
		self.Bind(wx.EVT_MENU, self.doInsertChild, self.popup_insert)
		self.Bind(wx.EVT_MENU, self.doEditChild, self.popup_edit)
		self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.onRClickPopup, self)
		
		# Add bindings for label interaction
		self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.onBeginLabelEdit, self)
		self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.onEndLabelEdit, self)
		self.Bind(wx.EVT_TREE_SEL_CHANGING, self.onEndLabelEdit, self)
		self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.onBeginLabelDrag, self)
		self.Bind(wx.EVT_TREE_END_DRAG, self.onEndLabelDrag, self)
		
		self.key_copy = wx.NewId()
		self.key_paste = wx.NewId()
		self.key_child = wx.NewId()
		self.key_endchild = wx.NewId()
		
		
		self.Bind(wx.EVT_MENU, self.doCopyChild, id=self.key_copy)
		self.Bind(wx.EVT_MENU, self.doPasteChild, id=self.key_paste)
		self.Bind(wx.EVT_MENU, self.doCreateChild, id=self.key_child)
		self.Bind(wx.EVT_MENU, self.doEndChild, id=self.key_endchild)
		self.Bind(wx.EVT_KEY_UP, self.onKeyPress)
		
		self.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('c'), self.key_copy),
											(wx.ACCEL_CTRL, ord('v'), self.key_paste),
											(wx.ACCEL_CTRL, ord('t'), self.key_child),
											(wx.ACCEL_CTRL, ord('e'), self.key_endchild)
											])
		self.SetAcceleratorTable(self.accel_tbl)
		
# ---- Events ------------------------------------------------------- #
		
	def onRClickPopup(self, event):
		"""Event handler for detecting a right click and presenting a popup menu."""
		self.PopupMenu(self.popup, event.GetPoint())

	def onKeyPress(self, event):
		"""Event handler for detecting special key presses."""
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_DELETE:
			self.doDeleteChild(event)
		if keycode == wx.WXK_TAB:
			self.doCreateChild(self, event)
		event.Skip()
		
	def onBeginLabelEdit(self, event):
		"""Event handler for detecting when a label is about to be edited.
	
		When the event occurs, if the label is blank (20 spaces), it is cleared
		for editing."""
		try:
			self.ActionHistory.EndAdd('message_tree_edit', self.GetItemText(self.labelEditSelected))
		except:
			pass
		selected = self.GetSelections()
		self.labelEditSelected = selected[0]
		self.labelEdit_oldlabel = self.GetItemText(selected[0])
		self.ActionHistory.StartAdd('message_tree_edit', [selected[0], self.GetItemText(selected[0])])
		if self.GetItemText( selected[0] ) == "                    ":
			self.SetItemText( selected[0], "" )
		
			
	def onEndLabelEdit(self, event):
		"""Event handler for detecting when a label has finished being edited.
		
		When the event occurs, check if the label was cleared, and if so, replace
		with 20 spaces."""
		if self.checklabel == 1:
			try:
				if self.GetItemText( self.labelEditSelected ) == "":
					self.SetItemText( self.labelEditSelected, "                    " )
			except:
				pass
#			if self.labelEdit_oldlabel == self.GetItemText(self.labelEditSelected):
#				self.ActionHistory.EndAdd('null', 0)
#			else:
#				self.ActionHistory.EndAdd('market_data_edit', self.GetItemText(self.labelEditSelected))
#			self.checklabel = 0
#		else:
#			self.checklabel = 1
			
	def onBeginLabelDrag(self, event):
		"""Event handler for detecting when a label is being dragged.
		
		If only one label is selected, the dragging is permitted."""
		if (len(self.GetSelections()) == 1 and self.GetChildrenCount(event.GetItem()) == 0):
			self.ActionHistory.StartAdd('message_tree_move', self.get_message())
			event.Allow()
			self.dragItem = event.GetItem()
		
	def onEndLabelDrag(self, event):
		"""Event handler for detecting when a label has finished being dragged.
		
		When the event occurs, the data is moved to its new location."""
		if not event.GetItem().IsOk():
			return
		try:
			old = self.dragItem
		except:
			return
		new = event.GetItem()
		parent = self.GetItemParent(new)
		text = self.GetItemText(old)
		self.Delete(old)
		self.InsertItem(parent, new, text)
		self.ActionHistory.EndAdd('message_tree_move', self.get_message())
		
	def doCopyChild(self, event):
		"""Event handler for copying a child node."""
		self.copy_selected()
		
	def doPasteChild(self, event):
		"""Event handler for pasting a child node."""
		self.paste_selected()
		
	def doDeleteChild(self, event):
		"""Event handler for deleting a child (children) node(s)."""
		self.delete_selected()
		
	def doInsertChild(self, event):
		"""Event handler for inserting a new child node after the selected node."""
		self.insert_selected()
		
	def doEditChild(self, event):
		
		self.edit_selected()
	
	def doCreateChild(self, event):
		"""Create a repeating group"""
		print "insert new child node"
		selected = self.GetSelections()
		rootItem = selected[0]
		if len(selected) > 1: print "Only supporting single insert at this point..."
		self.InsertItem(rootItem, idPrevious=selected[0], text="tag=value")
		
		
	def doEndChild(self, event):
		"""End a repeating group"""
		print "move back to root"
# ------------------------------------------------------------------- #
		
		
	def clear(self):
		"""Removes all items from the MessageTree."""
		self.DeleteAllItems()

	def set_message(self, message):
		"""Sets the MessageTree to the contents of the market data field."""
		self.DeleteAllItems()
		message_root = self.AddRoot("Message")
		tags = message.split('\x01')
		for tag in tags:
			if tag != "":
				self.AppendItem(message_root, tag)
		self.ExpandAll()

	def get_message(self, root=None):
		"""Returns the text from the MessageTree, delimited by SOH."""
		try:
			message = ""
			message_root = root
			if not message_root:
				message_root = self.GetRootItem()
			first_tag, cookie = self.GetFirstChild(message_root)
			message = self.GetItemText(first_tag) + "\x01"
			next_tag, cookie = self.GetNextChild(message_root, cookie)
			while next_tag.IsOk():
				message = message + self.GetItemText(next_tag) + "\x01"
				if self.ItemHasChildren(next_tag):
					message = message + self.get_message(next_tag)
				next_tag,cookie = self.GetNextChild(message_root, cookie)

			message = trim_SOH(message)
			return message
		except:
			return ""
		
	def copy_selected(self):
		"""Copy the text contents of the selected node."""
		selected = self.GetSelections()
		if len(selected) > 1: print "Only supporting single copy at this point..."
		pyperclip.copy( str( self.GetItemText( selected[0] ) ) )

	def paste_selected(self):
		"""Paste the contents of the clipboard into the selected node."""
		selected = self.GetSelections()
		pasteString = pyperclip.paste()
		if len(selected) > 1: print "Only supporting single paste at this point..."
		self.ActionHistory.Write('message_tree_paste', [selected[0], self.GetItemText(selected[0]), pasteString])
		self.SetItemText(selected[0], pasteString)
		
	def delete_selected(self):
		"""Delete the selected children nodes."""
		old_message = self.get_message()
		selected = self.GetSelections()
		for item in selected:
			self.Delete(item)
		new_message = self.get_message()
		self.ActionHistory.Write('message_tree_delete', [old_message, new_message])
		
	def insert_selected(self):
		"""Insert a new child node after the selected node."""
		old_message = self.get_message()
		selected = self.GetSelections()
		rootItem = selected[0]
		if len(selected) > 1: print "Only supporting single insert at this point..."
		self.InsertItem(self.GetItemParent(rootItem), idPrevious=selected[0], text="                    ")
		new_message = self.get_message()
		self.ActionHistory.Write('message_tree_insert', [old_message, new_message])
		
	def edit_selected(self):
		"""Edit the child node."""
		selected = self.GetSelections()
#		old_label = self.GetItemText(selected[0])

		self.EditLabel(selected[0])
#		new_label = self.GetItemText(selected[0])
#		if old_label != self.GetItemText(selected[0]):
#			self.ActionHistory.Write('message_tree_edit', [selected[0], old_label, new_label])
		
# --- End MessageTree class ----------------------------------------- #
		

def trim_SOH(message):
	"""Trim all leading and any additional SOH characters and return a new copy of
	the message."""
	while message[0] == "\x01":
		message = message[1:]
	while message[len(message)-2] == "\x01":
		message = message[:len(message)-1]
	return message