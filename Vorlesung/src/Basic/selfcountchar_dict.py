#!/usr/bin/env python3

import sys

line = 'abracadabra'
count_dict = dict()    # empty dictionary
for c in line:         # iterate over charactres in string
  if not (c in count_dict): # check if c is not already in dict.
    count_dict[c] = 0  # for first occurence init count to 0
  count_dict[c] += 1   # increment entry for character c in dict
for c, count in count_dict.items():# iterate over key/value pairs
  print('{}\t{}'.format(c,count))
