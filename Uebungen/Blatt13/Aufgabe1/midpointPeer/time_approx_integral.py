#!/usr/bin/env python3

from timeit import Timer
from approx_integral import approx_integral_trpz, \
                            np_approx_integral_trpz
from funcdefs import velocity, np_velocity
from functools import partial

def runtime_get(func,*args):
  partial_object = partial(func,*args)
  times = Timer(partial_object).repeat(3,1)
  return min(times)

p = 0.0
q = 1.0
n = 10000000
t = runtime_get(approx_integral_trpz,
                velocity,p,q,n)
print('runtime approx_integral_trpz: {:.2f} s'
       .format(t))
t = runtime_get(np_approx_integral_trpz,
                np_velocity,p,q,n)
print('runtime np_approx_integral_trpz: {:.2f} s'
       .format(t))
