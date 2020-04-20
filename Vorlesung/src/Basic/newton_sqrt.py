#!/usr/bin/env python3

# http://www.pythontutor.com/visualize.html#code=def%20newton_sqrt%28r,its%20%3D%2010%29%3A%0A%20%20%20%20x%20%3D%20r/2%0A%20%20%20%20for%20i%20in%20range%28its%29%3A%0A%20%20%20%20%20%20%20%20x%20%3D%200.5%20*%20%28x%20%2B%20r%20/%20x%29%0A%20%20%20%20return%20x%0A%20%20%20%20%0Afrom%20math%20import%20sqrt%0Afor%20r%20in%20%5B12345.0,83235.9,93483.2%5D%3A%0A%20%20%20%20print%28'sqrt%28%7B%7D%29%3A%20newton%3D%7B%3A.14f%7D'.format%28r,newton_sqrt%28r%29%29%29&cumulative=false&curInstr=57&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def newton_sqrt(r,its = 20): # number of iterations
  x = r/2   # x_{0}: initial guess of sqrt(r)
  for i in range(its): # i = 0, .., its - 1
    x = 0.5 * (x + r / x)
  return x

from math import sqrt

for r in [12345.0,83235.9,93483.2]:
  print('sqrt({}): newton={:.14f}\n{}python={:.14f}'
         .format(r,newton_sqrt(r),' ' * 15,sqrt(r)))
