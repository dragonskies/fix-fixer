from wxPython.wx import *
from wxPython.html import *
import os,sys

class exHtmlWindow(wxHtmlWindow):
   def __init__(self, parent, id, frame):
      wxHtmlWindow.__init__(self,parent,id)

class exHtmlPanel(wxPanel):
   def __init__(self, parent, id, frame):
      wxPanel.__init__(self, parent, -1)
      self.frame = frame
      self.cwd = os.path.split(sys.argv[0])[0]
      if not self.cwd:
         self.cwd = os.getcwd

      self.html = exHtmlWindow(self, -1, self.frame)

      self.box = wxBoxSizer(wxVERTICAL)
      self.box.Add(self.html, 1, wxGROW)

      subbox = wxBoxSizer(wxHORIZONTAL)

      btn = wxButton(self, 1202, "Load File")
      EVT_BUTTON(self, 1202, self.OnLoadFile)
      subbox.Add(btn, 1, wxGROW | wxALL, 2)

      btn = wxButton(self, 1203, "Load Page")
      EVT_BUTTON(self, 1203, self.OnLoadPage)
      subbox.Add(btn, 1, wxGROW | wxALL, 2)

      btn = wxButton(self, 1204, "Back")
      EVT_BUTTON(self, 1204, self.OnBack)
      subbox.Add(btn, 1, wxGROW | wxALL, 2)

      btn = wxButton(self, 1205, "Forward")
      EVT_BUTTON(self, 1205, self.OnForward)
      subbox.Add(btn, 1, wxGROW | wxALL, 2)

      self.box.Add(subbox, 0, wxGROW)
      self.SetSizer(self.box)
      self.SetAutoLayout(true)

   def OnLoadPage(self, event):
      dlg = wxTextEntryDialog(self, 'Location:')
      if dlg.ShowModal() == wxID_OK:
         self.destination = dlg.GetValue()
      dlg.Destroy()
      self.html.LoadPage(self.destination)

   def OnLoadFile(self, event):
      dlg = wxFileDialog(self, wildcard = '*.htm*', style=wxOPEN)
      if dlg.ShowModal():
         path = dlg.GetPath()
         self.html.LoadPage(path)
      dlg.Destroy()

   def OnBack(self, event):
      if not self.html.HistoryBack():
         wxMessageBox("No more items in history!")

   def OnForward(self, event):
      if not self.html.HistoryForward():
         wxMessageBox("No more items in history!")

class exFrame (wxFrame):
   def __init__(self, parent, ID, title):
      wxFrame.__init__(self,parent,ID,title,wxDefaultPosition,wxSize(600,750))
      panel = exHtmlPanel(self, -1, self)

class exApp(wxApp):
   def OnInit(self):
      frame = exFrame(NULL, -1, "Example Browser")
      frame.Show(true)
      self.SetTopWindow(frame)
      return true

app = exApp(0)
app.MainLoop()