#!/usr/bin/env python3
import re

for date in ['2014-12-13','2016-01-02']:
  # extract numbers from a date string YYYY-MM-DD
  m = re.search(r'(\d{4})-(\d{2})-(\d{2})', date)
  if m:
    year = m.group(1)
    month = m.group(2)
    day = m.group(3)
    print('{}.{}.{}'.format(day, month, year))

def date_parse(date):
  m = re.search(r'(\d{4})-(\d{2})-(\d{2})', date)
  if not m:
    return None
  d = dict()
  d['y'] = int(m.group(1))
  d['m'] = int(m.group(2))
  d['d'] = int(m.group(3))
  return d

for date in ['2014-12-13','2016-01-02']:
  d = date_parse(date)
  if d is not None:
    print(d)
