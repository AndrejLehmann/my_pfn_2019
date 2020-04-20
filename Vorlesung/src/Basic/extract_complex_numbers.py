#!/usr/bin/env python3

import re

cnp = ' (-3.1, 4) ' # complex number as pair
m = re.search(r'\(\s*([^,]+)\s*,\s*([^\)]+)\s*\)', cnp)
if m:
  a, b = float(m.group(1)), float(m.group(2))
  print('{}+{}i'.format(a,b))

m = cnp.strip()[1:-1].split(',') # m is list of length 2
a, b = float(m[0]), float(m[1])
print('{}+{}i'.format(a,b))

a, b = eval(cnp)
print('{}+{}i'.format(a,b))
