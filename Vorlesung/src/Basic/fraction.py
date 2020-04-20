#!/usr/bin/env python3

from gcd import gcd
import sys

class Fraction:
  def __init__(self,top,bottom):
    common = gcd(top,bottom)
    self.num = top//common  # integer division
    self.den = bottom//common

  def __str__(self):    # overload str
    if self.den == 1:
      return '{}'.format(self.num)
    else:
      return '{}/{}'.format(self.num,self.den)

  def __add__(self,o_frac):    # overload +
    newnum = self.num * o_frac.den + self.den * o_frac.num
    newden = self.den * o_frac.den
    return Fraction(newnum,newden)

  def __eq__(self, other):   # overload ==
    return self.num == other.num and self.den == other.den

def run_test():
  print('8/4={}'.format(Fraction(8,4)))
  frac1 = Fraction(13,30)
  frac2 = Fraction(1,15)
  frac3 = frac1 + frac2
  print('13/30 + 1/15={}'.format(frac3))
  frac4 = Fraction(4,8)
  if frac3 != frac4:
    sys.stderr.write('frac3 == {} != {} = frac4 not expected\n'
                      .format(frac3,frac4))
    exit(1)

if __name__ == '__main__':
  run_test()
