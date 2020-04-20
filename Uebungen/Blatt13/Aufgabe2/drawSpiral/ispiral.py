#!/usr/bin/env python3

# execute as
# bokeh serve ispiral.py

import math
from interactive_plot2 import InteractivePlot2
from spiral_coords import spiral_coords

golden_section = (1 + math.sqrt(5.0))/2.0

sliders_spec = [('radius ','r',0.5,1,1,0.01),
                ('divisor ','d',1.005,1.7,golden_section,0.005),
                ('quarters ','q',1,250,16,1),
                ('density ','p',20,200,20,1)]

def spiral_coords_args(args):
  origin = (1.0,1.0)
  radius = args[0]
  divisor = args[1]
  quarters = round(args[2])
  density = args[3]
  return spiral_coords(origin,radius,divisor,quarters,density)

InteractivePlot2('Spiral','red',spiral_coords_args,sliders_spec)
