#!/usr/bin/env python3
import sys, os

from multiseq import Multiseq
from parseREBASE import parseREBASE
from match_positions import match_positions_fwd

if len(sys.argv) < 3:
  sys.stderr.write('Usage: {} <dnafile> <rest. enzym. 1> [rest. enzym. 2..]'
                    .format(sys.argv[0]))
  exit(1)
inputfile = sys.argv[1]
queries = sys.argv[2:]

multiseq = Multiseq(inputfile)
dna = multiseq[0].sequence
rebase_dict = parseREBASE('REBASE.txt') # Get REBASE into dict
for query in queries:  # iterate over queries = sys.args[2:]
  if query in rebase_dict:
    site, regexp = rebase_dict[query] # elem at index 0 and 1
    poslist = match_positions_fwd(regexp, dna)
    if not poslist: # list is empty
      print('{}={} does not occur in DNA'.format(query,site))
    else:
      print('{}={} occurs at pos {}'
             .format(query,site,', '.join(map(str,poslist))))
  else:
    sys.stderr.write('{}: {} is not a valid name\n'
                      .format(sys.argv[0],query))
    exit(1)
