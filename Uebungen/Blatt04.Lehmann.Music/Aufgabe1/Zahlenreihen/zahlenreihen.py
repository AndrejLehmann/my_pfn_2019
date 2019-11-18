#!/usr/bin/python3
# Lehmann.Music

import sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} <k>\n".format(sys.argv[0]))
    exit(1)

try:
    k = int(sys.argv[1])
except ValueError as err:
    sys.stderr.write("{}: cannot convert '{}' to int\n".format(sys.argv[0],sys.argv[1]))
    exit(1)

if k < 0:
    sys.stderr.write("{}: parameter {} is not positive int\n".format(sys.argv[0],sys.argv[1]))
    exit(1)


### implementation of functions
'''
def summe(array):
    result = 0
    for n in array:
        print("{:.5e}".format(n))
        result += n
    return result 


def pow_(m, n):
    result = m
    for i in range(n-1):
        result *= m
    return result

# test pow_
"""
print('2**2 =',pow_(2,2),'=',2**2)
print('2**3 =',pow_(2,3),'=',2**3)
print('4**5 =',pow_(4,5),'=',4**5)
print('3**2 =',pow_(3,2),'=',3**2)
sys.exit()
"""


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# test factorial
"""
import math
print('0! =',factorial(0),'=',math.factorial(0))
print('1! =',factorial(1),'=',math.factorial(1))
print('2! =',factorial(2),'=',math.factorial(2))
print('3! =',factorial(3),'=',math.factorial(3))
print('4! =',factorial(4),'=',math.factorial(4))
sys.exit()
"""
'''
### END: implementation of functions


### implementation with loops
#Reihe_a = [2*n for n in range(1,k+1)]
print('Reihe a')
summe = 0
for n in range(1,k+1):
    n *= 2
    print(n)
    summe += n
print("Summe:",summe)
#print('Summe: {:.5e}',summe(Reihe_a))

print("Reihe b")
#Reihe_b = [(3+2*n)/pow_(2,n) for n in range(1,k+1)]
summe = 0
for n in range(1,k+1):
    zaehler = 3+2*n
    nenner = 2
    for i in range(n-1):
        nenner *= 2
    result = zaehler/nenner
    print('{:.5e}'.format(result))
    summe += result
print('Summe: {:.5e}'.format(summe))
    
print("Reihe c")
#Reihe_c = [pow_(-1,n-1)/pow_(2,n-1) for n in range(1,k+1)]
summe = 0
for n in range(1,k+1):
    zaehler = 1
    nenner = 1
    for i in range(1,n):
        zaehler *= (-1) 
        nenner *= 2
    result = zaehler/nenner
    print('{:.5e}'.format(result))
    summe += result
print('Summe: {:.5e}'.format(summe))
#print('Summe: {:.5e}'.format(summe(Reihe_c)))


print("Reihe d")
#Reihe_d = [1/factorial(n) for n in range(1,k+1)]
summe = 0
for n in range(1,k+1):
    zaehler = 1
    nenner = 1
    for i in range(1,n+1):
        nenner *= i
    result = zaehler/nenner
    print('{:.5e}'.format(result))
    summe += result
print('Summe: {:.5e}'.format(summe))
#print('Summe: {:.5e}.format(summe(Reihe_d))')
