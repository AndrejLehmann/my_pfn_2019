#!/usr/bin/env python3

import sys

def hextoint(cc):
  if cc >= 48 and cc <= 57: # a digit
    return cc - 48
  elif cc >= 65 and cc <= 70:
    return 10 + cc - 65
  else:
    sys.stderr.write('{}: illegal character in hex-number'.format(sys.argv[0]))
    exit(1)

def hex2toint(s):
  if len(s) != 2:
    sys.stderr.write('{}: {}.length = {} not expected'
                      .format(sys.argv[0], s, len(s)))
    exit(1)
  return hextoint(s[0]) * 16 + hextoint(s[1])
