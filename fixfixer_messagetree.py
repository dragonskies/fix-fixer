import wx

import pyperclip


class MessageTree(wx.TreeCtrl):
	def __init__(self, window, tID, style):
		wx.TreeCtrl.__init__(self, window, tID, style=style)
		self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.BeginLabelEdit, self)
		self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.EndLabelEdit, self)
		self.Bind(wx.EVT_TREE_SEL_CHANGING, self.EndLabelEdit, self)
		self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.BeginLabelDrag, self)
		self.Bind(wx.EVT_TREE_END_DRAG, self.EndLabelDrag, self)
		
	def BeginLabelEdit(self, event):
		selected = self.GetSelections()
		self.labelEditSelected = selected[0]
		if self.GetItemText( selected[0] ) == "                    ":
			self.SetItemText( selected[0], "" )
			
	def EndLabelEdit(self, event):
		try:
			if self.GetItemText( self.labelEditSelected ) == "":
				self.SetItemText( self.labelEditSelected, "                    " )
		except:
			pass
			
	def BeginLabelDrag(self, event):
		if self.GetChildrenCount(event.GetItem()) == 0:
			event.Allow()
			self.dragItem = event.GetItem()
		
	def EndLabelDrag(self, event):
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
		

	def clear(self):
		# Remove all items from the MessageTree
		self.DeleteAllItems()
		self.SetValue("")

	def set_message(self, message):
		# Set the MessageTree to the specified message
		self.DeleteAllItems()
		message_root = self.AddRoot("Message")
		tags = message.split('\x01')
		for tag in tags:
			#print tag
			self.AppendItem(message_root, tag)
		self.ExpandAll()

	def get_message(self):
		# Return the text from the MessageTree, delimited by SOH
		message = ""
		message_root = self.GetRootItem()
		first_tag, cookie = self.GetFirstChild(message_root)
		message = self.GetItemText(first_tag) + "\x01"
		next_tag, cookie = self.GetNextChild(message_root, cookie)
		while next_tag.IsOk():
			message = message + self.GetItemText(next_tag) + "\x01"
			next_tag,cookie = self.GetNextChild(message_root, cookie)
		message = trim_SOH(message)
		return message
		
	def copy_selected(self):
		# Copy the text contents of the selected node.
		selected = self.GetSelections()
		if len(selected) > 1: print "Only supporting single copy at this point..."
		pyperclip.copy( str( self.GetItemText( selected[0] ) ) )
		
	def paste_selected(self):
		# Paste the contents of the clipboard into the selected node.
		selected = self.GetSelections()
		pasteString = pyperclip.paste()
		if len(selected) > 1: print "Only supporting single paste at this point..."
		self.SetItemText(selected[0], pasteString)
		
	def delete_selected(self):
		# Delete the selected child.
		selected = self.GetSelections()
		if len(selected) > 1: print "Only supporting single delete at this point..."
		self.Delete(selected[0])
		
	def insert_selected(self):
		# Insert a child item after the selected child.
		rootItem = self.GetRootItem()
		selected = self.GetSelections()
		if len(selected) > 1: print "Only supporting single insert at this point..."
		self.InsertItem(rootItem, idPrevious=selected[0], text="                    ")
	
	
def trim_SOH(message):
	# Remove any SOH from beginning of message and any additional SOH from the end.
	while message[0] == "\x01":
		message = message[1:]
	while message[len(message)-2] == "\x01":
		message = message[:len(message)-1]
	return message