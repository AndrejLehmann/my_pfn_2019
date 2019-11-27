#!/usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 

import re, sys

def usage():
  sys.stderr.write("Usage: {} <linewidth> <inputfile>\n"
                   .format(sys.argv[0]))
  exit(1)

if len(sys.argv) != 3:
  usage()

try:
  linewidth = int(sys.argv[1])
except ValueError as err:
  sys.stderr.write("{}: cannot convert {} into integer\n".format(filename, err))
  usage()

filename = sys.argv[2]
try:
  stream = open(filename, "r")
except IOError as err:
  sys.stderr.write("{}: {}\n".format(filename, err))
  exit(1)

# add your code here
stream.close()
