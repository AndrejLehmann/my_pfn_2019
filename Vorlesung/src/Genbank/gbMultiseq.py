#!/usr/bin/env python3

import sys, re
from print_sequence import print_sequence
from multiseq import Multiseq

for filename in sys.argv[1:]:     # process command line args
  multiseq = Multiseq(filename)
  for seq_entry in multiseq:
    print('>{}'.format(seq_entry.header))
    print_sequence(seq_entry.sequence,50)  # print formatted, width 50
