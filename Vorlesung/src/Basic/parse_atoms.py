#!/usr/bin/env python3

import re

atoms = ['Hydrogen gas 1.00794',
         'Lithium  alkaline metal 6.941',
         'Beryllium   alkaline earth metal9.012182']
for atom in atoms:
  m = re.search(r'(\w+)\s+([\w\s]+)\s?(\d+\.\d+)', atom)
  if m:
    print('{:<9s} {:<20s} {:>.3f}'
           .format(m.group(1),m.group(2),float(m.group(3))))
