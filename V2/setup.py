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

from distutils.core import setup
import py2exe
import os
import sys
import shutil

def remove_executables():
	print "\n*** remove old executables ***"
	success = True
	executables = ['fixfixer_main.exe', 'fixfixer_gui.exe']
	os.chdir('dist')
	for exe in executables:
		if os.path.isfile(exe):
			try:
				print "removing " + os.path.abspath(exe)
				os.remove(exe)
			except Exception:
				print "The file " + exe + " could not be removed.  Is it in use, or is the path read-only?"
				success = False
	os.chdir('..')
	return success
		

def update_dependencies():
	print "\n*** update dependencies ***"
	dependencies = ['fix-fixer.ico', 'home.png', 'prev.png', 'next.png', 'help.html', 'fix_screenshot.jpg', 'Fields.xml']
	dist_resources = os.path.join('dist', 'resources')
	if not os.path.isdir(dist_resources):
	    os.chdir('dist')
	    os.mkdir('resources')
	    os.chdir('..')
	os.chdir(dist_resources)

	for file in dependencies:
		if os.path.isfile(file):
			try:
				print "removing " + os.path.abspath(file)
				os.remove(file)
			except Exception:
				print "The file " + file + " could not be removed.  Is it in use, or is the path read-only?"
				return False
	os.chdir('..')
	os.chdir('..')

	
	for file in dependencies:
		if os.path.isfile(os.path.join('resources', file)):
			try:
				print "copying " + os.path.abspath(os.path.join('resources',file))
				shutil.copyfile(os.path.join('resources', file), os.path.join(dist_resources, file))
			except Exception:
				print "The file " + file + " could not be copied.  Is the write path read-only?"
				return False
		else:
			print "The file " + file + " could not be found.  Has it been removed?"
			return False
	return True
		
		
def post_install():
	print "\n*** post-installation ***"
	os.chdir('dist')
	print "renaming " + 'fixfixer_main.exe' + " -> " + 'fixfixer_gui.exe'
	os.rename( 'fixfixer_main.exe', 'fixfixer_gui.exe')
	os.chdir('..')
	
	
if remove_executables() and update_dependencies():
	print "\n*** compile binaries ***"
	icopath = os.path.join('resources', 'fix-fixer.ico')
	setup(
        name = "Fix Message Fixer",
        version = "2.0",
        license = "GPL",
        description = "An easy to use FIX message creator/editor for testing messaging systems.",
        options = {"py2exe":{"dll_excludes":["msvcr71.dll", "msvcp90.dll"],
#               "bundle_files":1,           # bundle breaks appearance
               "optimize":2,
               "compressed":True,
               "excludes":['_ssl',  # Exclude _ssl
                        'pyreadline', 'difflib', 'doctest',
                        'optparse', 'pickle', 'calendar'],}},

        zipfile = None,
        author = "Sean Davis, Timothy Davis",
#        copyright = "Timothy Davis 2012",  # tag does not work
		windows=[
			{
				"script": 'fixfixer_main.py',
				"icon_resources":[(0, icopath), (1, icopath)],
			}
		],
		data_files=["msvcp90.dll"],
	)

	post_install()
