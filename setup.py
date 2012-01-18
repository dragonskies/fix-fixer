from distutils.core import setup
import py2exe
import os

os.remove('fixfixer_gui.exe')

setup(console=['fixfixer_main.py'])

os.chdir('dist')
os.remove('fixfixer_gui.exe')
os.rename( 'fixfixer_main.exe', 'fixfixer_gui.exe')
os.chdir('..')