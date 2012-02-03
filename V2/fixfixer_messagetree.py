import wx
import pyperclip
import fixfixer_xml


class MessageTree(wx.TreeCtrl):
    """An extended wx.TreeCtrl with added functionality."""
    def __init__(self, window, tID, ActionHistory):
        wx.TreeCtrl.__init__(self, window, tID, style=wx.TR_HAS_BUTTONS|
                             wx.TR_NO_LINES|wx.TR_DEFAULT_STYLE|
                             wx.SUNKEN_BORDER|wx.TR_EDIT_LABELS|wx.TR_MULTIPLE)

        self.ActionHistory = ActionHistory

        # Set up the right-click popup menu.
        self.popup = wx.Menu()
        self.popup_copy = wx.MenuItem(self.popup, 0, "&Copy\tCtrl-C", 
                                                "Copy item", wx.ITEM_NORMAL)
        self.popup_paste =wx.MenuItem(self.popup, 1, "&Paste\tCtrl-V", 
                                                "Replace item", wx.ITEM_NORMAL)
        self.popup_delete = wx.MenuItem(self.popup, 2, "&Delete\tDelete", 
                                                "Delete item", wx.ITEM_NORMAL)
        self.popup_insert = wx.MenuItem(self.popup, 3, "Insert", 
                                                "Insert item", wx.ITEM_NORMAL)
        self.popup_edit = wx.MenuItem(self.popup, 4, "Edit", 
                                                "Edit item", wx.ITEM_NORMAL)
        self.popup.AppendItem(self.popup_edit)
        self.popup.AppendItem(self.popup_copy)
        self.popup.AppendItem(self.popup_paste)
        self.popup.AppendSeparator()
        self.popup.AppendItem(self.popup_delete)
        self.popup.AppendItem(self.popup_insert)
        
        # Drag'n'Drop Popup
        self.dnd_popup = wx.Menu()
        self.move_above = wx.MenuItem(self.dnd_popup, 5, "Insert Above", 
                                      "Insert item above", wx.ITEM_NORMAL)
        self.move_below = wx.MenuItem(self.dnd_popup, 6, "Insert Below", 
                                      "Insert item below", wx.ITEM_NORMAL)
        self.add_child = wx.MenuItem(self.dnd_popup, 7, "Add as child", 
                                      "Add item as child", wx.ITEM_NORMAL)
        self.move_cancel = wx.MenuItem(self.dnd_popup, 8, "Cancel", 
                                      "Cancel move", wx.ITEM_NORMAL)
        self.dnd_popup.AppendItem(self.move_above)
        self.dnd_popup.AppendItem(self.move_below)
        self.dnd_popup.AppendItem(self.add_child)
        self.dnd_popup.AppendSeparator()
        self.dnd_popup.AppendItem(self.move_cancel)


        # Add bindings for popup menu
        self.Bind(wx.EVT_MENU, self.doCopyChild, self.popup_copy)
        self.Bind(wx.EVT_MENU, self.doPasteChild, self.popup_paste)
        self.Bind(wx.EVT_MENU, self.doDeleteChild, self.popup_delete)
        self.Bind(wx.EVT_MENU, self.doInsertChild, self.popup_insert)
        self.Bind(wx.EVT_MENU, self.doEditChild, self.popup_edit)
        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.onRClickPopup, self)
        
        # Add binding for Drag'n'Drop
        self.Bind(wx.EVT_MENU, self.dnd_popup_result_above, self.move_above)
        self.Bind(wx.EVT_MENU, self.dnd_popup_result_below, self.move_below)
        self.Bind(wx.EVT_MENU, self.dnd_popup_result_child, self.add_child)
        self.Bind(wx.EVT_MENU, self.dnd_popup_result_cancel, self.move_cancel)

        # Add bindings for label interaction
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.onBeginLabelEdit, self)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.onEndLabelEdit, self)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.onEndLabelEdit, self)
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.onBeginLabelDrag, self)
        self.Bind(wx.EVT_TREE_END_DRAG, self.onEndLabelDrag, self)
        self.Bind(wx.EVT_TREE_ITEM_GETTOOLTIP, self.onGetToolTip, self)
        self.key_copy = wx.NewId()
        self.key_paste = wx.NewId()
        self.key_child = wx.NewId()
        self.key_endchild = wx.NewId()


        self.Bind(wx.EVT_MENU, self.doCopyChild, id=self.key_copy)
        self.Bind(wx.EVT_MENU, self.doPasteChild, id=self.key_paste)
        self.Bind(wx.EVT_MENU, self.doCreateChild, id=self.key_child)
        self.Bind(wx.EVT_MENU, self.doEndChild, id=self.key_endchild)
        self.Bind(wx.EVT_KEY_UP, self.onKeyPress)

        self.accel_tbl = wx.AcceleratorTable(
                                  [(wx.ACCEL_CTRL, ord('c'), self.key_copy),
                                   (wx.ACCEL_CTRL, ord('v'), self.key_paste),
                                   (wx.ACCEL_CTRL, ord('t'), self.key_child),
                                   (wx.ACCEL_CTRL, ord('e'), self.key_endchild)
                                  ])
        self.SetAcceleratorTable(self.accel_tbl)
        
    def GetIndex(self, wxTreeItem):
        """Get index of wxTreeItem"""
        message_root = self.GetRootItem()
        tag, cookie = self.GetFirstChild(message_root)
        if tag == wxTreeItem: return 0
        return self.GetIndexRecursive(wxTreeItem, message_root, cookie, 0)[0]
			
    def GetIndexRecursive(self, wxTreeItem, root, cookie, index):
        """Recursive subfunction of GetIndex"""
        tag, cookie = self.GetNextChild(root, cookie)
        while tag.IsOk():
            index += 1
            if tag == wxTreeItem: return (index, True)
            if self.ItemHasChildren(tag):
                index, found = self.GetIndexRecursive(wxTreeItem, root, 
                                                      cookie, index)
                if found: return (index, True)
            tag, cookie = self.GetNextChild(root, cookie)
        return (-1, False)

    def IsValid(self):
        """Return True if MessageTree consists of at least one node."""
        try:
            message_root = self.GetRootItem()
            if self.GetItemText(message_root) == 'Message':
                if self.GetChildrenCount(message_root) > 0: return True
                return False
            return False
        except wx._core.PyAssertionError:
            return False
		
