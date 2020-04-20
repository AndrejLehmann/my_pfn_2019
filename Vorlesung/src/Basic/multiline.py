#!/usr/bin/env python3

import re

def test_match(flags):
  m = re.search(r'^.*$','AAC\nGTT',flags=flags)
  if m:
    print('match with flags={} in range [{}-{}]'
           .format(flags,m.start(),m.end()))
  else:
    print('no match with flags={}'.format(flags))

test_match(0)
test_match(re.S)
test_match(re.M)
test_match(re.S|re.M)
