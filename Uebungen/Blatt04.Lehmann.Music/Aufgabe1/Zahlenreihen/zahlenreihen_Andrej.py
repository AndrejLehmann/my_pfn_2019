#!/usr/bin/python3

import sys

try:
    k = int(sys.argv[1])
except ValueError as err:
    sys.stderr.write("Usage: {} <k>\n".format(sys.argv[0],sys.argv[1]))
    exit(1)

if k < 0:
    sys.stderr.write("{}: parameter {} is not positive int\n".format(sys.argv[0],sys.argv[1]))
    exit(1)

def sum_(array):
    sum_ = 0
    for n in array:
        print(n)
        sum_ += n
    print("Summe:",sum_)

Reihe_a = [2*n for n in range(1,k+1)]
print("Reihe a")
sum_(Reihe_a)
# v-- loop alternative
"""
sum_Reihe_a = 0
for n in Reihe_a:
    print(n)
    sum_Reihe_a += n
print("Summe:",sum_Reihe_a)
"""

Reihe_b = [3+2*n for n in range(1,k+1)]
print("Reihe b")
sum_(Reihe_b)

Reihe_c = []
