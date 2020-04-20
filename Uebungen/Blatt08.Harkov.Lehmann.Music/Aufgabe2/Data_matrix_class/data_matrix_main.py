#!/usr/bin/env python3

#lst{DataMatrixCommandlineParser}
import sys, argparse

def parse_command_line():
  p = argparse.ArgumentParser(description=('extract information '
                                           'of data matrix'))
  p.add_argument('-k','--keys',nargs='+',default=None,
                  help='specify keys for which values are output')
  p.add_argument('-a','--attributes',nargs='+',default=None,
                  help='specify attributes output')
  p.add_argument('-o','--orig',action='store_true',default=False,
                  help='output key/value pairs in original format')
  p.add_argument('-s','--sep',type=str,default='\t',
                  help='specify column separator, default is Tab')
  p.add_argument('inputfile',type=str,
                  help='specify inputfile (mandatory argument)')
  return p.parse_args()
#lstend#

def parse_command_line_documentation():
  p = argparse.ArgumentParser(description='extract information ..')
#lst{DataMatrixCommandlineParserInputfile}
  p.add_argument('inputfile',type=str,
                  help='specify inputfile (mandatory argument)')
#lstend#
#lst{DataMatrixCommandlineParserKeys}
  p.add_argument('-k','--keys',nargs='+',default=None,
                  help='specify keys for which values are output')
#lstend#
#lst{DataMatrixCommandlineParserOutput}
  p.add_argument('-o','--orig',action='store_true',default=False,
                  help='output key/value pairs in original format')
#lstend#
#lst{DataMatrixCommandlineParserSep}
  p.add_argument('-s','--sep',type=str,default='\t',
                  help='specify column separator, default is Tab')
#lstend#
  return p.parse_args()

#lst{DataMatrixMainFirstPart}
args = parse_command_line()

try:
  stream = open(args.inputfile)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)
#lstend#

#lst{DataMatrixMainSecondPart}
from data_matrix import *

attribute_list, matrix = data_matrix_new(stream)
stream.close()
if args.attributes:  # option -a was used
  attributes = args.attributes
else:
  attributes = attribute_list # use all attributes
if args.keys:  # option -k was used
  keys = args.keys
else:
  keys = matrix.keys()   # use all keys
if args.orig:
  data_matrix_show_orig(matrix,args.sep,attributes,keys)
else:
  data_matrix_show(matrix,args.sep,attributes,keys)
#lstend#
