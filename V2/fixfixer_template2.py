#Boa:Dialog:Body1
# Body information for Market Data refresh message

import wx
import wx.lib.intctrl
import wx.lib.masked.numctrl
from wx.lib.anchors import LayoutAnchors

def create(parent):
	return Body1(parent)

[wxID_BODY1, wxID_BODY1BUTTON1, wxID_BODY1BUTTON2, wxID_BODY1NOTEBOOK1, 
wxID_BODY1SPINCTRL1, wxID_BODY1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Body1(wx.Dialog):
	#running ID for market data tab page
	panelID = 1
	
	def _init_coll_notebook1_Pages(self, parent):
		# generated method, don't edit
		new_page = Panel1(parent, 11, "Page 1" )
		parent.AddPage(imageId=-1, page=new_page, select=True, text=u'Data 1')

	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Dialog.__init__(self, id=wxID_BODY1, name=u'Body1', parent=prnt,
			pos=wx.Point(90, 321), size=wx.Size(395, 381),
			style=wx.DEFAULT_DIALOG_STYLE, title=u'Body')
		self.SetClientSize(wx.Size(387, 354))

		self.spinCtrl1 = wx.SpinCtrl(id=wxID_BODY1SPINCTRL1, initial=0, max=100,
			min=0, name='spinCtrl1', parent=self, pos=wx.Point(144, 24),
			size=wx.Size(117, 21), style=wx.SP_ARROW_KEYS)
		self.spinCtrl1.SetValue(1)
		self.spinCtrl1.SetRange(1, 10)

		self.spinCtrl1.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl1Spinctrl,
			id=wxID_BODY1SPINCTRL1)

		self.button1 = wx.Button(id=wx.ID_OK, label=u'Next',
			name='button1', parent=self, pos=wx.Point(8, 320),
			size=wx.Size(75, 23), style=0)
		self.button1.SetDefault()
		self.button1.SetConstraints(LayoutAnchors(self.button1, True, True,
			False, False))
		self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
			id=wxID_BODY1BUTTON1)

		self.button2 = wx.Button(id=wx.ID_CANCEL, label=u'Cancel',
			name='button2', parent=self, pos=wx.Point(304, 320),
			size=wx.Size(72, 24), style=0)
		self.button2.SetConstraints(LayoutAnchors(self.button2, True, True,
			False, False))
		self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
			id=wxID_BODY1BUTTON2)

		self.staticText1 = wx.StaticText(id=wxID_BODY1STATICTEXT1,
			label=u'Number of Market Data', name='staticText1', parent=self,
			pos=wx.Point(24, 32), size=wx.Size(112, 13), style=0)

		self.notebook1 = wx.Notebook(id=wxID_BODY1NOTEBOOK1, name='notebook1',
			parent=self, pos=wx.Point(16, 72), size=wx.Size(344, 240),
			style=0)
		self.notebook1.SetFitToCurrentPage(False)

		self._init_coll_notebook1_Pages(self.notebook1)

	def __init__(self, parent):
		self._init_ctrls(parent)


	def OnSpinCtrl1Spinctrl(self, event):
		while self.notebook1.GetPageCount() != self.spinCtrl1.GetValue():
			self.panelID +=1
			data_page = Panel1(self.notebook1, self.panelID, "market data")
			if self.notebook1.GetPageCount() < self.spinCtrl1.GetValue():
				self.notebook1.AddPage(data_page, "Data " + str(self.panelID))
			if self.notebook1.GetPageCount() > self.spinCtrl1.GetValue():
				self.notebook1.RemovePage(0)
		event.Skip()

	def OnButton1Button(self, event):
		self.EndModal(1)

	def OnButton2Button(self, event):
		self.EndModal(2)

	def GetMarketData(self):
		soh = "\x01"
		message = ""
		page_count = self.notebook1.GetPageCount()
		for i in range(page_count):
			page = self.notebook1.GetPage(i)
			tag_279 = "279=" + str(page.choice1.GetSelection())
			if page.choice2.GetSelection ==3:
				tag_269 = "269=J"
			else:
				tag_269 = "269="+ str(page.choice2.GetSelection())
			tag_270 = "270=" + str(page.numCtrl1.GetValue())
			tag_271 = "271=" + str(page.intCtrl1.GetValue())
			tag_55 = "55=" + page.textCtrl1.GetValue()
			tag_278 = "278="+ str(self.panelID)
			message = message + tag_279 + soh + tag_269 + soh + tag_270 + soh + tag_271 + soh + tag_55 + soh + tag_278 + soh
		print message
		return "268="+ str(page_count) + soh + message
