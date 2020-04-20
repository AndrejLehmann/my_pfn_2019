#!/usr/bin/env python3

filename = 'NM_021964fragment.pep'
print('Try to open "{}"'.format(filename))
stream = open(filename,'r')
# read lines delivered by stream and print them
for line in stream:
  print('next line is {}'.format(line), end='')
stream.close()
