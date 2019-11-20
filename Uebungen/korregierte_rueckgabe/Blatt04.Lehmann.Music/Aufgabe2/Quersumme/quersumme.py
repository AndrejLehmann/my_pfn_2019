#!/usr/bin/python3
# Lehmann.Music

# bitte eure Bearbeitungszeit angeben, und vor Abgabe alle nicht notwendige
# File oder Lösung von anderen löschen.
# bitte vor Abgabe überprüfen dass alle Zeile kürzer als 80 Zeichen sind.
# Punkte: 3/3
# Korrektur: LZ

import sys
import re

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} <integer>\n".format(sys.argv[0]))
    sys.exit(1)

if not re.search(r'^ *[-+]?[0-9]+ *$',sys.argv[1]):
    sys.stderr.write('{}: argument "{}" is not an integer\n'.format(sys.argv[0],sys.argv[1]))
    sys.exit(1)


number = sys.argv[1].lstrip(' ').lstrip('-').lstrip('+').rstrip(' ')

quersumme = 0
for n in number:
    #try:
        quersumme += int(n)
    #except ValueError as err:
    #    sys.stderr.write('{}: argument "{}" is not an integer\n'.format(sys.argv[0],sys.argv[1]))
    #    exit(1)

print('{}\t{}'.format(sys.argv[1].strip(' '),quersumme))
