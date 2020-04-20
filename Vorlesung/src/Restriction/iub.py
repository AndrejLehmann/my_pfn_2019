# IUB_to_regexp
#
# given a sequence with IUB ambiguity codes,
# outputs a translation with IUB codes changed to regular expressions
#
# These are the IUB ambiguity codes
# (Eur. J. Biochem. 150: 1-5, 1985):
# R = G or A
# Y = C or T
# M = A or C
# K = G or T
# S = G or C
# W = A or T
# B = not A (C or G or T)
# D = not C (A or G or T)
# H = not G (A or C or T)
# V = not T (A or C or G)
# N = A or C or G or T
import sys
def iub_to_regexp(iub):
  iub2character_class = {
        'A' : 'A',
        'C' : 'C',
        'G' : 'G',
        'T' : 'T',
        'R' : '[GA]',
        'Y' : '[CT]',
        'M' : '[AC]',
        'K' : '[GT]',
        'S' : '[GC]',
        'W' : '[AT]',
        'B' : '[CGT]',
        'D' : '[AGT]',
        'H' : '[ACT]',
        'V' : '[ACG]',
        'N' : '[ACGT]'
    }
  # list of regexps mapped to IUB characters
  mapped = list()
  # Replace each IUB item with its character class
  for iubchar in iub:
    if iubchar in iub2character_class:
      mapped.append(iub2character_class[iubchar])
    else:
      sys.stderr.write('{}: unknown IUB-character {}\n'
                        .format(sys.argv[0],iubchar))
      exit(1)
  return ''.join(mapped)
