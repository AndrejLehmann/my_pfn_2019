#!/usr/bin/env python3

import re

stream = open('DNAfile', 'r')
dna = stream.read()
stream.close()

countA = len(re.findall(r'[aA]', dna)) # len for number of matches
countC = len(re.findall(r'[cC]', dna))
countG = len(re.findall(r'[gG]', dna))
countT = len(re.findall(r'[tT]', dna))
errs = len(re.findall(r'[^acgtACGT]',dna)) # all which is not base

print('A\t{}\nC\t{}\nG\t{}\nT\t{}\nerrs\t{}'
      .format(countA,countC,countG,countT,
              errs))
