#!/usr/bin/env python3

import sys

def gcd_simple(x,y):
  while x % y != 0:
    previous_x = x
    previous_y = y
    x = previous_y
    y = previous_x % previous_y   # % is modulus operator
  return y

def gcd(x,y):
  while x % y != 0:
    previous_x = x
    x = y
    y = previous_x % y
  return y

def expect_gcd(x,y,d):
  if x % d != 0:
    sys.stderr.write('expect x={} % d={} == 0, but it is {}\n'
                      .format(x,d,x % d))
    exit(1)
  if y % d != 0:
    sys.stderr.write('expect y={} % d={} == 0, but it is {}\n'
                      .format(y,d,y % d))
    exit(1)
  if d != gcd(y,x):
    sys.stderr.write('expect d={} == gcd({},{})={}\n'
                      .format(d,y,x,gcd(y,x)))
    exit(1)
  if gcd(x//d,y//d) != 1:   # // is the integer division
    sys.stderr.write('expect gcd(x/d={},y/d={}) == 1, it is {}\n'
                      .format(x//d,y//d,gcd(x//d,y//d)))
    exit(1)

import random
def run_test(trials):
  for i in range(trials):
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    d = gcd(x,y)
    expect_gcd(x,y,d)

if __name__ == '__main__':
  run_test(100000)
