#!/usr/bin/env python3

import re
import sys

dnafile = open('small.dna','r')
dna = dnafile.readlines()
dna = ''.join(dna)

countA = len(re.findall('a|A', dna))
countC = len(re.findall('c|C', dna))
countG = len(re.findall('g|G', dna))
countT = len(re.findall('t|T', dna))
errors = len(re.findall('[^acgt|ACGT]', dna))

outputfilename = 'countbase'

# write results to file, s_out is the output stream
try:
  s_out = open(outputfilename,'w')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

s_out.write('A={} C={} G={} T={}\n'
             .format(countA, countC, countG, countT))
s_out.close()
