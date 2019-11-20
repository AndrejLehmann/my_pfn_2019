#!/usr/bin/env python3
# Lehmann.Music

# bitte eure Bearbeitungszeit angeben, und vor Abgabe alle nicht notwendige
# File oder Lösung von anderen löschen.
# bitte vor Abgabe überprüfen dass alle Zeile kürzer als 80 Zeichen sind.
# Punkte: 2/2
# Korrektur: LZ

import sys
import re

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} <inputfile with dates in format dd.mm.yyyy>".format(sys.argv[0]))
    exit(1)

try:
    f = open(sys.argv[1],'r')
except:
    sys.stderr.write("{}: [Errno 2] No such file or directory: '{}'".format(sys.argv[0],sys.argv[1]))
    exit(1)
dates = f.readlines()
f.close()


for date in dates:
    day, month, year = date.split('.')
# am besten mit regulären Ausdruck das Format überprüfen, sonst bricht
# das Programm direkt ab wenn das Format nicht stimmt.
    leapyear = None
    if (int(year)%4 == 0) and (int(year)%100 != 0) or (int(year)%400 == 0):
        leapyear = True
    else:
        leapyear = False

    if not leapyear:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dayNumber = 0
    for n in range(int(month)-1):
        dayNumber += days[n]
    dayNumber += int(day)
    print('{}\t{}'.format(date.rstrip('\n'),dayNumber))
