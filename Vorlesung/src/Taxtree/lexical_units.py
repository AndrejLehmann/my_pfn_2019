#!/usr/bin/env python3

import re, sys, argparse
from enum import Enum
class LexicalKind(Enum):
  OPEN = 0
  CLOSE = 1
  LEAF = 2
  def __str__(self):
    return self.name

def lexical_units_enum(inputfile):
  if inputfile == '-':
    stream = sys.stdin
  else:
    try:
      stream = open(inputfile,'r')
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
  for line in stream:
    line = re.sub(r'\s*','',line) # delete all white spaces
    for match in re.findall(r'\)?[^\(\),;]+[,;]?|\(',line):
      if match == '(':
        yield (LexicalKind.OPEN,None)
      else:
        mo = re.search(r'\)(?P<branch_name>[^,;]+)[,;]?',match)
        if mo: # match )branch_name optionally followed by , or ;
          yield (LexicalKind.CLOSE,mo.group('branch_name'))
        else: # no ( and ) => leaf
          yield (LexicalKind.LEAF,re.sub(r',$','',match))
  if inputfile != '-':
    stream.close()

def lexical_units_indent(lu_stream):
  level = 0
  indent = lambda level : ' ' * (2 * level)
  for lu in lu_stream:
    if lu[0] == LexicalKind.OPEN:
      print('{}{}'.format(indent(level),lu[0]))
      level += 1
    else:
      if lu[0] == LexicalKind.CLOSE:
        assert level > 0
        level -= 1
      print('{}{} {}'.format(indent(level),
                             lu[0],lu[1]))

if __name__ == '__main__':
  p = argparse.ArgumentParser()
  p.add_argument('inputfile',type=str,
                 help='specify input files, - means stdin')
  args = p.parse_args()
  lexical_units_indent(lexical_units_enum(args.inputfile))
