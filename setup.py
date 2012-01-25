from distutils.core import setup
import py2exe
import os
import sys

setup(
	windows=[
		{
			"script": 'fixfixer_main.py',
			"icon_resources":[(1, "fix-fixer.ico")]
		}
	]
)

os.chdir('dist')
try:
	os.remove('fixfixer_gui.exe')
except:
	pass
os.rename( 'fixfixer_main.exe', 'fixfixer_gui.exe')
os.chdir('..')