# ---- Events ------------------------------------------------------- #
		
    def onRClickPopup(self, event):
        """Event handler for  presenting a right-click popup menu."""
        disabled = ['Message']
        if self.GetItemText(self.GetSelections()[0]) in disabled: return
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
        disabled = ['Message']
        try:
            self.ActionHistory.EndAdd('message_tree_edit', 
                                      self.GetItemText(self.labelEditSelected))
        except:
            pass
        selected = self.GetSelections()
        self.labelEditSelected = selected[0]
        self.labelEdit_oldlabel = self.GetItemText(selected[0])
        if self.labelEdit_oldlabel in disabled:
            event.Veto()
        self.ActionHistory.StartAdd('message_tree_edit', [selected[0], 
                                    self.GetItemText(selected[0])])
        if self.GetItemText( selected[0] ) == "                    ":
            self.SetItemText( selected[0], "" )
        
        
    def onEndLabelEdit(self, event):
        """Event handler for detecting when a label has finished being edited.

        When the event occurs, check if the label was cleared, and if so, 
        replace with 20 spaces."""
        try:
            if self.GetItemText( self.labelEditSelected ) == "":
                self.SetItemText(self.labelEditSelected, "                    ")
        except:
            pass
			
    def onBeginLabelDrag(self, event):
        """Event handler for detecting when a label is being dragged.

        If only one label is selected, the dragging is permitted."""
        disabled = ['Message']
        if self.GetItemText( self.GetSelections()[0] ) in disabled: return
        if (len(self.GetSelections()) == 1 and self.GetChildrenCount(event.GetItem()) == 0):
            self.ActionHistory.StartAdd('message_tree_move', self.GetMessage())
            event.Allow()
            self.dragItem = event.GetItem()
    
    def onEndLabelDrag(self, event):
        """Event handler for detecting when a label has finished being dragged.

        When the event occurs, the data is moved to its new location."""
        if not event.GetItem().IsOk():
            return
        if event.GetItem() == self.GetRootItem():
            return
        try:
            old = self.dragItem
        except:
            return
        new = event.GetItem()
        parent = self.GetItemParent(new)
        text = self.GetItemText(old)
        if parent != self.GetRootItem(): self.move_above.Enable(False)
        else: self.move_above.Enable(True)
        self.PopupMenu(self.dnd_popup, event.GetPoint())
        if self.dnd_popup_selected == 'cancel': return
        self.Delete(old)
        if self.dnd_popup_selected == 'above':
            self.InsertItemBefore(parent, self.GetIndex(new), text)
        elif self.dnd_popup_selected == 'below':
            self.InsertItem(parent, new, text)
        elif self.dnd_popup_selected == 'child':
            rootItem = new
            self.InsertItem(rootItem, idPrevious=new, text=text)
            self.Expand(new)
        self.ActionHistory.EndAdd('message_tree_move', self.GetMessage())

    def onGetToolTip(self, event):
        """Event handler for displaying an informative tooltip."""
        disabled = ['Message', "                    ", ""]
        selected_tag_text = self.GetItemText(event.GetItem())
        if selected_tag_text in disabled: return
        tag_text = selected_tag_text.split("=")[0]
        desc_text = fixfixer_xml.find_tag_desc(tag_text)
        event.SetToolTip(desc_text)
		
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
        """Event handler for editing a child node."""
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
        
    def dnd_popup_result_above(self, event):
        self.dnd_popup_selected = 'above'
        
    def dnd_popup_result_below(self, event):
        self.dnd_popup_selected = 'below'
        
    def dnd_popup_result_child(self, event):
        self.dnd_popup_selected = 'child'
        
    def dnd_popup_result_cancel(self, event):
        self.dnd_popup_selected = 'cancel'
