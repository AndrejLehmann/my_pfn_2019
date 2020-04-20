#!/usr/bin/env python3

from fraction import *

def faculty(n):
  prod = 1
  for i in range(1,n+1):
    prod *= i
  return prod

def binom(n,k):
  if k < 0:
    sys.stderr.write('binom undefined for k < 0\n')
  elif n < k:
    return Fraction(0,1)
  else:
    return Fraction(faculty(n),faculty(k) * faculty(n-k))

print('binom(49,6)={}'.format(binom(49,6)))
