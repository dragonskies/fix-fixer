class FixAction():
	def __init__(self, parent, name, data):
		self.parent = parent
		self.name = name
		self.data = data
		
	def UndoAction(self):
		if self.name == 'clear':
			# if 'clear', then we want to fill everything back in.
			# data[0] = previous market_data value
			# data[1] = previous message_tree data
			self.parent.market_data.SetValue(self.data[0])
			self.parent.message_tree.set_message(self.data[1])
			
		elif self.name == 'market_data_edit':
			# data[0] = previous market_data value
			# data[1] = current market_data value
			self.parent.market_data.ChangeValue(self.data[0])
			
			
		elif self.name == 'message_tree_edit':
			self.parent.message_tree.SetItemText(self.data[0], self.data[1])
			
		elif self.name == 'message_tree_paste':
			# data[0] = wxTreeId
			# data[1] = old value
			# data[2] = new value
			self.parent.message_tree.SetItemText(self.data[0], self.data[1])
		
#		elif self.name == 'message_tree_insert':
		
#		elif self.name == 'message_tree_delete':
		
#		elif self.name == 'message_tree_move':
	
	def RedoAction(self):
		if self.name == 'clear':
			self.parent.market_data.SetValue("")
			self.parent.message_tree.clear()
			
		elif self.name == 'market_data_edit':
			self.parent.market_data.ChangeValue(self.data[1])
			
		elif self.name == 'message_tree_edit':
			self.parent.message_tree.SetItemText(self.data[0], self.data[2])
		
		elif self.name == 'message_tree_paste':
			self.parent.message_tree.SetItemText(self.data[0], self.data[2])
		
#		elif self.name == 'message_tree_insert':
		
#		elif self.name == 'message_tree_delete':
		
#		elif self.name == 'message_tree_move':

class FixActionHistory():
	def __init__(self, parent):
		self.parent = parent
		self.UndoHistory = []
		self.RedoHistory = []
		self.StartAdd_name = None
		self.StartAdd_data = None
		
	def Undo(self):
		try:
			action = self.UndoHistory.pop()
			action.UndoAction()
			self.RedoHistory.append(action)
		except:
			pass
		
	def Redo(self):
		try:
			action = self.RedoHistory.pop()
			action.RedoAction()
			self.UndoHistory.append(action)
		except:
			pass
		
	def GetUndoHistory(self):
		return self.UndoHistory
		
	def GetRedoHistory(self):
		return self.RedoHistory
		
	def ClearHistory(self):
		self.UndoHistory = []
		self.RedoHistory = []
		self.StartAdd_name = None
		self.StartAdd_data = None
		
	def Write(self, name, data):
		action = FixAction(self.parent, name, data)
		self.UndoHistory.append(action)
		self.RedoHistory = []
#		print "Undo:\n" + str(self.UndoHistory)
#		print "Redo:\n" + str(self.RedoHistory)
		
	def StartAdd(self, name, data):
#		print "StartAdd: %s, %s" % (name, data)
		self.StartAdd_name = name
		self.StartAdd_data = data
		
	def EndAdd(self, name, data):
#		print "EndAdd: %s, %s" % (name, data)
		if name == self.StartAdd_name:
			if type(data) == type(list()):
				self.Write(name, self.StartAdd_data + data )
			else:
				self.Write(name, [self.StartAdd_data, data])
		self.StartAdd_name = None
		self.StartAdd_data = None 