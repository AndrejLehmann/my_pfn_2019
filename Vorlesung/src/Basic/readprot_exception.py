#!/usr/bin/env python3
import sys

fname = 'NM_021964fragment.pep'
print('open "{}"'.format(fname))
try:
  stream = open(fname,'r')  # this statement may throw an exception
except IOError as err:  # exception stores error message in err
  # now comes the code reacting on the exception
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

# read lines delivered by stream and print them
for line in stream:
  print('next line is {}'.format(line), end='')
stream.close()
