#!/usr/bin/env python3

import sys

try:
  stream = open(__file__, 'r') # open this source file
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

counters = [0] * 256  # list with 256 entries, init with 0
for line in stream:    # iterate over the lines in stream
  for c in line:       # iterate over the characters in line
    c_code = ord(c)         # convert character to code
    counters[c_code] += 1   # use code as index and increment
stream.close()
for c_code, count in enumerate(counters):  # iterate over counters
  if count > 0:                            # output positive counts
    print('{}\t{}'.format(chr(c_code),count)) # convert code->char

def distribution_list_new(s):
  counters = [0] * 256
  for line in s:
    for c in line:
      counters[ord(c)] += 1
  return counters

def distribution_list_show(dist):
  for c_code, count in enumerate(dist):
    if count > 0:
      print('{}\t{}'.format(chr(c_code),count))

def distribution_list_freq_show(dist):
  sum_count = 0
  for count in dist:
    sum_count += count
  for c_code, count in enumerate(dist):
    if count > 0:
      print('{}\t{}'.format(chr(c_code),100.0 * count/sum_count))

try:
  stream = open(__file__, 'r') # open this source file
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))

dist = distribution_list_new(stream)
distribution_list_freq_show(dist)
