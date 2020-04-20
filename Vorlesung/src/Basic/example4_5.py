#!/usr/bin/env python3
# Example 4-5 Reading protein sequence data from a file

# filename of the file containing the protein sequence data
proteinfilename = 'NM_021964fragment.pep'

# first create a new stream for reading, named protein_stream
protein_stream = open(proteinfilename, 'r')

# read protein sequence data from stream by calling readline method
protein = protein_stream.readline()

# now that we've got our data, we can close the stream
protein_stream.close()

# display protein sequence
print('Here is the protein:\n{}'.format(protein),end='')
