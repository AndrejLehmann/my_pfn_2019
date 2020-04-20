#!/usr/bin/env python3

''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the plotted function
Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve iplot_quadratic.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/iplot_quadratic

in your browser.
'''

from interactive_plot import InteractivePlot

def quadratic_function(args,x):
  return args[0] * x * x + args[1] * x + args[2]

sliders_spec = [('','a',0,4,1),('','b',0,16,1),('','c',0,64,1)]
title = 'f(x) = a * x^{2} + b * x + c'
InteractivePlot(title,0,6,'blue',quadratic_function,sliders_spec)