#Boa:FramePanel:Panel1

[wxID_PANEL1, wxID_PANEL1CHOICE1, wxID_PANEL1CHOICE2, wxID_PANEL1INTCTRL1, 
wxID_PANEL1NUMCTRL1, wxID_PANEL1SCROLLEDWINDOW1, wxID_PANEL1STATICTEXT2, 
wxID_PANEL1STATICTEXT3, wxID_PANEL1STATICTEXT4, wxID_PANEL1STATICTEXT5, 
wxID_PANEL1STATICTEXT6, wxID_PANEL1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Panel1(wx.Panel):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Panel.__init__(self, id=wxID_PANEL1, name='', parent=prnt,
			pos=wx.Point(724, 380), size=wx.Size(308, 205),
			style=wx.TAB_TRAVERSAL)
		self.SetClientSize(wx.Size(300, 178))

		self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_PANEL1SCROLLEDWINDOW1,
			name='scrolledWindow1', parent=self, pos=wx.Point(0, 0),
			size=wx.Size(336, 214), style=wx.HSCROLL | wx.VSCROLL)

		self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_PANEL1NUMCTRL1,
			name='numCtrl1', parent=self.scrolledWindow1, pos=wx.Point(80,
			72), size=wx.Size(99, 22), style=0, value=0)
		self.numCtrl1.SetAllowNegative(False)
		self.numCtrl1.SetDefaultValue(u'0.0')
		self.numCtrl1.SetHelpText(u'Price for security')

		self.staticText6 = wx.StaticText(id=wxID_PANEL1STATICTEXT6,
			label=u'Security', name='staticText6',
			parent=self.scrolledWindow1, pos=wx.Point(0, 136),
			size=wx.Size(39, 13), style=0)

		self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4,
			label=u'Entry Price', name='staticText4',
			parent=self.scrolledWindow1, pos=wx.Point(0, 72), size=wx.Size(56,
			13), style=0)

		self.staticText5 = wx.StaticText(id=wxID_PANEL1STATICTEXT5,
			label=u'Entry Quantity', name='staticText5',
			parent=self.scrolledWindow1, pos=wx.Point(0, 104),
			size=wx.Size(71, 16), style=0)

		self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2,
			label=u'Entry Action', name='staticText2',
			parent=self.scrolledWindow1, pos=wx.Point(0, 16), size=wx.Size(59,
			13), style=0)

		self.choice1 = wx.Choice(choices=['New', 'Change', 'Delete'],
			id=wxID_PANEL1CHOICE1, name='choice1',
			parent=self.scrolledWindow1, pos=wx.Point(80, 8),
			size=wx.Size(130, 21), style=0)
		self.choice1.SetLabel(u'')

		self.choice2 = wx.Choice(choices=['Bid', 'Ask', 'Trade', 'Empty Book'],
			id=wxID_PANEL1CHOICE2, name='choice2',
			parent=self.scrolledWindow1, pos=wx.Point(80, 40),
			size=wx.Size(136, 21), style=0)

		self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3,
			label=u'Entry Type', name='staticText3',
			parent=self.scrolledWindow1, pos=wx.Point(0, 40), size=wx.Size(53,
			13), style=0)

		self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
			allow_none=False, default_color=wx.BLACK, id=wxID_PANEL1INTCTRL1,
			limited=False, max=None, min=None, name='intCtrl1',
			oob_color=wx.RED, parent=self.scrolledWindow1, pos=wx.Point(80,
			104), size=wx.Size(132, 21), style=0, value=0)

		self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL1, name='textCtrl1',
			parent=self.scrolledWindow1, pos=wx.Point(80, 136),
			size=wx.Size(100, 21), style=0, value=u'Tag 55')

		
	def __init__(self, parent, id, name):
		self._init_ctrls(parent)
