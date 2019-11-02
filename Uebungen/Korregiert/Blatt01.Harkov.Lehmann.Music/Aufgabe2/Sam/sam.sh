#!/bin/sh
# Harkov.Lehmann.Music
# Bearbeitungszeit: 3 Stunden

# Punkte: 5/5
# Korrektur: CR

# Den Ordner 'Sam' einfach in Aufgabe 2 umbenennen und keinen weiteren Ordner

# Bitte die Format-Regeln beachten. Mehr als 80 Zeichen pro Zeile f"uhren zu
# Punktabzug ab "Ubung 3

cut -f 3 alignments.sam  | sort -u -d | grep NODE* > references.txt
# statt less kann man auch nach dem grep einfach die Datei benennen, also so:
# grep -v ^@ alignments.sam| grep NODE > aligned_only.sam
less alignments.sam | grep -v ^@ | grep NODE > aligned_only.sam

#                                               v-- uniq only matches on repeated lines, so sort first
cut -f 3 alignments.sam  |  grep -E 'NODE|\*' | sort | uniq -c | tr -s " " | tr " "  "\t" | cut -f 2,3 > references_count.tsv
#                                                              |            Umwandeln zur             |
#                                                              |____ tabulator-getrennter Ausgabe ____|

less alignments.sam | grep -v ^@ | grep NODE | cut -f 1 | sort -n | uniq -c | tr -s " " | tr " "  "\t" | cut -f 2,3 > reads_n_alignments.tsv

#zur Sicherheit bei sort -n angeben, falls der PC andere Settings hat 
cut -f 1 reads_n_alignments.tsv | sort | uniq -c | tr -s " " | tr " "  "\t" | cut -f 2,3 > reads_n_alignments_distri.tsv
