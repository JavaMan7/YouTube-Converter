# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:37:06 2017

@author: Jordan
"""
import os
from cx_Freeze import setup,Executable
os.environ['TCL_LIBRARY'] = r'C:\Users\Jordan\AppData\Local\conda\conda\envs\y2mp3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Jordan\AppData\Local\conda\conda\envs\y2mp3\tcl\tk8.6'
setup(name="y",version=".01",description="parse stuff",executables=[Executable("YouTube converter.py")])