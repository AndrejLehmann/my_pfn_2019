#!/usr/bin/env python3

# convert a comma separated to a tab separated file, such that the
# commas in quoted columns are not replaced by a tab
# this program was used to convert the file data.csv from the repo
# https://github.com/andrejewski/periodic-table.git
# into the file atom-data.tsv

import sys, re

def comma2tab(line):
  incomment = False
  char_list = list()
  for cc in line:
    if cc == ',':
      if not incomment:
        char_list.append('\t')
      else:
        char_list.append(',')
    elif cc == '"':
      if incomment:
        incomment = False
      else:
        incomment = True
    else:
      char_list.append(cc)
  nline = ''.join(char_list)
  return re.sub(r' ?\t ?','\t',nline)

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <csv-file>\n'.format(sys.argv[0]))
  exit(1)

try:
  astream = open(sys.argv[1])
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

for line in astream:
  tsv_line = comma2tab(line.rstrip())
  print(tsv_line)
astream.close()
