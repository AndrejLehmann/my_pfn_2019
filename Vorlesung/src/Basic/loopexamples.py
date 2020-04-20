#!/usr/bin/env python3

languages = ['C', 'C++', 'Python']
for lang in languages:
  print(lang)

for word in ['dog','cat','mouse']:
  print(word,len(word))

minval_so_far = None  # represent the absence of a value
for i in [3,5,2,1,9,5,-1,4,-2,0]:
  if minval_so_far is None or i < minval_so_far:
    minval_so_far = i
print('minimum is {}'.format(minval_so_far))

count = total = 0
for f in [3.8,5.1,2.3,1.9,9.1,5.2,11.0,4.1]:
  total += f
  count += 1
print('average is {:.2f}'.format(total/count))

poem = 'Almost nothing was more annoying than having our wasted\
        time wasted on something not worth wasting it on'
char_list = list()
for cc in poem:
  if not (cc in char_list):
    char_list.append(cc)
print('"{}"'.format(''.join(char_list)))

for i in range(5):
  print('{} '.format(i),end='')
print('')

for counter in range (4,0,-1):
  print('counter has value {} and is '.format(counter),end='')
  if counter % 2 == 0:
    print('even')
  else:
    print('odd')

m = 50
n = 100
sum = 0
for i in range(m,n+1):
  sum = sum + i
print(sum)

n = 17
from math import sqrt
for i in range(1,n+1):
  for j in range(i,n+1):
    square_sum = i**2 + j**2
    k = int(sqrt(square_sum))
    if square_sum == k**2:
      print(i, j, k)

def pythagorean(n):
  triples = list()
  for i in range(1,n+1):
    for j in range(i,n):
      square_sum = i**2 + j**2
      k = int(sqrt(square_sum))
      if square_sum == k**2:
        triples.append([i, j, k])
  return triples

for pt in pythagorean(20):
  print('\t'.join(map(str,pt)))

i = 0
j = 10
while i < j:
  print(i,j)
  i = i + 1
  j = j - 1
print('at end: i={},j={}'
       .format(i,j))

import sys
while True:
  c = sys.stdin.read(1)
  if c == '\n':
    break
  print('found {}'.format(c))
