#!/usr/bin/env python3

import sys, re

stream = open('TagesWerteHamburg/produkt_klima_tag_19360101_20171231_01975.txt')
for line in stream:
  if line[0] == ' ':
    values = line.strip().split(';')
    temp = float(values[13])
    date = re.search(r'(\d{4})(\d{2})(\d{2})',values[1])
    assert date
    year = int(date.group(1))
    month = int(date.group(2))
    day = int(date.group(3))
    if year >= 2008:
      print('{}-{:02d}-{:02d}\t{:.1f}'.format(year,month,day,temp))
stream.close()
