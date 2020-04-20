#!/usr/bin/env python3

import re

re_list = ['[ab][cd]','[01][23]']
for re in re_list:
  for s in ['ac','bd','02','12']:
    m = re.search(r'{}'.format(re),s)
    if not (m is None):
      print('{} matches {}'.format(re,s))
