#!/usr/bin/env python3

import re, sys, argparse

def lexicalunits(inputfile):
  if inputfile == '-':
    stream = sys.stdin
  else:
    try:
      stream = open(inputfile,'r')
    except IOerror as err:
      sys.stderr.write('{}: {}'.format(sys.argv[0],err))
      exit(1)
  for line in stream:
    line = re.sub(r'\s*','',line)
    for lex_unit in re.findall(r'\)?[^\(\),;]+[,;]?|[\(\),;]',line):
      yield lex_unit
  if inputfile != '-':
    stream.close()

def parse_arguments():
  p = argparse.ArgumentParser()
  p.add_argument('inputfile',type=str,
                  help='specify input files, - means stdin')
  return p.parse_args()

args = parse_arguments()

level = 0
for lex_unit in lexicalunits(args.inputfile):
  if lex_unit[0] == '(':
    print('{}{}'.format(' ' * (2 * level),lex_unit))
    level += 1
  else:
    if lex_unit[0] == ')':
      assert level > 0
      level -= 1
    print('{}{}'.format(' ' * (2 * level),lex_unit))
