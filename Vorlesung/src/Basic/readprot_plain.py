#!/usr/bin/env python3

filename = 'NM_021964fragment.pep'
print('Try to open "{}"'.format(filename))
stream = openr(filename,'r')

for line in stream:
  print('next line is {}'.format(line), end='')
stream.close()
