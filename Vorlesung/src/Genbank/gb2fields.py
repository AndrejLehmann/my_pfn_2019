#!/usr/bin/env python3
import sys, re
from myopen import myopen

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <genbankfile>\n'.format(sys.argv[0]))
  exit(1)

# Get some of the information identifying the records
# LOCUS, DEFINITION, ACCESSION, ORGANISM
indef = False   # used for parsing DEFINITION (can be multiline)
values = dict()  # empty dictionary
stream = myopen(sys.argv[1],'r')
for line in stream:
  if re.search(r'^LOCUS', line):
    line = re.sub(r'^LOCUS\s*','', line) # del. LOCUS at beginning
    values['LOCUS'] = line.rstrip()
  elif re.search(r'^DEFINITION', line):
    line = re.sub(r'^DEFINITION\s*','', line) # delete DEFINITION
    values['DEFINITION'] = line.rstrip()
    indef = True          # now inside DEFINITION
  elif re.search(r'^ACCESSION', line):
    line = re.sub(r'^ACCESSION\s*','', line) # delete ACCESSION
    values['ACCESSION'] = line.rstrip()
    indef = False        # now again outside of DEFINITION
  elif re.search(r'^  ORGANISM', line):
    line = re.sub(r'^\s*ORGANISM\s*', '', line) # delete ORGANISM
    values['ORGANISM'] = line.rstrip()
  elif indef:            # still inside DEFINITION
    line = re.sub(r'^\s+',' ', line) # initial multispaces => space
    values['DEFINITION'] += line.rstrip()
stream.close()

for key in ['LOCUS','DEFINITION','ACCESSION','ORGANISM']:
  print('*** {} ***\n{}'.format(key,values[key]))
