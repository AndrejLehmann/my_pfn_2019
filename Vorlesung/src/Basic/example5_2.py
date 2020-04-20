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

# Read the protein sequence data from the file in a while loop,
# printing each line as it is read.
while True:
  protein = proteinfile.readline()
  if protein == '':
    break
  print('#  Here is the next line of the file:\n{}'.format(protein), end='')

# When we have reached the end, close file.
proteinfile.close()

exit(0)
