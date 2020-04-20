#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
  inputfile = 'DNAfile'
else:
  inputfile = sys.argv[1]

try:
  f = open(inputfile,'r')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0], err))
  exit(1)

def hansen(f):
  dna = f.readlines()
  dna = ''.join(dna)
  dna = dna.lower()
  print(dna, end='')

def kurtz(f):
  for i, x in enumerate(f):
    print('line {}: {}'.format(i, x.lower()), end='')

def changefirstchar(s):
  a = s.split('')
  a[0] = a[0].lower()
  return ''.join(a)

# hansen(f)
kurtz(f)
f.close()
