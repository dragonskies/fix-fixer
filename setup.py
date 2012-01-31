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
	os.chdir('dist')

	for file in dependencies:
		if os.path.isfile(file):
			try:
				print "removing " + os.path.abspath(file)
				os.remove(file)
			except Exception:
				print "The file " + file + " could not be removed.  Is it in use, or is the path read-only?"
				return False
	os.chdir('..')
	
	for file in dependencies:
		if os.path.isfile(file):
			try:
				print "copying " + os.path.abspath(file)
				shutil.copyfile(file, os.path.join('dist', file))
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
	setup(
		windows=[
			{
				"script": 'fixfixer_main.py',
				"icon_resources":[(1, "fix-fixer.ico")]
			}
		]
	)

	post_install()