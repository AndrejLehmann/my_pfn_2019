#!/usr/bin/env python3

from funcdefs import velocity
from prepare_plot import prepare_plot_data
from math import floor

x_min = 0.0
x_max = 1.0
numpoints = 100
x_list, y_list = prepare_plot_data(velocity, x_min, x_max, numpoints)
y_min = min(y_list)
y_max = max(y_list)

import matplotlib.pyplot as plt
plt.switch_backend('agg') # to allow remote use

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('$t$')
ax.set_ylabel('$v(t)$')
ax.grid(True)
ax.set_xlim(x_min,x_max)
ax.set_ylim(min(0.0,y_min),floor(y_max+1.0))
ax.set_title('$v(t)=3t^{2}\mathrm{e}^{t^{3}}$',# LaTeX
             fontsize=12, color='black')
ax.plot(x_list, y_list, color='blue', label='$v(t)$')
ax.legend(loc='upper left')
fig.savefig('velocityplot.pdf')