# ------------------------------------------------------------------- #
		
		
    def Clear(self):
        """Removes all items from the MessageTree."""
        self.DeleteAllItems()

    def SetMessage(self, message):
        """Sets the MessageTree to the contents of the market data field."""
        self.DeleteAllItems()
        message_root = self.AddRoot("Message")
        tags = message.split('\x01')
        for tag in tags:
            if tag != "":
                self.AppendItem(message_root, tag)
        self.ExpandAll()

    def GetMessage(self, root=None):
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
                    message = message + self.GetMessage(next_tag)
                next_tag,cookie = self.GetNextChild(message_root, cookie)

            message = trim_SOH(message)
            return message
        except:
            return ""
		
    def copy_selected(self):
        """Copy the text contents of the selected node."""
        disabled = ['Message']
        try:
            selected = self.GetSelections()
            if self.GetItemText(selected[0]) in disabled: return
            if len(selected) > 1: print "Only supporting single copy at this point..."
            pyperclip.copy( str( self.GetItemText( selected[0] ) ) )
        except IndexError:
            pass

    def paste_selected(self):
        """Paste the contents of the clipboard into the selected node."""
        disabled = ['Message']
        try:
            selected = self.GetSelections()
            if self.GetItemText(selected[0]) in disabled: return
            pasteString = pyperclip.paste()
            if len(selected) > 1: print "Only supporting single paste at this point..."
            self.ActionHistory.Write('message_tree_paste', [selected[0], 
                                     self.GetItemText(selected[0]), pasteString])
            self.SetItemText(selected[0], pasteString)
        except IndexError:
            pass
		
    def delete_selected(self):
        """Delete the selected children nodes."""
        disabled = ['Message']
        try:
            selected = self.GetSelections()
            if self.GetItemText(selected[0]) in disabled: return
            old_message = self.GetMessage()
            for item in selected:
                self.Delete(item)
            new_message = self.GetMessage()
            self.ActionHistory.Write('message_tree_delete', [old_message, new_message])
        except IndexError:
            pass
		
    def insert_selected(self):
        """Insert a new child node after the selected node."""
        disabled = ['Message']
        try:
            selected = self.GetSelections()
            if self.GetItemText(selected[0]) in disabled: return
            old_message = self.GetMessage()
            rootItem = selected[0]
            if len(selected) > 1: print "Only supporting single insert at this point..."
            self.InsertItem(self.GetItemParent(rootItem), idPrevious=selected[0], 
                            text="                    ")
            new_message = self.GetMessage()
            self.ActionHistory.Write('message_tree_insert', [old_message, new_message])
        except IndexError:
            pass
		
    def edit_selected(self):
        """Edit the child node."""
        selected = self.GetSelections()
        self.EditLabel(selected[0])
	
# --- End MessageTree class ----------------------------------------- #
		

def trim_SOH(message):
    """Trim all leading and any additional SOH characters and return a new copy of
    the message."""
    while message[0] == "\x01":
        message = message[1:]
    while message[len(message)-2] == "\x01":
        message = message[:len(message)-1]
    return message
