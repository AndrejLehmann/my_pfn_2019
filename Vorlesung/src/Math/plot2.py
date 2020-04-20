#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

def f(t):
    return t * t

t = np.arange(-4,4,1/40.)
section = np.arange(-1, 1, 1/20.)
fig, ax = plt.subplots()
ax.fill_between(section,f(section))
ax.plot(t,f(t))
fig.savefig('plot2.pdf')
