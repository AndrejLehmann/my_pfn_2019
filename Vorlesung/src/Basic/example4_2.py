#!/usr/bin/env python3
# Example 4-2   Concatenating DNA

# store two DNA sequences into two variables called dna1 and dna2
dna1 = 'ACGGGAGGACGGGAAAATTACTACGGCATTAGC'
dna2 = 'ATAGTGCCGTGAGAGTGATGTAGTA'

# print the DNA onto the screen
print('Here are the original two DNA sequences:')
print(dna1)
print(dna2)

# concatenate DNA sequences into a 3rd var with format
dna3 = '{}{}'.format(dna1, dna2)
print('concatenation of the first two sequences (version 1):')
print(dna3)

# alternative way using the concatenation operator +:
dna3 = dna1 + dna2
print('Concatenation of the first two sequences (version 2):')
print(dna3)

# print the same thing without using the variable dna3
print('Concatenation of the first two sequences (version 3):')
print(dna1 + dna2)

exit(0)
