#!/usr/bin/env python3
bases = ['A', 'C', 'G', 'T']
base1 = bases.pop()
bases.insert(0, base1)
print('element from end put on beginning: {}'.format(bases))
