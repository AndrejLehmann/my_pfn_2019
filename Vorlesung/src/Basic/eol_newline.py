#!/usr/bin/env python3

f = open('filewitoutlastnewline.txt','r')
for line in f:
  print('line=>{}<'.format(line))
