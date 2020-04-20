#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg') # to allow remote use

x = np.linspace(0, 1, 20)
np.random.seed(34214) # for reproducibility
y = np.cos(x) + 0.3 * np.random.rand(20)
if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} True|False\n'.format(sys.argv[0]))
  exit(1)

fig, ax = plt.subplots()
if sys.argv[1] == 'True':
  pdegree = 3
  termlist = list()
  fitted = np.polyfit(x, y, pdegree)
  for idx, f in enumerate(fitted):
    termlist.append('{:.2f} x^{}'.format(f,len(fitted)-idx-1))
  print('fitted coefficients: {}'.format(fitted))
  print('fitted polynom:        {}'.format(' + '.join(termlist)))
  t = np.linspace(0, 1, 200)
  p = np.poly1d(fitted)
  ax.plot(x, y, 'o', t, p(t), '-')
  ax.legend(('measures', 'fitted poly'), loc='upper right')
  fig.savefig('polyfit.png')
else:
  ax.plot(x, y, 'o')
  ax.legend(['measures'], loc='upper right')
  fig.savefig('measures.png')
