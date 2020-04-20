#!/usr/bin/env python3
# Example 4-4   Calculating the reverse complement of a DNA-strand
#from revcom import reverse
from reverse_complement import reverse
import re, string

dna = 'ACGGGAGGACGGGAAAATTACTACGGCATTAGC'
print('Here is the DNA:')
print(dna)

revcom = reverse(dna)

revcom = re.sub('A','T', revcom)
revcom = re.sub('T','A', revcom)
revcom = re.sub('G','C', revcom)
revcom = re.sub('C','G', revcom)

print('Here is the incorrect result:\n{}'.format(revcom))

revcom = reverse(dna)
transtab = str.maketrans('ACGTacgt','TGCAtgca')
revcom = revcom.translate(transtab)
print('Here is the reverse complement DNA:\n{}'.format(revcom))
