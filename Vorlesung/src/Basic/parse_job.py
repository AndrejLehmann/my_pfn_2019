#!/usr/bin/env python3
import re

employees = ['Anne User, System Administrator, 2005',
             'Joe Smith,Programmer, 2010']

for name_with_job in employees:
  m = re.search(r'(\w+)\s+(\w+),\s?([\w\s]+)', name_with_job)
  if m is not None:
    mlist = [m.group(1), m.group(2), m.group(3)]
    print('{}'.format('\t'.join(mlist)))

