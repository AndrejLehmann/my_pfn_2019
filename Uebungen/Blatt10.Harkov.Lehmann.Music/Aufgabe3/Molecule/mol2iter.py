#!/usr/bin/env python3

import sys, os, re
from molecule import Molecule

from enum import Enum
class ParseState(Enum):
  IN_MOLECULE = 0
  IN_ATOM = 1
  IN_BOND = 2

def mol2Iterator(mol2file):
  try:
    stream = open(mol2file)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  molecule_name = None
  parse_state = None
  atom_list = list()
  bond_list = list()
  for linenum, line in enumerate(stream,1):
    if re.search(r'^@<TRIPOS>MOLECULE',line):
      if parse_state == ParseState.IN_BOND:
        parse_state = None
        if not (molecule_name is None):
          yield molecule_name, atom_list, bond_list
          molecule_name = None
          atom_list = list()
          bond_list = list()
      parse_state = ParseState.IN_MOLECULE
    elif re.match(r'^@<TRIPOS>ATOM',line):
      parse_state = ParseState.IN_ATOM
    elif re.match(r'^@<TRIPOS>BOND',line):
      parse_state = ParseState.IN_BOND
    elif re.match(r'^@',line):
      if parse_state == ParseState.IN_BOND:
        parse_state = None
        if not (molecule_name is None):
          yield molecule_name, atom_list, bond_list
          molecule_name = None
          atom_list = list()
          bond_list = list()
    elif parse_state == ParseState.IN_MOLECULE:
      if molecule_name is None:
        molecule_name = line.rstrip()
    elif parse_state == ParseState.IN_ATOM:
      ls = line.rstrip().split()
      if len(ls) < 6:
        sys.stderr.write('{}: file {}, line {} contains less than 6 columns\n'
                         .format(sys.argv[0],mol2file,linenum))
        exit(1)
      atom_list.append(ls)
    elif parse_state == ParseState.IN_BOND:
      ls = line.rstrip().split()
      if len(ls) < 4:
        sys.stderr.write('{}: file {}, line {} contains less than 4 columns\n'
                         .format(sys.argv[0],mol2file,linenum))
        exit(1)
      bond_list.append(ls)
  if parse_state == ParseState.IN_BOND and not (molecule_name is None):
    yield molecule_name, atom_list, bond_list
  stream.close()

if __name__ == '__main__':
  molecule_list = list()
  molecule_names = set()
  if len(sys.argv) != 2:
    sys.stderr.write('Usage: {} <mol2file>\n'.format(sys.argv[0]))
    exit(1)
  mol2file = sys.argv[1]
  for molecule_name, atom_list, bond_list in mol2Iterator(mol2file):
    if molecule_name in molecule_names:
      sys.stderr.write('{}: molecule name {} already occurred'
                        .format(sys.argv[0],molecule_name))
      exit(1)
    molecule_list.append(Molecule(molecule_name,atom_list,bond_list))
    molecule_names.add(molecule_name)

  for molecule in molecule_list:
    print('{}'.format(molecule))
