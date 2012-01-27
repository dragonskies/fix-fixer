import wx
import pyperclip

class MarketData(wx.TextCtrl):
	"""An extended wx.TextCtrl with added functionality."""
	def __init__(self, window, tID, ActionHistory):
		wx.TextCtrl.__init__(self, window, tID, "", style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE|wx.TE_RICH|wx.TE_LINEWRAP)
		
		self.ActionHistory = ActionHistory
		
		self.Bind(wx.EVT_TEXT_CUT, self.doCut)
		self.Bind(wx.EVT_TEXT_COPY, self.doCopy)
		self.Bind(wx.EVT_TEXT_PASTE, self.doPaste)

	def doCut(self, event):
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
		selection = self.GetSelection()
		message = self.GetMessage()
		message = message[selection[0]:selection[1]]
		pyperclip.copy( message )
		
	def doPaste(self, event):
		insertionpoint = self.GetInsertionPoint()
		selection = self.GetSelection()
		message = message[:selection[0]] + pyperclip.paste() + message[selection[1]:]
		self.SetMessage(message)
		
	def doSelectAll(self, event):
		self.SelectAll()
		
	def SetMessage(self, message):
		message = trim_SOH(message)
		message = message.replace('\x01', '|')
		self.SetValue(message)
		
	def GetMessage(self):
		message = self.GetValue()
		message = message.replace('|', '\x01')
		return message
		
	def Clear(self):
		self.SetMessage("")
		
def trim_SOH(message):
	"""Trim all leading and any additional SOH characters and return a new copy of
	the message."""
	while message[0] == "\x01":
		message = message[1:]
	while message[len(message)-2] == "\x01":
		message = message[:len(message)-1]
	return message