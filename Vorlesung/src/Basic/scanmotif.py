#!/usr/bin/env python3
import sys  # for error message
import re   # for regular expressions

# ask the user for the filename of the file containing
# the sequence data, and collect it from the keyboard
filename = input('type filename of the sequence: ')

# remove trailing newline from the read filename
filename = filename.rstrip()

# open the file, or exit: sys.argv[0] is name of program
try:
  stream = open(filename,'r')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0], err))
  exit (1)

# read the sequence data from file, store it in sequence_lines
sequence_lines = stream.readlines()

stream.close()

# concatenate lines into a single string, as it's easier to
# search for a motif in a string than in a list of lines
sequence = ''.join(sequence_lines)

# Remove whitespace from sequence
sequence = re.sub(r'\s','',sequence)

# In a loop, ask user for motif, search for motif, and report
# if it was found. break out of loop if no motif is entered.
while True:
  motif = input('enter motif to search (return => quit): ')
  motif = motif.rstrip()
  if motif == '':
    break
  print('searching motif "{}"'.format(motif))
  m = re.search(r'{}'.format(motif), sequence)
  if m:
    print('I found it!')
  else:
    print('I couldn\'t find it!')
