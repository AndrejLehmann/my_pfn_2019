#!/usr/bin/env python3
import sys, string

def reverse(seq):
  return ''.join(reversed(seq))

def reverse_complement(seq):
  revcom = reverse(seq)
  transtab = str.maketrans('ACGTacgt','TGCAtgca')
  return revcom.translate(transtab)

if __file__ == sys.argv[0]:
  s = 'agctatcagcagcat'
  t = reverse_complement(s)
  if s != reverse_complement(t):
    sts.stderr.write('s = {} != {} = RC({})\n'
                      .format(s,reverse_complement(t),t))
