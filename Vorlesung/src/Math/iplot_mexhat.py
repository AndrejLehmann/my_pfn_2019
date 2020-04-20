#!/usr/bin/env python3

from mexhat import mexhat_np

''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``mexican hat function``
Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve iplot_mexhat.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/iplot_mexhat

in your browser.
'''

from interactive_plot import InteractivePlot

'''Computes Mexican hat shape using numpy, see
http://en.wikipedia.org/wiki/Mexican_hat_wavelet'''

def mexhat(args,t):
  sigma = args[0]
  return mexhat_np(sigma,t)

sliders_spec = [('sigma ','sigma',0.8,3,1)]
title = 'mexican hat function for varying sigma'
InteractivePlot(title,-7,7,'red',mexhat,sliders_spec)
