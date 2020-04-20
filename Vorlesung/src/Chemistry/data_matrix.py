#!/usr/bin/env python3

import re, sys

def data_matrix_new(lines,key_col = 1,sep = '\t'):
  matrix = dict()
  attribute_list = None
  for line in lines:
    ls = line.rstrip('\n').split(sep)
    if attribute_list is None: # in first line
      attribute_list = ls
    else:  # not in first line: values
      if len(ls) != len(attribute_list):
        sys.stderr.write('line has {} columns, but {} expected\n'
                          .format(len(ls),len(attribute_list)))
        exit(1)
      line_dict = dict()
      for attr, value in zip(attribute_list,ls):
        line_dict[attr] = value
      k = ls[key_col]
      if k in matrix:
        sys.stderr.write('key {} in line {} is not unique\n'
                          .format(k,2+len(matrix)))
        exit(1)
      matrix[k] = line_dict
  return attribute_list, matrix

def data_matrix_show(matrix,sep,attributes,keys):
  for key in keys:
    for a in attributes:
      if matrix[key][a] != '':
        print('{}{}{}{}{}'.format(key,sep,a,sep,matrix[key][a]))

def data_matrix_show_orig(matrix,sep,attributes,keys):
  print(sep.join(attributes))
  for key in keys:
    line_elems = list()
    for a in attributes:
      line_elems.append(matrix[key][a])
    print(sep.join(line_elems))
