#!/usr/bin/env python3

from math import sin

def factorial(x):
  prod = 1
  for i in range(1,x):
    prod *= i
  return prod

def sin_approx1(x,stop):
  sinval = x
  neg = True
  for e in range(3,stop,2):
    if neg:
      sinval -= (x**e)/factorial(e)
      neg = False
    else:
      sinval += (x**e)/factorial(e)
      neg = True
  return sinval

stop = 100
for x in [0.1,0.2,0.3]:
  print('sin({}): our={:.14f}\n{}python={:.14f}'
         .format(x,sin_approx1(x,stop),' ' * 7,sin(x)))
