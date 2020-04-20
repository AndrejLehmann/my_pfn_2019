#!/usr/bin/env python3

''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the plotted function
Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve iplot_normal.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/iplot_normal

in your browser.
'''

from interactive_plot import InteractivePlot
from normal_pdf import normalProbabilityDensity

def normal_func(args,x):
  assert len(args) == 2
  mean = args[0]
  stddev = args[1]
  return normalProbabilityDensity(mean,stddev,x)

x_min = -3
x_max = 3
stddev_min = 0.5
stddev_max = 1.5
default_mean = x_min + (x_max - x_min)/2
default_stddev = stddev_min + (stddev_max - stddev_min)/2
sliders_spec = [('','mean',x_min+1,x_max-1,default_mean),
                ('','stddev',stddev_min,stddev_max,default_stddev)]
title = 'normal_pdf(x)'
InteractivePlot(title,x_min,x_max,'blue',normal_func,sliders_spec)
