#!/usr/bin/env python3
# Example 5-2   Reading protein sequence data from a file, take 4

import sys

# The filename of the file containing the protein sequence data
proteinfilename = 'NM_021964fragment.pep'

try:
  proteinfile = open(proteinfilename,'r')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)


# Read the protein sequence data from the file via an iterator,
# printing each line as it is read.
for line in proteinfile:
  print('# Here is the next line of the file:')
  print(line, end='')

proteinfile.close()

exit(0)
