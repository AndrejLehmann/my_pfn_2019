#!/usr/bin/env python3
# Example 4-7   Reading protein sequence data from a file, take 3

# filename of file containing the protein sequence data
proteinfilename = 'NM_021964fragment.pep'

# create a stream, without exception handling to keep it simple
protein_stream = open(proteinfilename, 'r')

# read protein sequence data from file, and store it in list
proteins = protein_stream.readlines()

# iterate over the elements in the list and generate their index
for idx, protein in enumerate(proteins):
  print('{}: {}'.format(idx, protein), end='')
protein_stream.close()

exit(0)
