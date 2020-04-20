#!/usr/bin/env python3

def gensigneddoubles(maxabs):
    n = 1
    while abs(2*n) <= maxabs:
        n = -2*n
        yield n

for num in gensigneddoubles(2000):
    print('{} '.format(num), end='')
print()
