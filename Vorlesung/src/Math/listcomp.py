#!/usr/bin/env python3

from math import sqrt

'''
http://python-history.blogspot.com/2010/06/from-list-comprehensions-to-generator.html
[f(x) for x in S if P(x)]

This produces a list containing the values of the sequence S selected by the predicate P and mapped by the function f. The if-clause is optional, and multiple for-clauses may be present, each with their own optional if-clause, to represent nested loops (the latter feature is rarely used though, since it typically maps a multi-dimensional entity to a one-dimensional list).

List comprehensions provide an alternative to using the built-in map() and filter() functions. map(f, S) is equivalent to [f(x) for x in S] while filter(P, S) is equivalent to [x for x in S if P(x)]. One would think that list comprehensions have little to recommend themselves over the seemingly more compact map() and filter() notations. However, the picture changes if one looks at a more realistic example. Suppose we want to add 1 to the elements of a list, producing a new list. The list comprehension solution is [x+1 for x in S]. The solution using map() is map(lambda x: x+1, S). The part “lambda x: x+1” is Python’s notation for an anonymous function defined in-line.
'''

'''
examples from https://www.datacamp.com/community/tutorials/python-list-comprehension
Some mathematical sets:
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}
translated into list comprehensions of python
'''

listS = [x*x for x in range(9+1)]
listV = [2**i for i in range(11+1)]
listM = [m for m in listS \
               if m % 2 == 0]

def cut_column(stream,column,sep='\t'):
  return [line.split(sep)[column] for line in stream]

stream = open('../Chemistry/atom-data.tsv')
print(cut_column(stream,2))
stream.close()

def cut(stream,extract_columns,sep='\t'):
  return [[line.split(sep)[i] for i in extract_columns]\
          for line in stream]

stream = open('../Chemistry/atom-data.tsv')
print(cut(stream,[1,3]))
stream.close()

def cut_dict(stream,key_col,value_col,sep='\t'):
  return {split_line[key_col] : split_line[value_col]\
          for line in stream\
          for split_line in [line.split(sep)]}

stream = open('../Chemistry/atom-data.tsv')
print(cut_dict(stream,1,2))
stream.close()

for name, l in zip(['S','V','M'],[listS,listV,listM]):
  print('{}={}'.format(name,l))

def my_map_y(f,g):
  for a in g:
    yield f(a)

def my_map(f,g):
  return (f(a) for a in g)

def gen_increment_map(g):
  return map(lambda x: x+1, g)

def gen_increment(g):
  return (x+1 for x in g)

intlist = [5,3,7,8,10]
print('gen_increment({})={}'
       .format(intlist,list(gen_increment(intlist))))

list_increment = list(gen_increment_map(intlist))
assert list_increment == list(gen_increment(intlist))
assert list_increment == list(my_map(lambda x: x+1,intlist))
assert list_increment == list(my_map_y(lambda x: x+1,intlist))

def my_filter(p,g):
  return (a for a in g if p(a))

def is_odd(i):
  return i % 2 == 1

assert list(my_filter(is_odd,list(range(0,25)))) == \
       list(filter(is_odd,list(range(0,25))))

def flatten(list_of_lists):
  return [x for l in list_of_lists for x in l]

list_of_lists = [[1,2,3],[4,5,6],[7,8]]
print('flatten({})={}'
       .format(list_of_lists,flatten(list_of_lists)))

def same_list_length(ll):
  return not ll or all([len(ll[0]) == len(l) for l in ll])

def transpose(matrix):
  assert same_list_length(matrix)
  return [[row[j] for row in matrix]\
          for j in range(len(matrix[0]))]

def matrix_new(rows,columns,init):
  return [[init(i,j) for j in range(columns)] for i in range(rows)]

matrix1 = matrix_new(2,4,lambda i,j: i*4 + j)

matrix2 = [[0,1,2,3],
           [4,5,6,7]]

assert matrix1 == matrix2

matrix_t = transpose(matrix1)
print('transpose({})={}'.format(matrix1,matrix_t))

'''
https://www.python-course.eu/python3_list_comprehension.php
'''

def pythagorean_triples(n):
  return [(i,j,k) for i in range(1,n)\
                  for j in range(i,n)\
                  for square_sum in [i**2 + j**2]\
                  for k in [int(sqrt(square_sum))]\
                  if square_sum == k**2]

print('{}'.format(pythagorean_triples(20)))

def codons():
  bases = 'acgt'
  return [''.join([x,y,z]) for x in bases \
                           for y in bases \
                           for z in bases]

print('codons={}'.format(codons()))

def multisets3(alpha_size):
  return [[i,j,k] for i in range(alpha_size) \
                  for j in range(i,alpha_size)\
                  for k in range(j,alpha_size)]

print('multisets3(2)={}'.format(multisets3(2)))


def gen_squares_func(n):
  for x in range(n):
    yield x ** 2

gen_squares = (x**2 for x in range(10))

def sieve_lc(n):
  no_primes = [j for i in range(2, int(sqrt(n))+1)\
                 for j in range(i*2, n, i)]
  return [p for p in range(2, n+1) if p not in no_primes]

def sieve_sc(n):
  no_primes = {j for i in range(2, int(sqrt(n))+1)\
                 for j in range(i*2, n, i)}
  return [p for p in range(2, n+1) if p not in no_primes]

assert sieve_lc(1000) == sieve_sc(1000)
print('primes={}'.format(sieve_sc(70)))
