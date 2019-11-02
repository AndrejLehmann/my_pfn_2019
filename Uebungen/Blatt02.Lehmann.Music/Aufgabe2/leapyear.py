#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 0.5h

import sys

for year in sys.argv[1:]:
    year = int(year)
    if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
        print(year, "ist ein Schaltjahr")
    else:
        print(year, "ist kein Schaltjahr")


