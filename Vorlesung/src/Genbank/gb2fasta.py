#!/usr/bin/env python3

import sys, re
from print_sequence import print_sequence
from myopen import myopen

def gb2fasta(filename):
  seq_lines = None  # initialize list of sequence lines
  stream = myopen(filename,'r')
  for line in stream:
    if re.search(r'^\/\/\n', line): # end-of-record line //\n
      break       # break out of the nearest enclosing loop
    elif seq_lines is not None: # we are in a sequence
      seq_lines.append(line)   # add current line to array
    elif re.search(r'^ORIGIN', line): # line before sequence part
      seq_lines = list()    # now start with the sequences
  stream.close()
  return re.sub(r'[\s0-9]','', ''.join(seq_lines))

for filename in sys.argv[1:]:     # process command line args
  sequence = gb2fasta(filename)
  print('>')                    # empty fasta header
  print_sequence(sequence, 50)  # print formatted, width 50
