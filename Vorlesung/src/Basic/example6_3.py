#!/usr/bin/env python3
# Example 6-3   Count number of G's in some DNA from command line

import sys

if len(sys.argv) != 2:
  sys.stderr.write(
        'Usage: {} DNA\n'
        .format(sys.argv[0]))
  exit(1)

s = sys.argv[1].lower()
print('{} contains {} g\'s'
        .format(s,
                s.count('g')))
