#!/usr/bin/env python3

import os
import sys
import re

# Example 5-6   Determining frequency of nucleotides, take 2

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

# Read the DNA sequence data from the file, and store it
# as a concatenated string in the variable dna
dna = dnafile.readlines()
dna = ''.join(dna)

# Close the file
dnafile.close()

# Remove whitespace
dna = re.sub(r'\s','', dna)

# Initialize the counts.
count_of_A = 0
count_of_C = 0
count_of_G = 0
count_of_T = 0
errors     = 0

# In a loop, look at each base in turn, determine which of the
# four types of nucleotides it is, and increment the
# appropriate count.
for position in range(len(dna)):
  base = dna[position]
  if base == 'A':
    count_of_A += 1
  elif base  == 'C':
    count_of_C += 1
  elif base == 'G':
    count_of_G += 1
  elif base == 'T':
    count_of_T += 1
  else:
    print('Error - I don\'t recognize this base: {}'.format(base))
    errors += 1

# print the results
print('A = {}'.format(count_of_A))
print('C = {}'.format(count_of_C))
print('G = {}'.format(count_of_G))
print('T = {}'.format(count_of_T))
print('errors = {}'.format(errors))
