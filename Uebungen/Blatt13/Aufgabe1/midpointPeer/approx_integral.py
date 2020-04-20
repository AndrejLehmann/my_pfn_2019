#!/usr/bin/env python3
import math, argparse

def approx_line_length(f,p,q,n):
  total = 0.0
  x1 = p
  fx1 = f(x1)
  d = (q - p)/n
  d_square = d * d

  for i in range(n):
    fx2 = f(x1 + d) # x1 + d = p + d * i
    dy = fx2 - fx1

    total += math.sqrt(d_square + dy * dy)
    fx1 = fx2  # reuse fx2 as fx1 in next iteration
    x1 += d    # x1 becomes p + d * i
  return total

def approx_integral_trpz(f,p,q,n):
  fsum = 0.0
  d = (q - p)/n
  for i in range(1,n):
    fsum += f(p + i * d)
  return d * (0.5 * (f(p) + f(q)) + fsum)

def approx_integral_trpz_print(f,p,q,maxsteps,expected = None):
  n = 10
  numerical = None # as we use it after the loop
  while n <= maxsteps:
    numerical = approx_integral_trpz(f,p,q,n)
    print('n = {:7d}, integral({},{:.1f},{:.1f}) = {:.6f}'
           .format(n,f.__name__,p,q,numerical))
    n *= 10
  if expected and numerical:
    equality = '==' if expected == numerical else '!='
    print('numerical = {:.8f} {} {:.8f} = expected'
           .format(numerical,equality,expected))

def approx_integral_trpz_test(f,p,q,n,expected):
  numerical = approx_integral_trpz(f,p,q,n)
  absdiff = abs(expected - numerical)
  reldiff = absdiff/expected
  abstol = 1e-14
  if absdiff >= abstol:
    sys.stderr.write('error={:g} >= {:g} = abstol\n'
                      .format(absdiff,abstol))
    sys.stderr.write('reldiff={:g}\n'.format(reldiff))

def approx_integral_mid(f,p,q,n):
  fsum = 0.0
  d = (q - p)/n
  for i in range(0,n):
    fsum += f(p + i * d + d/2)
  return d * fsum

def approx_integral_generic_print(imethod,f,p,q,maxsteps,expected):
  print('method: {}, integral({},{},{}):'
         .format(imethod.__name__,f.__name__,p,q))
  n = 10
  while n <= maxsteps:
    numerical = imethod(f,p,q,n)
    diff = expected - numerical
    print('n = {:7d}, numerical = {:.6f}, diff={:.2e}'
           .format(n,numerical,diff))
    n *= 10

import numpy as np

def np_approx_integral_trpz(f, p, q, n):
  d = (q-p)/n
  x_array = np.linspace(p + d, q - d, n-1)
  return d * (0.5 * (f(p) + f(q)) + np.sum(f(x_array)))

def np_approx_integral_mid(f, p, q, n):
  d = (q-p)/n
  x_array = np.linspace(p + d/2, q - d/2, n)
  return d * np.sum(f(x_array))

def positive_int(s):
  try: # may raise exception ValueError in int conversion
    value = int(s)
  except ValueError: # handle exception
    raise argparse.ArgumentTypeError('{} is not a positive integer\n'.format(s))
  if value < 1:
    raise argparse.ArgumentTypeError('{} is not a positive integer\n'.format(s))

def parse_arguments():
  default_maxsteps = 1000000
  p = argparse.ArgumentParser(description='run numerical integration methods')
  p.add_argument('-m','--maxsteps',metavar='<positive int>',
                 type=positive_int,default=default_maxsteps,
                 help='specify integer, default is {}'.format(default_maxsteps))
  return p.parse_args()

if __name__ == '__main__':
  import sys
  from funcdefs import curvedM, velocity, velocity_anti_derivative

  args = parse_arguments()
  maxsteps = args.maxsteps

  approx_integral_trpz_print(curvedM,0.0,4.0,maxsteps)

  expected =  velocity_anti_derivative(1.0) - \
              velocity_anti_derivative(0.0)

  approx_integral_trpz_print(velocity,0.0,1.0,maxsteps,expected)

  approx_integral_generic_print(approx_integral_trpz,velocity,
                                0.0,1.0,maxsteps,expected)
  print('{}expected = {:.6f}'.format(' ' * 14,expected))


  approx_integral_generic_print(approx_integral_mid,velocity,
                                0.0,1.0,maxsteps,expected)
  print('{}expected = {:.6f}'.format(' ' * 14,expected))

  from funcdefs import np_velocity

  approx_integral_generic_print(np_approx_integral_mid,np_velocity,0.0,1.0,
                                maxsteps,expected)
  print('{}expected = {:.6f}'.format(' ' * 14,expected))

  approx_integral_generic_print(np_approx_integral_trpz,np_velocity,0.0,1.0,
                                maxsteps,expected)
  print('{}expected = {:.6f}'.format(' ' * 14,expected))
