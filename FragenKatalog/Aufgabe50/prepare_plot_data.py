#!/usr/bin/env python3

import numpy as np

def  prepare_plot_data(f, x_min, x_max, numpoints):
    stepwidth = ( x_max - x_min ) / numpoints
    x_list = [ x_min + p * stepwidth for p in range(numpoints+1) ]
    y_list = [ f(x) for x in x_list]
    #y_list = f(np.array(x_list))  # !!! geht nur mit numpy
    return x_list, y_list


def f(x):
    return x**2


print(prepare_plot_data(f, 0, 2, 4))
