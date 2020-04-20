#!/usr/bin/env python3

dna = 'acgactactcgaccatcatcagcca'
count_purine = count_pyrimidine = 0
for base in dna:
  if base == 'a' or base == 'g':
    count_purine += 1
  elif base == 'c' or base == 't':
    count_pyrimidine += 1
print('purine={},pyrimidine={}'.format(count_purine,count_pyrimidine))
