#!/usr/bin/env python3
# Example 4-3   Transcribing DNA into RNA

import re      # use methods from class re

dna = 'ACGGGAGGACGGGAAAATTACTACGGCATTAGC'

# print the DNA onto the screen
print('Here is the DNA:')
print(dna)

# transcribe the DNA to RNA by substituting all T's with U's.
rna = re.sub('T', 'U', dna)   # use method sub from class re

print('Here is the result of transcribing the DNA to RNA:')
print(rna)

exit(0)
