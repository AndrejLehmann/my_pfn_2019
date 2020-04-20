#!/usr/bin/env python3
def updatepop(a,b):
  print('in func:     a = {}'.format(a))
  print('in func:     b = {}'.format(b))
  a[0] = '2'
  b.pop(0)

a = ['1','3']
b = ['a','b']

print('before call: a = {}'.format(a))
print('before call: b = {}'.format(b))

updatepop(a,b)

print('after call:  a = {}'.format(a))
print('after call:  b = {}'.format(b))
