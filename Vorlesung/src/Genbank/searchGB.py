#!/usr/bin/env python3
from splitGB import split_genbank
import sys, re

def search_genbank(multiline, regexp):
  poslst = list()
  # match regexp against multiline sequence, be case insensitive
  for mo in re.finditer(regexp, multiline, flags=re.I|re.M):
    poslst.append(mo.start())  # append start position of match
  return poslst

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  sys.stderr.write('Usage: {} <genbankfile>\n'.format(sys.argv[0]))
  exit(1)

seqnum = 0
for annotation, dna in split_genbank(filename):
  if search_genbank(dna, 'AAA[CG].'):
    print('Sequence found in record {}'.format(seqnum))
  if search_genbank(annotation, 'homo sapiens'):
    print('Annotation found in record {}'.format(seqnum))
  seqnum += 1
