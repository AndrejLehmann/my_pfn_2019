#!/usr/bin/env python3
# Example 5-3   Searching for motifs

import sys
import re

# Ask the user for the filename of the file containing
# the protein sequence data, and collect it from the keyboard
print('Please type the filename of the protein sequence data: ', end='')
proteinfilename = input()

# Remove the newline from the protein filename
proteinfilename = proteinfilename.rstrip()

try:
  proteinfile = open(proteinfilename,'r')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

# Read the protein sequence data from the file, and store it
# into the list variable lines
lines = proteinfile.readlines()

# Close the file - we've read all the data into protein now.
proteinfile.close()

# Put the protein sequence data into a single string, as it's easier
# to search for a motif in a string than in a list of
# lines (what if the motif occurs over a line break?)
proteinseq = ''.join(lines)

# Remove whitespace and '>' symbols
proteinseq = re.sub('\s|\>', '', proteinseq)

print('"{}"'.format(proteinseq))

# In a loop, ask the user for a motif, search for the motif,
# and report if it was found.
# Exit if no motif is entered.
while True:
  print('Enter a motif to search for: ', end='')
  motif = input()

  # exit on an empty user input
  if motif == '':
    exit(0)

  # Remove the newline at the end of the motif
  motif = motif.rstrip()

  # Look for the motif
  m = re.search(r'{}'.format(motif), proteinseq)
  if m is not None:
    print('I found "{}" as {}'.format(motif, m.group(0)))
  else:
    print('I couldn\'t find {}'.format(motif))

# exit the program
exit(0)
