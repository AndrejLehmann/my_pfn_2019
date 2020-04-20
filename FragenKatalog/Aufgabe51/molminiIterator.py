#!/usr/bin/env python3
import re

def molminiIterator(stream):
    line = stream.readline()
    while line:
        m = re.search(r'^MOLECULE (\w+)$', line)
        if m:
            MolName = m.group(1)
            atoms = []
            line = stream.readline()

        while re.search(r'^MOLECULE (\w+)$', line) is None and line:
            atoms.append(line.rstrip('\n').lstrip())
            line = stream.readline()

        yield MolName, atoms

stream = open('test.txt', 'r')
for molName, atom_list in molminiIterator(stream):
    print(molName, atom_list)
