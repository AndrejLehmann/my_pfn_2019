#!/usr/bin/env python3

import re

a = 'cruel world'
pattern = re.compile(r'(\w+)')
for w in re.findall(pattern, a):
  print('<{}> '.format(w), end='')         # print words in brackets
print('\n', end='')
pattern = re.compile(r'(.)(.)')
for (c, b) in re.findall(pattern, a):
  print('{}{}'.format(b, c), end='')
print('\n', end='')
