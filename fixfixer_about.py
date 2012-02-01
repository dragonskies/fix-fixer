import wx

class AboutFixFixer(wx.AboutDialogInfo):
    """About Dialog for Fix Message fixer"""
    def __init__(self, parent):
        wx.AboutDialogInfo.__init__(self)
        self.parent = parent
        self.artists = ["Icons from Tango Desktop Project <http://tango.freedesktop.org/>"]
        self.copyright = "\xa9 2012 Timothy Davis"
        self.description = "Message editor for the FIX Protocol <http://fixprotocol.org/>"
        self.developers = ["Timothy Davis", "Sean Davis"]
        self.docwriters = ["Timothy Davis"]
        self.icon = "fix-fixer.ico"
        self.license = ""
        self.name = "Fix Message fixer"
        self.translators = [""]
        self.version = "0.1"
        self.website = ("http://code.google.com/p/fix-fixer/", "Fix Fixer Website")
        self.SetProperties()

    def SetProperties(self):
        self.SetArtists(self.artists)
        self.SetCopyright(self.copyright)
        self.SetDescription(self.description)
        self.SetDevelopers(self.developers)
        self.SetDocWriters(self.docwriters)
        self.SetIcon( wx.Icon(self.icon, wx.BITMAP_TYPE_ICO) )
        self.SetLicense(self.license)
        self.SetName(self.name)
#      self.SetTranslators(self.translators)
        self.SetVersion(self.version)
        self.SetWebSite(self.website)

    def show(self):
        wx.AboutBox(self)

