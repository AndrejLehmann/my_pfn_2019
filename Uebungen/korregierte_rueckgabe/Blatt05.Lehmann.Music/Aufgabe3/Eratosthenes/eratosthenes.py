#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 0.5h

# Punkte: 3/3
# Korrektur: LZ

import math, sys

def usage_exit(exit_code):
  sys.stderr.write("Usage: {} <integer >= 3>\n"
                    .format(sys.argv[0]))
  exit(exit_code)

if len(sys.argv) != 2:
  usage_exit(1)

try:
   n = int(sys.argv[1])
except:
   usage_exit(2)

if n <= 2:
   usage_exit(3)

# Implement the Algorithm 'Sieve of Eratosthenes' after the line
# initializing the list marked below, as described in the exercise sheet.
# After the marking process has finished, create a list
# primes of all i, 2<=i<=n, such that marked[i] is not True.
# This is the list of prime numbers, which is output in the code below

marked = [None,None] + ([False] * (n-1))
#      = [None, None, False, False, ..., False]
primes = []


# Sieve of Eratosthenes
#for i in range(len(marked)):
i = 2
while i < math.sqrt(n):
    if marked[i] is False:
        j = 2
        while j*i < len(marked):
            marked[j*i] = True
            j += 1
    i += 1


# save the prime numbers in a list
for i in range(len(marked)):
    if marked[i] is False:
        primes.append(i)

num_primes = len(primes)
print('there are {} prime numbers <= {}'.format(num_primes,n))
show_primes = 10
print('the largest {} prime numbers <= {} are:'
      .format(min(num_primes,show_primes),n))
for i in range(max(0,num_primes-show_primes),num_primes):
  print('{}'.format(primes[i]))
