#!/bin/sh
# Harkov.Lehmann.Music
# Bearbeitungszeit: 1.5 Stunden

# Punkte: 5/5
# Korrektur: CR

# Den Ordner 'Tsv' einfach in Aufgabe 1 umbenennen und keinen weiteren Ordner

tail -n +2 islands.tsv > nohead.tsv
# man h"atte hier auch grep mit hypothetical protein und nohead nutzen k"onnen
less islands.tsv | grep "hypothetical protein" > hypo.tsv
less islands.tsv | grep -v "hypothetical protein" | tail -n +2 > nothypo.tsv
# hier h"atte man auch die nohead datei nutzen k"onnen 
cut -f 7 islands.tsv | tail -n +2 > locus.tsv
cut -f 1,2 islands.tsv | sort -u -g | tail -n +2 > ranges.tsv
