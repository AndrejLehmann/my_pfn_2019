#!/usr/bin/env python3
import sys, re
from splitGB import split_genbank
from parseAnno import parse_annotation
from parseFeatures import parse_features

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <genbankfile>\n'.format(sys.argv[0]))
  exit(1)

filename = sys.argv[1]
for annotation, dna in split_genbank(filename):
  fields = parse_annotation(annotation)
  for featureentry in parse_features(fields['FEATURES']):
    mo = re.search('^ {5}(\S+)', featureentry)
    if mo:
      stars = '*' * 8
      feature_name = mo.group(1)
      print('{} {} {}'.format(stars,feature_name,stars))
      print(featureentry, end = '')
  break # only output first
