#!/usr/bin/env python3

''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``linear function``
Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve iplot_linear.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/iplot_linear

in your browser.
'''

from interactive_plot import InteractivePlot

def linear_function(args,x):
  return args[1] + args[0] * x

sliders_spec = [('slope ','a',0,8,1),('shift ','b',0,5,0)]
title = 'f(x) = a * x + b'
InteractivePlot(title,0,6,'red',linear_function,sliders_spec)
