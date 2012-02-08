import wx
import wx.html

class FixFixerHelpFrame(wx.Frame):
	"""Help Dialog class for Fix Message fixer.  Uses a basic web browser to view
	   The help HTML files."""
	def __init__(self, *args, **kwds):
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		_icon = wx.Icon("fix-fixer.ico", wx.BITMAP_TYPE_ICO)
		self.SetIcon(_icon)

		# Tool Bar
		self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.TB_FLAT | wx.TB_DOCKABLE)
		self.SetToolBar(self.toolbar)
		self.button_home = self.toolbar.AddLabelTool(wx.ID_ANY, "Home", wx.Bitmap("home.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		self.toolbar.AddSeparator()
		self.button_prev = self.toolbar.AddLabelTool(wx.ID_ANY, "Previous", wx.Bitmap("prev.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		self.button_next = self.toolbar.AddLabelTool(wx.ID_ANY, "Next", wx.Bitmap("next.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		# Tool Bar end

		self.SetHome("help.html")
		self.html = wx.html.HtmlWindow(self)
		self.done_show = False
		wx.EVT_IDLE( self, self.OnShow )
		
		self.Bind(wx.EVT_TOOL, self.OnHome, self.button_home)
		self.Bind(wx.EVT_TOOL, self.OnBack, self.button_prev)
		self.Bind(wx.EVT_TOOL, self.OnForward, self.button_next)

		self.__set_properties()
		self.__do_layout()
		
	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle("Help - Fix Message fixer")
		self.SetSize((640, 480))
		self.toolbar.Realize()
		# end wxGlade
		
	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.html, 1, wx.EXPAND, 0)
		self.SetSizer(sizer)
		self.Layout()
		# end wxGlade
		
# ---- Events ------------------------------------------------------- #
		
	def OnShow(self, event):
		"""Event handler for showing items when the frame is made visible."""
		if self.done_show:
			return
		self.done_show = True
		self.html.LoadPage( self.HOME )
		
	def OnHome(self, event):
		"""Event handler for pressing the Home button."""
		self.LoadPage(self.HOME)
		
	def OnBack(self, event):
		"""Event handler for pressing the Back button."""
		if not self.html.HistoryBack():
			wx.MessageBox("No more items in history!")
	
	def OnForward(self, event):
		"""Event handler for pressing the Forward button."""
		if not self.html.HistoryForward():
			wx.MessageBox("No more items in history!")
# ------------------------------------------------------------------- #
		
	def SetHome(self, url):
		self.HOME = url
		
	def LoadPage(self, url):
		self.html.LoadPage(url)
		
	def show(self):
		self.Show()
