#!/usr/bin/env python3
# Example 6-1  program with a function to add values

def addsomething(n,s,l):
  print('parameters: n={},s={},l={}'
        .format(n,s,l))
  n += 1
  s += 'C'
  l += [3]
  print(' after inc: n={},s={},l={}'
         .format(n,s,l))

n = 5
s = 'A'
l = [1]
addsomething(n,s,l)
print('after call: n={},s={},l={}'
       .format(n,s,l))

def addsomething_ids(n,s,l):
  print('parameters: n={},s={},l={}'
        .format(n,s,l))
  print('ids={},{},{}'.format(id(n),id(s),id(l)))
  n += 1
  s += 'C'
  l += [3]
  print(' after inc: n={},s={},l={}'
         .format(n,s,l))
  print('ids={},{},{}'.format(id(n),id(s),id(l)))

n = 5
s = 'A'
l = [1]
addsomething_ids(n,s,l)
print('after call: n={},s={},l={}'
       .format(n,s,l))
print('ids={},{},{}'.format(id(n),id(s),id(l)))

def overwrite_list(l):
  print('param:       l={},id={}'.format(l,id(l)))
  l = [3]
  print('after write: l={},id={}'.format(l,id(l)))

l = [1]
overwrite_list(l)
print('after call:  l={},id={}'.format(l,id(l)))
