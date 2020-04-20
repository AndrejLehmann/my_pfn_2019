#!/usr/bin/env python3
bases = ['A', 'C', 'G', 'T']
base2 = bases.pop(0)
bases.append(base2)
print('element from beginning put on end: {}'.format(bases))
