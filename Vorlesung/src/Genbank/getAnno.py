#!/usr/bin/env python3
import sys, re
from splitGB import split_genbank
from parseAnno import parse_annotation

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <genbankfile>\n'.format(sys.argv[0]))
  exit(1)

filename = sys.argv[1]
for annotation, dna in split_genbank(filename):
  fields = parse_annotation(annotation)
  for key, value in fields.items():
    stars = '*' * 8
    print('{} {} {}'.format(stars,key,stars))
    print(value, end='')
  break # only output first
