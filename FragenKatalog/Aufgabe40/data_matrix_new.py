#!/usr/bin/env python3

import sys

def data_matrix_new(lines):
    dic_outer = {}
    for line in lines[1:]:
        split = line.rstrip('\n').split('\t')
        if len(split) == 3:
            atomicNumber, symbol, name = split
            meltingPoint = ''
        elif len(split) == 4:
            atomicNumber, symbol, name, meltingPoint = split
        else:
            sys.stderr.write('Unexpected format. Number of columns is not 3 or 4')
        dic_inner = {'atomicNumber': atomicNumber,
                     'symbol': symbol,
                     'meltingPoint': meltingPoint,
                     'name': name }
        dic_outer[symbol] = dic_inner
    return dic_outer


with open('test.txt', 'r') as f:
    lines = f.readlines()

print(data_matrix_new(lines))


