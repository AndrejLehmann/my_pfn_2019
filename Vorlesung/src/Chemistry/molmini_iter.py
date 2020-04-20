#!/usr/bin/env python3

import sys, re

def molminiIterator(stream):
  molecule_name = None
  atom_list = list()
  for line in stream:
    line = line.rstrip()
    m = re.search(r'^MOLECULE\s(.*)$',line)
    if m:
      if atom_list: # output previous molecule
        yield molecule_name, atom_list # will be processed
        atom_list = list()     # reset
      molecule_name = m.group(1)
    elif re.search(r'^\s+\S',line):  # atom line
      atom_list.append(line)
  if atom_list:                # process last molecule
    yield molecule_name, atom_list

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write('Usage: {} <filename>\n'.format(sys.argv[0]))
    exit(1)
  try:
    stream = open(sys.argv[1])
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  count_molecules = count_atoms = 0
  for molecule_name, atom_list in molminiIterator(stream):
    count_molecules += 1
    count_atoms += len(atom_list)
  stream.close()
  print('found {} molecules with {:.2f} atoms on average'
         .format(count_molecules,count_atoms/count_molecules))
