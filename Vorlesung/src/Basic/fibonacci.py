#!/usr/bin/env python3

def arith(x):  # generates two values
  yield x + 1  # first this
  yield x * 2  # then this

for y in arith(5):   # iterate over the generated values
  print(y)

def fib_up_to(maxfib):
  p = pp = 1  # p is previous, pp is previous of previous
  while pp <= maxfib:
    yield pp   # iteration will receive pp as value
    current_sum = p + pp
    pp = p
    p = current_sum

for f in fib_up_to(1000): # use function as iterator
  print('{} '.format(f),end='')  # f will be yielded value
print()

def fib_infinite():
  p = pp = 1  # p is previous, pp is previous of previous
  while True:
    yield pp   # iteration will receive pp as value
    current_sum = p + pp
    pp = p
    p = current_sum

for f in fib_infinite(): # use function as iterator without limit
  if f > 1000:           # f is yielded value
    break
  print('{} '.format(f),end='')
print()

class Fib:
  def __init__(self):
    return
  def __iter__(self):
    self.a = 1
    self.b = 1
    return self
  def __next__(self):
    fib = self.a
    self.a, self.b = self.b, self.a + self.b
    return fib

for f in Fib():
  if f > 1000:
    break
  print('{} '.format(f), end='')
print()
