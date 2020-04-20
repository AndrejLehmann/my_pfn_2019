#!/usr/bin/env python3

from funcdefs import curvedM
import math

x_min = 0.0
x_max = 4.0
numpoints = 10000
stepwidth = \
 (x_max - x_min)/numpoints
x_list = list()
y_list = list()
for p in range(numpoints+1):
  x = x_min + p * stepwidth
  x_list.append(x)
  y_list.append(curvedM(x))
y_min = min(y_list)
y_max = max(y_list)

import matplotlib.pyplot as plt
plt.switch_backend('agg') # to allow remote use

fig, ax = plt.subplots(figsize=(10, 6.18)) # golden section
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(x_min,x_max)
ax.set_ylim(min(0.0,y_min),math.floor(y_max+1.0))
ax.set_title('$f(x)=2+\sin(5x)+\cos(10x)+x^{2}/10$',  # LaTeX
             fontsize=12, color='black')
ax.plot(x_list, y_list, color='blue',label='$f(x)$')
ax.legend(loc='upper left')
fig.savefig('curvedMplot.pdf')
