#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 2:
  s = sys.argv[1]
else:
  sys.stderr.write('Usage: {} <string>\n'.format(sys.argv[0]))
  exit(1)

m = re.search(r'name is (\w+), (\w+)', s)
if m:
  print('{} {}'.format(m.group(2), m.group(1)))
