#!/usr/bin/env python3

import re
def match_positions_fwd(regexp, sequence):
  poslist = list()
  # match regexp against sequence, be case insensitive
  for m in re.finditer(regexp, sequence, flags=re.I):
    poslist.append(m.start())
  return poslist

if __name__ == '__main__':
  sequence = 'abracadabra, dreimal schwarzer Kater'
  regexp = r'a[clr]'
  print('{}'.format(match_positions_fwd(regexp, sequence)))
