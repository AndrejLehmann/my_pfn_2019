#!/usr/bin/env python3

import sys, os, re
from get_file_data import get_file_data

# Extract annotation and sequence sections using regexps

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <genbankfile>\n'.format(sys.argv[0]))
  exit(1)

filename = sys.argv[1]
record = get_file_data(filename,'//\n')[0] # get first record
annotation = None
dna = None
m = re.search('^(LOCUS.*ORIGIN\s*\n)(.*)',record, flags=re.M|re.S)
if m:
  annotation = m.group(1)
  dna = m.group(2)
else:
  sys.stderr.write('{}: Cannot separate annot./seq. in {}\n'
                    .format(sys.argv[0],filename))
  exit(1)
print('annotation:\n{}DNA:\n{}'.format(annotation,dna),end='')
