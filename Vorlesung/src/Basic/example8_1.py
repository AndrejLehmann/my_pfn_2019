#!/usr/bin/env python3
# Example 8-1   Translate DNA into protein

import codon2aa

# Initialize variables
dna = 'CGACGTCTTCGTACGGGACTAGCTCGTGTCGGTCGC'
protein = ''

# Translate each three-base codon into an amino acid, and append to a protein
n = 3
for codon in [dna[i:i+n] for i in range(0, len(dna), n)]:
  protein += codon2aa.codon2aa(codon)

print('I translated the DNA\n\n{}\ninto the protein\n{}'.format(dna, protein))
