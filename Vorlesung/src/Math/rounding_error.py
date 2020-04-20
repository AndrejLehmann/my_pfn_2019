#!/usr/bin/env python3
import math

'''
>>> a = 1; b = 2; expected = 3;
>>> a + b == expected

>>> a = 0.1; b = 0.2; expected = 0.3
>>> a + b == expected

>>> fs = '{:.17f}\n' * 4
>>> print(fs.format(0.1,0.2,0.1 + 0.2,0.3))

>>> a = 0.1; b = 0.2; expected = 0.3; computed = a + b
>>> diff = abs(expected - computed)
>>> tol = 1e-15
>>> diff < tol
'''

def difference(k):
  return 10**k + 0.3 - (10**k + 0.1 + 0.2)

for k in range(1,10+1):
  print('{:>2d}\t{:>+.17f}\t{:>.17f}'
         .format(k,difference(k),10.0 ** (k-16)))

for k in range(1,10+1):
  d = difference(k)
  v = 10**k + 0.3
  print('{:>2d}\t{:.2g}'
        .format(k,d/v))
