#!/usr/bin/env python3

attribute_list = ['atomicNumber','symbol',
                  'name', 'meltingPoint']
ls = ['1','H','Hydrogen','14']
for attr, value in zip(attribute_list,ls):
  print('{} {}'.format(attr,value))
