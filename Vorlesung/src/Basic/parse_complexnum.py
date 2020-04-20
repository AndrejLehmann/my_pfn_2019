#!/usr/bin/env python3

import re

im_re = '(-?\s*\d+)\s*i'
for cs in ['7i-2','4-3i','9 i','-2',\
           '21-14i','-17 i+1']:
  m = re.search(r'{}'.format(im_re),cs)
  if not m:
    b = 0
    a = int(cs)
  else:
    b = int(m.group(1))
    if b < 0:
      b = '({})'.format(b)
    rest = re.sub(r'{}'.format(im_re),'',cs)
    if rest == '':
      a = 0
    else:
      a = int(rest)
  print('{:10s} {}+{}i'.format(cs,a,b))
