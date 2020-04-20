#!/usr/bin/env python3

import os
import sys
import re

# Example 5-7   Determining frequency of nucleotides, take 3

# Get the name of the file with the DNA sequence data
print('Please type the filename of the DNA sequence data: ', end='')
dnafilename = input()
dnafilename = dnafilename.rstrip()

if os.path.exists(dnafilename):
  try:
    dnafile = open(dnafilename,'r')
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
else:
  sys.stderr.write('File {} does not exist!\n'.format(dnafilename))
  exit(1)

dna = dnafile.readlines()
dna = ''.join(dna)
dnafile.close()
dna = re.sub(r'\s','', dna)

a, c, g, t, e = 0, 0, 0, 0, 0

# Use a regular expression trick, and five loops,
#  to find the counts of the four bases plus errors
a = len(re.findall('a|A', dna))
c = len(re.findall('c|C', dna))
g = len(re.findall('g|G', dna))
t = len(re.findall('t|T', dna))
e = len(re.findall('[^acgt|ACGT]', dna))

print('A={} C={} G={} T={} errors={}\n'.format(a,c,g,t,e), end='')

# Also write the results to a file called countbase
outputfilename = 'countbase'

try:
  countbase = open(outputfilename,'w')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

#output = 'A={} C={} G={} T={} errors={}\n'.format(a, c, g, t, e))
countbase.write('A={} C={} G={} T={} errors={}\n'.format(a, c, g, t, e))
countbase.close()

exit(0)
