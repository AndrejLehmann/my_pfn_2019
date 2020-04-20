#!/usr/bin/env python3

import numpy as np

# !!! numpy 596--618
def np_prepare_plot_data(f, x_min, x_max, numpoints):
    x_list = np.linspace(x_min, x_max, numpoints)
    y_list = np.array([f(x)])
    return x_list, y_list
