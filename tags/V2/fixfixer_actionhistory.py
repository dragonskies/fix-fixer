class FixAction():
    """A class that represents an action taken by the user.

        The data is indexed as follows:

            Action                Index      Data
            clear                 data[0]    MarketData value
                                  data[1]    MessageTree value
            market_data_edit      data[0]    Previous MarketData value
                                  data[1]    Current MarketData value
            message_tree_edit     data[0]    MessageTree Index
                                  data[1]    Previous MessageTree Index Label
                                  data[2]    Current MessageTree Index Label
            message_tree_paste    data[0]    MessageTree Index
                                  data[1]    Previous MessageTree Index Label
                                  data[2]    Current MessageTree Index Label
            message_tree_insert   data[0]    Previous MessageTree Contents
                                  data[1]    Current MessageTree Contents
            message_tree_delete   data[0]    Previous MessageTree Contents
                                  data[1]    Current MessageTree Contents
            message_tree_move     data[0]    Previous MessageTree Contents
                                  data[1]    Current MessageTree Contents"""

    def __init__(self, parent, name, data):
        self.parent = parent
        self.name = name
        self.data = data

    def UndoAction(self):
        """The action to perform if Undo() is called."""
        if self.name == 'clear':
            self.parent.market_data.SetValue(self.data[0])
            self.parent.message_tree.set_message(self.data[1])

        elif self.name == 'market_data_edit':
            self.parent.market_data.ChangeValue(self.data[0])

        elif self.name == 'message_tree_edit':
            self.parent.message_tree.SetItemText(self.data[0], self.data[1])

        elif self.name == 'message_tree_paste':
            self.parent.message_tree.SetItemText(self.data[0], self.data[1])

        elif self.name == 'message_tree_insert':
            self.parent.message_tree.set_message(self.data[0])

        elif self.name == 'message_tree_delete':
            self.parent.message_tree.set_message(self.data[0])

        elif self.name == 'message_tree_move':
            self.parent.message_tree.set_message(self.data[0])

    def RedoAction(self):
        """The action to perform if Redo() is called."""
        if self.name == 'clear':
            self.parent.market_data.SetValue("")
            self.parent.message_tree.clear()

        elif self.name == 'market_data_edit':
            self.parent.market_data.ChangeValue(self.data[1])

        elif self.name == 'message_tree_edit':
            self.parent.message_tree.SetItemText(self.data[0], self.data[2])

        elif self.name == 'message_tree_paste':
            self.parent.message_tree.SetItemText(self.data[0], self.data[2])

        elif self.name == 'message_tree_insert':
            self.parent.message_tree.set_message(self.data[1])

        elif self.name == 'message_tree_delete':
            self.parent.message_tree.set_message(self.data[1])

        elif self.name == 'message_tree_move':
            self.parent.message_tree.set_message(self.data[1])



class FixActionHistory():
    """The Fix Action Server class.  Contains information on all of the
    applications history.  Handles query requests to the history."""
    
    def __init__(self, parent):
        self.parent = parent
        self.UndoHistory = []
        self.RedoHistory = []
        self.StartAdd_name = None
        self.StartAdd_data = None

    def Undo(self):
        """When Undo() is called, perform the action and append it to Redo, 
        enabling and disabling each as needed."""
        try:
            action = self.UndoHistory.pop()
            action.UndoAction()
            self.RedoHistory.append(action)
            self.parent.Redo.Enable(True)
        except:
            pass
        if len(self.UndoHistory) == 0: self.parent.Undo.Enable(False)

    def Redo(self):
        """When Redo() is called, perform the action and append it to Undo, 
        enabling and disabling each as needed."""
        try:
            action = self.RedoHistory.pop()
            action.RedoAction()
            self.UndoHistory.append(action)
            self.parent.Undo.Enable(True)
        except:
            pass
        if len(self.RedoHistory) == 0: self.parent.Redo.Enable(False)

    def GetUndoHistory(self):
        """Return the Undo history."""
        return self.UndoHistory

    def GetRedoHistory(self):
        """Return the Redo history."""
        return self.RedoHistory
		
    def ClearHistory(self):
        """Clear Undo and Redo histories, disabling each."""
        self.UndoHistory = []
        self.RedoHistory = []
        self.StartAdd_name = None
        self.StartAdd_data = None
        self.parent.Undo.Enable(False)
        self.parent.Redo.Enable(False)

    def Write(self, name, data):
        """Add an item to the Undo history, clearing the Redo history."""
        action = FixAction(self.parent, name, data)
        self.UndoHistory.append(action)
        self.RedoHistory = []
        self.parent.Undo.Enable(True)
        self.parent.Redo.Enable(False)

    def StartAdd(self, name, data):
        """StartAdd() is used to begin adding data when only part of it is 
        available."""
        self.StartAdd_name = name
        self.StartAdd_data = data

    def EndAdd(self, name, data):
        """Ends the StartAdd() with additional data."""
        if name == self.StartAdd_name:
            if type(data) == type(list()):
                self.Write(name, self.StartAdd_data + data )
            else:
                self.Write(name, [self.StartAdd_data, data])
        self.StartAdd_name = None
        self.StartAdd_data = None

