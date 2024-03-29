#Boa:Dialog:Dialog1

import wx
import wx.lib.masked.numctrl

def create(parent):
	return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1BUTTON3, 
wxID_DIALOG1NOTEBOOK1, wxID_DIALOG1SPINCTRL1, wxID_DIALOG1STATICTEXT1, 
wxID_DIALOG1WINDOW1, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Dialog1(wx.Dialog):
	panelID = 1
	
	def _init_coll_notebook1_Pages(self, parent):
		# generated method, don't edit
		new_page = Panel1(parent, 11, "Page 1" )
		parent.AddPage(imageId=-1, page=new_page, select=True, text=u'Leg 1')

		#parent.AddPage(imageId=-1, page=self.window1, select=True,text=u'Leg 1')

	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
			pos=wx.Point(19, 616), size=wx.Size(420, 326),
			style=wx.DEFAULT_DIALOG_STYLE, title=u'Legs')
		self.SetClientSize(wx.Size(412, 299))

		self.spinCtrl1 = wx.SpinCtrl(id=wxID_DIALOG1SPINCTRL1, initial=1,
			max=2, min=1, name='spinCtrl1', parent=self, pos=wx.Point(160,
			16), size=wx.Size(117, 21), style=wx.SP_ARROW_KEYS)
		
		self.spinCtrl1.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl1Spinctrl,
			id=wxID_DIALOG1SPINCTRL1)

		self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
			label=u'Number of Legs', name='staticText1', parent=self,
			pos=wx.Point(72, 16), size=wx.Size(75, 13), style=0)

		self.button1 = wx.Button(id=wx.ID_OK, label=u'Ok',
			name='button1', parent=self, pos=wx.Point(24, 256),
			size=wx.Size(75, 23), style=0)
		self.button1.SetDefault()
		self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
			id=wxID_DIALOG1BUTTON1)


		self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label=u'Back',
			name='button2', parent=self, pos=wx.Point(168, 256),
			size=wx.Size(75, 23), style=0)
		self.button2.SetAutoLayout(True)
		self.button2.Center(wx.HORIZONTAL)
		#self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
		#	id=wxID_DIALOG1BUTTON1)

		self.button3 = wx.Button(id=wx.ID_CANCEL, label=u'Cancel',
			name='button3', parent=self, pos=wx.Point(312, 256),
			size=wx.Size(75, 23), style=0)
		self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
			id=wxID_DIALOG1BUTTON1)

		self.notebook1 = wx.Notebook(id=wxID_DIALOG1NOTEBOOK1, name='notebook1',
			parent=self, pos=wx.Point(16, 48), size=wx.Size(376, 192),
			style=0)
		self.notebook1.SetFitToCurrentPage(False)
		
		self._init_coll_notebook1_Pages(self.notebook1)

	def OnSpinCtrl1Spinctrl(self, event):
		data_page = Panel1(self.notebook1, self.panelID, "leg info")
		while self.notebook1.GetPageCount() != self.spinCtrl1.GetValue():
			if self.notebook1.GetPageCount() < self.spinCtrl1.GetValue():
				self.notebook1.AddPage(data_page, "Leg " + str(self.panelID))
				self.panelID +=1
			if self.notebook1.GetPageCount() > self.spinCtrl1.GetValue():
				self.notebook1.RemovePage(0)
			
	def OnButton1Button(self, event):
		self.EndModal(1)

	def OnButton2Button(self, event):
		self.EndModal(2)
	
	def OnButton3Button(self, event):
		self.EndModal(3)
		
	def GetLegInformation(self):
		soh = "\x01"
		message = ""
		page_count = self.notebook1.GetPageCount()
		for i in range(page_count):
			page = self.notebook1.GetPage(i)
			tag_556="556="+page.textCtrl1.GetValue()
			if page.choice1.GetSelection() ==0:
				tag_600="600=FIXED"
			else:
				tag_600="600=FLOAT"
			date_selected = page.datePickerCtrl1.GetValue()
			tag_249="249="+str(date_selected.GetYear())+str(date_selected.GetMonth())+str(date_selected.GetDay())
			tag_252="252="+str(page.numCtrl1.GetValue())
			message = message + tag_556 + soh + tag_600 + soh + tag_249 + soh + tag_252 + soh
		tag_555="555="+str(i)
		leg_message =tag_555 + soh + message
		return leg_message
	
	def __init__(self, parent):
		self._init_ctrls(parent)


#Boa:FramePanel:Panel1

import wx
import wx.lib.masked.numctrl

[wxID_PANEL1, wxID_PANEL1CHOICE1, wxID_PANEL1DATEPICKERCTRL1, 
wxID_PANEL1NUMCTRL1, wxID_PANEL1STATICTEXT1, wxID_PANEL1STATICTEXT2, 
wxID_PANEL1STATICTEXT3, wxID_PANEL1STATICTEXT4, wxID_PANEL1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Panel1(wx.Panel):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Panel.__init__(self, id=wxID_PANEL1, name='', parent=prnt,
			pos=wx.Point(606, 566), size=wx.Size(253, 178),
			style=wx.TAB_TRAVERSAL)
		self.SetClientSize(wx.Size(245, 151))

		self.staticText1 = wx.StaticText(id=wxID_PANEL1STATICTEXT1,
			label=u'Leg Symbol', name='staticText1', parent=self,
			pos=wx.Point(40, 24), size=wx.Size(54, 13), style=0)

		self.staticText2 = wx.StaticText(id=wxID_PANEL1STATICTEXT2,
			label=u'Leg Currency', name='staticText2', parent=self,
			pos=wx.Point(32, 56), size=wx.Size(64, 13), style=0)

		self.staticText3 = wx.StaticText(id=wxID_PANEL1STATICTEXT3,
			label=u'Leg Issue Date', name='staticText3', parent=self,
			pos=wx.Point(24, 88), size=wx.Size(72, 16), style=0)

		self.choice1 = wx.Choice(choices=['FIXED', 'FLOAT'], id=wxID_PANEL1CHOICE1,
			name='choice1', parent=self, pos=wx.Point(104, 16),
			size=wx.Size(130, 21), style=0)
		self.choice1.SetStringSelection(u'FIXED\nFLOAT')

		self.textCtrl1 = wx.TextCtrl(id=wxID_PANEL1TEXTCTRL1, name='textCtrl1',
			parent=self, pos=wx.Point(104, 48), size=wx.Size(128, 21),
			style=0, value='textCtrl1')

		self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_PANEL1DATEPICKERCTRL1,
			name='datePickerCtrl1', parent=self, pos=wx.Point(104, 80),
			size=wx.Size(128, 21), style=wx.DP_SHOWCENTURY)

		self.numCtrl1 = wx.lib.masked.numctrl.NumCtrl(id=wxID_PANEL1NUMCTRL1,
			name='numCtrl1', parent=self, pos=wx.Point(104, 112),
			size=wx.Size(128, 22), style=0, value=0)

		self.staticText4 = wx.StaticText(id=wxID_PANEL1STATICTEXT4,
			label=u'Leg Purchase Rate', name='staticText4', parent=self,
			pos=wx.Point(8, 120), size=wx.Size(90, 13), style=0)
	def __init__(self, parent, id, name):
		self._init_ctrls(parent)
