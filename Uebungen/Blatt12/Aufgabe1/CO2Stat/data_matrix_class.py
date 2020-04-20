#!/usr/bin/env python3

import re, sys

class DataMatrix:
#INCLUDE   def __init__(self,lines,key_col = 1,sep = '\t'):
#BEGIN{exclude}
  def __init__(self,lines,key_col = 1,sep = '\t', ordered = False):
    if ordered:
      self._keys = list()
    else:
      self._keys = None
#END{exclude}
    self._matrix = dict()
    self._attribute_list = None
    for line in lines:
      ls = line.rstrip('\n').split(sep)
      if self._attribute_list is None: # in first line
        self._attribute_list = ls
#BEGIN{exclude}
        if key_col < 0 or key_col >= len(ls):
          sys.stderr.write('{}: number of column for keys is out of range\n'
                            .format(sys.argv[0]))
          exit(1)
#END{exclude}
      else:  # not in first line: values
        if len(ls) != len(self._attribute_list):
          sys.stderr.write('line has {} columns, but {} expected\n'
                            .format(len(ls),len(self._attribute_list)))
          exit(1)
        line_dict = dict()
        for attr, value in zip(self._attribute_list,ls):
          line_dict[attr] = value
        k = ls[key_col]
        if k in self._matrix:
          sys.stderr.write('key {} in line {} is not unique\n'
                          .format(k,2+len(self._matrix)))
          exit(1)
        self._matrix[k] = line_dict
#BEGIN{exclude}
        if ordered:
          self._keys.append(k)
#END{exclude}
  def keys(self):
#BEGIN{exclude}
    if self._keys:
      return self._keys
#END{exclude}
    return self._matrix.keys()
  def attribute_list(self):
    return self._attribute_list
  def show(self,sep,attributes,keys):
    for key in keys:
      for a in attributes:
        if self._matrix[key][a] != '':
          print('{}{}{}{}{}'
                 .format(key,sep,a,sep,self._matrix[key][a]))
  def show_orig(self,sep,attributes,keys):
    print(sep.join(attributes))
    for key in keys:
      line_elems = list()
      if not key in self._matrix:
        sys.stderr.write('{}: illegal key "{}"\n'.format(sys.argv[0],key))
        exit(1)
      for a in attributes:
        if not a in self._matrix[key]:
          sys.stderr.write('{}: illegal attribute "{}"\n'.format(sys.argv[0],a))
          exit(1)
        line_elems.append(self._matrix[key][a])
      print(sep.join(line_elems))
#BEGIN{exclude}
  def sort_keys(self, attribute):
    keys_and_sorting_values = list()
    for key, row in self._matrix.items():
      keys_and_sorting_values.append((row[attribute], key))
    keys_and_sorting_values.sort()
    return map(lambda key_value: key_value[1],keys_and_sorting_values)
  
  def show_attribute_mean(self,attributes,keys):
    for attribute in attributes:
      values = list()
      numeric = True
      for key in keys:
        value = self._matrix[key][attribute]
        if value:
          try:
            numvalue = float(value)
          except:
            numeric = False
            break
          values.append(numvalue)
      if numeric and len(values) > 0:
        mean = sum(values)/len(values)
        print('Mean {}: {:.2f}'.format(attribute, mean))
  def matrix_select(self,attributes,keys):
    for key in keys:
      for a in attributes:
        if self._matrix[key][a] != '':
          yield key, a, self._matrix[key][a]
#lst{webscrapingattributeselect}
  def attribute_select(self,attribute):
    for key in self._keys:
      yield self._matrix[key][attribute]
#lstend#
  def __getitem__(self,key):
    assert key in self._matrix, \
           '{}: no matrix entry for key {}'.format(sys.argv,key)
    return self._matrix[key]
#END{exclude}
 
import sys, argparse

def parse_command_line():
  p = argparse.ArgumentParser(description='handle data matrices')
  p.add_argument('-k','--keys',nargs='+',default=None,metavar='<key>',
                  help='specify keys for which values are output')
  p.add_argument('-a','--attributes',nargs='+',default=None,
                 metavar='<attribute>',
                 help='specify attributes output')
  p.add_argument('-o','--orig',action='store_true',default=False,
                  help='output key/value pairs in original format')
  p.add_argument('-s','--sep',type=str,default='\t',
                  help='specify column separator, default is Tab')
#BEGIN{exclude}
  p.add_argument('--key_col',type=int,default=1,metavar='<number>',
                 help=('specify column number in which unique keys are '
                       'stored, index starts with 0'))
  p.add_argument('--sort_ascending',type=str,default=None,
                 metavar='<attribute>',
                 help=('sort in ascending order by attribute which is '
                       'specified as argument'))
  p.add_argument('-m', '--mean',action='store_true',default=False,
                 help='output average of numeric attributes')
#END{exclude}
  p.add_argument('inputfile',type=str,
                  help='specify inputfile (mandatory argument)')
  return p.parse_args()

def main():
  args = parse_command_line()
  try:
    stream = open(args.inputfile)
  except IOError as err:
    sys.stderr.write('{}: cannot open file {}\n'
                      .format(sys.argv[0],args.inputfile))
    exit(1)
#BEGIN{exclude}
  if args.keys or args.sort_ascending:
    ordered = False
  else:
    ordered = True
  data_matrix = DataMatrix(stream,args.key_col,args.sep, ordered)
#END{exclude}
#INCLUDE   data_matrix = DataMatrix(stream,1,args.sep)
  stream.close()
  if args.attributes:  # option -a specifies attributes
    attributes = args.attributes
  else:
    attributes = data_matrix.attribute_list() # use all attributes
  if args.keys:
    keys = args.keys # use -k specified keys
#BEGIN{exclude}
  elif args.sort_ascending:
    keys = data_matrix.sort_keys(args.sort_ascending)
#END{exclude}
  else:
    keys = data_matrix.keys() # use all keys
  if args.orig:
#BEGIN{exclude}
    if args.mean:
      sys.stderr.write(('{}: option -o/--orig is incompatible with option ' +
                        '-m/--mean\n').format(sys.argv[0]))
      exit(1)
#END{exclude}
    data_matrix.show_orig(args.sep,attributes,keys)
#BEGIN{exclude}
  elif args.mean:
    if args.sort_ascending:
      sys.stderr.write('{}: option --sort_ascending is incompatible with '
                       'option -m/--mean\n'.format(sys.argv[0]))
      exit(1)
    data_matrix.show_attribute_mean(attributes,keys)
#END{exclude}
  else:
    data_matrix.show(args.sep,attributes,keys)

if __name__ == '__main__':
  main()
