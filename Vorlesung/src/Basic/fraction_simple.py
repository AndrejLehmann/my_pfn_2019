#!/usr/bin/env python3

class FractionSimple:
  def __init__(self,top,bottom):
    self.num = top
    self.den = bottom

  def tostring(frac):
    return '{}/{}'.format(frac.num,frac.den)

  def add(f1,f2):
    newnum = f1.num * f2.den + f1.den * f2.num # numerator of (2)
    newden = f1.den * f2.den                   # denominator of (2)
    return FractionSimple(newnum,newden)

frac1 = FractionSimple(13,30)
frac2 = FractionSimple(1,15)

frac3 = FractionSimple.add(frac1,frac2)  # frac1=13/30, frac2=1/15

print('{} + {} = {}'
      .format(FractionSimple.tostring(frac1),
              FractionSimple.tostring(frac2),
              FractionSimple.tostring(frac3)))
