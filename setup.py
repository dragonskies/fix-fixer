from distutils.core import setup
import py2exe
import os
import sys

setup(console=['fixfixer_main.py'])

os.chdir('dist')
try:
	os.remove('fixfixer_gui.exe')
except:
	print "Old 'fixfixer_gui.exe' cannot be deleted."
	sys.exit(1)
os.rename( 'fixfixer_main.exe', 'fixfixer_gui.exe')
os.chdir('..')