#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 0.25h


# Alle Daten sollen im originalen Ordner liegen.
# Punkte: 2/2
# Korrektur: LZ

import sys
# t_c und t_f sind nicht notwendig hier, und als Liste verbrauchen sie
# zusätzlichen Speicherplatz. Am besten alles kompakt in for-Schleife schreiben.
t_c = [t for t in range(1,101)]
t_f = [(t*9.0)/5.0+32.0 for t in t_c]

print("# {}\t{}".format("celsius","fahrenheit"))

for i in range(len(t_c)):
    print("{:.2f}\t{:.2f}".format(t_c[i],t_f[i]))
