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
import os

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
        self.icon = os.path.join('resources', 'fix-fixer.ico')
        self.license = ""
        self.name = "Fix Message fixer"
        self.translators = [""]
        self.version = "2.0"
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

