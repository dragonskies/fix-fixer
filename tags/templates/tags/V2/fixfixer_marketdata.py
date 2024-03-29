import wx
import pyperclip

class MarketData(wx.TextCtrl):
    """An extended wx.TextCtrl with added functionality."""
    def __init__(self, window, tID, ActionHistory):
        wx.TextCtrl.__init__(self, window, tID, "", style=wx.TE_PROCESS_ENTER|
                                   wx.TE_MULTILINE|wx.TE_RICH|wx.TE_LINEWRAP)

        self.ActionHistory = ActionHistory
        self.CurrentString = ""

        self.Bind(wx.EVT_TEXT, self.onSetText)
        self.Bind(wx.EVT_TEXT_CUT, self.doCut)
        self.Bind(wx.EVT_TEXT_COPY, self.doCopy)
        self.Bind(wx.EVT_TEXT_PASTE, self.doPaste)


    def onSetText(self, event):
        """Event handler for when the text is modified."""
        self.ActionHistory.Write('market_data_edit', [self.CurrentString, 
                                 self.GetValue()])
        self.CurrentString = self.GetValue()

    def doCut(self, event):
        """Event handler for Cut command."""
        insertionpoint = self.GetInsertionPoint()
        selection = self.GetSelection()
        message = self.GetMessage()
        message = message[selection[0]:selection[1]]
        pyperclip.copy( message )
        message = self.GetValue()
        message = message[:selection[0]] + message[selection[1]:]
        self.SetMessage( message )
        self.SetInsertionPoint(insertionpoint)
		
    def doCopy(self, event):
        """Event handler for Copy command."""
        selection = self.GetSelection()
        message = self.GetMessage()
        message = message[selection[0]:selection[1]]
        pyperclip.copy( message )
		
    def doPaste(self, event):
        """Event handler for Paste command."""
        insertionpoint = self.GetInsertionPoint()
        selection = self.GetSelection()
        message = self.GetMessage()
        message = message[:selection[0]] + pyperclip.paste() + message[selection[1]:]
        self.SetMessage(message)

    def SetMessage(self, message):
        """Update the MarketData message."""
        if "\x01" in message: message = trim_SOH(message)
        message = message.replace('\x01', '|')
        self.SetValue(message)

    def GetMessage(self):
        """Return the MarketData message."""
        message = self.GetValue()
        message = message.replace('|', '\x01')
        return message

    def Clear(self):
        """Clear the MarketData message."""
        self.SetMessage("")


def trim_SOH(message):
    """Trim all leading and any additional SOH characters and return a new copy 
    of the message."""
    while message[0] == "\x01":
        message = message[1:]
    while message[len(message)-2] == "\x01":
        message = message[:len(message)-1]
    return message
