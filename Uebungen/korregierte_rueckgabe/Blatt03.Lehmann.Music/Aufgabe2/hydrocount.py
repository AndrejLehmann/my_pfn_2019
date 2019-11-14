#!/usr/bin/env python3

# Bitte eure Namen und Bearbeitungszeit angeben
# Bitte die originale Ordner nicht löschen
# Punkte: 1.5/2
# Korrektur: LZ

import sys

if len(sys.argv) == 2:

    hydrophob = hydrophil = 0
    hydrophobe_saeuren = ['A','F','I','L','M','P','V','W']
    # hier muss noch eine Liste für hydrophile Aminosäure definiert werden,
    # denn es gibt noch Buchstaben, die weder hydrophobe nor hydrophile AS sind.
    # Im diesem Fall funktioniert euer Programm nicht korrekt. -0.5
    for amino in sys.argv[1]:
        for c in amino:
            if c in hydrophobe_saeuren:
                hydrophob += 1
            else:
                hydrophil += 1
    print("hydrophobic={}, hydrophilic={}".format(hydrophob,hydrophil))
else:
    sys.stderr.write("Usage: {} <aminoacid sequence>\n".format(sys.argv[0]))
