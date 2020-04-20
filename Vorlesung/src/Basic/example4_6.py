#!/usr/bin/env python3
# Example 4-6 Reading protein sequence data from a file, take 2

# filename of file containing the protein sequence data
proteinfilename = 'NM_021964fragment.pep'

protein_stream = open(proteinfilename, 'r')

# Since the file has three lines, and since readline only returns
# one line, we'll read a line and print it, three times.

protein = protein_stream.readline()
print('First line of protein file:\n{}'.format(protein),end='')

protein = protein_stream.readline()
print('Second line of protein file:\n{}'.format(protein),end='')

protein = protein_stream.readline()
print('Third line of protein file:\n{}'.format(protein), end='')

# Now that we've got our data, we can close the file.
protein_stream.close()

exit(0)
