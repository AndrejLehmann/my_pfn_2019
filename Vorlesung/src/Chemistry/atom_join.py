#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
  sys.stderr.write('Usage: {} <atomfile1> <atomfile2>\n'
                    .format(sys.argv[0]))
  exit(1)

stream_list = list()
for arg in sys.argv[1:]:  # iterate over all elements except 1st
  try:
    stream = open(arg)
  except IOError as err:
    sys.stderr.write('{}: {}\n'
                      .format(sys.argv[0],err))
    exit(1)
  stream_list.append(stream)

dict_list = list()
for stream in stream_list:
  atom2name = dict()  # key is abbrev, value is name
  for line in stream:
    abbrev_name = line.rstrip().split('\t')
    if len(abbrev_name) != 2:
      sys.stderr.write('{}: expect two columns in line {}'
                        .format(sys.argv[0],line.rstrip()))
      exit(1)
    atom2name[abbrev_name[0]] = abbrev_name[1]
  stream.close()
  dict_list.append(atom2name)

atom2name0 = dict_list[0]
atom2name1 = dict_list[1]
for abbrev, name in atom2name0.items():
  if abbrev in atom2name1:
    print('{}\t{}\t{}'.format(abbrev,name,atom2name1[abbrev]))
