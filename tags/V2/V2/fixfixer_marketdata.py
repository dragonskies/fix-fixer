################################################################################
# Copyright (c) 2012  Timothy Davis
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
################################################################################

import wx
import pyperclip

class MarketData(wx.TextCtrl):
    """An extended wx.TextCtrl with added functionality."""
    def __init__(self, window, tID, ActionHistory, parent):
        wx.TextCtrl.__init__(self, window, tID, "", style=wx.TE_PROCESS_ENTER|
                                   wx.TE_MULTILINE|wx.TE_RICH|wx.TE_LINEWRAP)

        self.parent = parent
        self.ActionHistory = ActionHistory
        self.CurrentString = ""

        self.Bind(wx.EVT_TEXT, self.onSetText)
        self.Bind(wx.EVT_TEXT_CUT, self.doCut)
        self.Bind(wx.EVT_TEXT_COPY, self.doCopy)
        self.Bind(wx.EVT_TEXT_PASTE, self.doPaste)
        self.Bind(wx.EVT_KEY_UP, self.onKeyPress)

    def onKeyPress(self, event):
        """Event handler for detecting special key presses."""
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_F1:
            self.parent.onShowHelp(event)
        event.Skip()

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
        if "\x01" in message: 
            message = trim_SOH(message)
            message = message.replace('\x01', '|')
        elif "^" in message:
            message = message.replace('^', '\x01')
            message = trim_SOH(message)
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
