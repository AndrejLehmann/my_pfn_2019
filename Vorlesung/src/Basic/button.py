#!/usr/bin/env python3

from tkinter import *

def out():
  print('hello') # the button calls this function
Button(root, text='Hello!', font='Times 16', command=out).pack()
