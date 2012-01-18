from distutils.core import setup
import py2exe
import os
import sys

setup(windows=['fixfixer_main.py'])

os.chdir('dist')
try:
	os.remove('fixfixer_gui.exe')
except:
	pass
os.rename( 'fixfixer_main.exe', 'fixfixer_gui.exe')
os.chdir('..')