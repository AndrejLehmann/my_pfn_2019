#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <filename>\n'.format(sys.argv[0]))
  exit(1)

try:
  f = open(sys.argv[1], 'r')
except IOError as err:
  print('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

def changefirstchar(s):
  a = list(s)
  a[0] = a[0].lower()
  return ''.join(a)

for x in f.readlines():
  print(changefirstchar(x), end='')
