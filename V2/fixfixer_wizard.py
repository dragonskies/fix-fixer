import wx
import os
import sys

import fixfixer_template1
import fixfixer_template2
import fixfixer_template3
import fixfixer_template4

def doMessageWizard(fixframe):
	wizard_dialog1 = fixfixer_template1.create(fixframe)
	wizard_dialog1.Center()
	wizard_dialog1.ShowModal()
	if wizard_dialog1.GetReturnCode() == wx.ID_OK:
		selected_message = wizard_dialog1.choice1.GetSelection()
		if selected_message == 0:
			header_message = "35=X" + "\x01" + "48=" + wizard_dialog1.textCtrl1.GetValue() + "\x01"
			body_message = doMarketDataMessage(fixframe)
			return header_message + body_message
		elif (selected_message == 1) or (selected_message ==2):
			if selected_message ==1:
				header_message = "35=y\x0148=" + wizard_dialog1.textCtrl1.GetValue() + "\x01"
			else:
				header_message = "35=f\x0148=" + wizard_dialog1.textCtrl1.GetValue() + "\x01"
			body_message = doSecurityMessage(fixframe)
			return header_message + body_message
		
def doMarketDataMessage(fixframe):
	wizard_dialog2 = fixfixer_template2.create(fixframe)
	wizard_dialog2.Center()
	wizard_dialog2.ShowModal()
	if wizard_dialog2.GetReturnCode() ==wx.CANCEL:
		return Null
	return wizard_dialog2.GetMarketData()
	
def doSecurityMessage(fixframe):
	wizard_dialog3 = fixfixer_template3.create(fixframe)
	wizard_dialog3.Center()
	wizard_dialog3.ShowModal()
	if wizard_dialog3.GetReturnCode() == wx.CANCEL:
		return Null
	wizard_dialog4 = fixfixer_template4.create(fixframe)
	wizard_dialog4.Center()
	wizard_dialog4.ShowModal()
	if wizard_dialog4.GetReturnCode() == wx.CANCEL:
		return Null
	return wizard_dialog4.GetSecurityData()+wizard_dialog3.GetLegInformation()
