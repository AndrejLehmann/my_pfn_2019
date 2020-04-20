#!/usr/bin/env python3

def func1(a, b, c):
  print('{}: {} {} {}'.format(func1.__name__, a, b, c))

func1(1, 2, 3)

def func2(a, b, c=3):
  print('{}: {} {} {}'.format(func2.__name__, a, b, c))

func2(1, 2)
func2(1, 2, 5)

def func3(a, b, *otherargs):
  str_otherargs = ' '.join(map(str,otherargs))
  print('{}: {} {} {}'.format(func3.__name__, a, b, str_otherargs))

func3(1, 2, 3, 4, 5)       # a=1, b=2, otherargs=[3,4,5]
func3(1, 2)                # a=1, b=2, otherargs=[]
