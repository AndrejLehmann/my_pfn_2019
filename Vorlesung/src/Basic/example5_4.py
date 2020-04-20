#!/usr/bin/env python3

import os
import sys
import re

# Example 5-4   Determining frequency of nucleotides

# Get the name of the file with the DNA sequence data
print('Please type the filename of the DNA sequence data: ', end='')
dnafilename = input()

# Remove the newline from the DNA filename
dnafilename = dnafilename.rstrip()

# open the file, or exit
if os.path.exists(dnafilename):
  try:
    dnafile = open(dnafilename,'r')
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
else:
  sys.stderr.write('File {} does not exist\n'.format(dnafilename))
  exit(1)

# Read the DNA sequence data from the file, and store it
# as a concatenated string in the variable dna
dna = dnafile.readlines()
dna = ''.join(dna)

# Close the file
dnafile.close()

# Remove whitespace
dna = re.sub(r'\s','', dna)

# Now explode the DNA into a list where each letter of the
# original string is now an element in the list.
# This will make it easy to look at each position.
#dna = dna.split(//)

# Initialize the counts.
count_of_A = 0
count_of_C = 0
count_of_G = 0
count_of_T = 0
errors     = 0

# In a loop, look at each base in turn, determine which of the
# four types of nucleotides it is, and increment the
# appropriate count.
for base in dna:
  if base == 'A' or base == 'a':
      count_of_A += 1
  elif base == 'C' or base == 'c':
      count_of_C += 1
  elif base == 'G' or base == 'g':
      count_of_G += 1
  elif base == 'T' or base == 't':
      count_of_T += 1
  else:
      errors += 1

# print the results
print('A = {}'.format(count_of_A))
print('C = {}'.format(count_of_C))
print('G = {}'.format(count_of_G))
print('T = {}'.format(count_of_T))
print('errors = {}'.format(errors))
gccount = count_of_C + count_of_G
totallength = len(dna)
print('GC-content: {:.1f}\n'.format(100.0 * gccount/totallength), end='')
