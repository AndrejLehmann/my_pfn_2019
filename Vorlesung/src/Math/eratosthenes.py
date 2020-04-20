#!/usr/bin/env python3
import math, sys

def usage_exit(exit_code):
  sys.stderr.write('Usage: {} <integer >= 3>\n'
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
#BEGIN{exclude}
sqrt_n = math.sqrt(n)
smallest_unmarked = 2
while smallest_unmarked < sqrt_n:
  for i in range(2*smallest_unmarked,n+1,smallest_unmarked):
    marked[i] = True
  for i in range(smallest_unmarked+1,n+1):
    if not marked[i]:
      smallest_unmarked = i
      break
primes = list()
for i in range(2,n+1):
  if not marked[i]:
    primes.append(i)

# here is a version base on numpy, which runs faster by a factor of about 4

import numpy as np
def np_primes_list_get(n):
  is_prime = np.ones((n,),dtype=bool)
  is_prime[:2] = False
  n_max = int(np.sqrt(len(is_prime)))
  for j in range(2,n_max):
    is_prime[2*j::j] = False
  return np.nonzero(is_prime)[0] # nonzero return tuple (array[],)
#END{exclude}

num_primes = len(primes)
print('there are {} prime numbers <= {}'.format(num_primes,n))
show_primes = 10
print('the largest {} prime numbers <= {} are:'
      .format(min(num_primes,show_primes),n))
for i in range(max(0,num_primes-show_primes),num_primes):
  print('{}'.format(primes[i]))
