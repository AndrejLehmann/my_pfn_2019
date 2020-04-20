#!/usr/bin/env python3

def fac(n):
  if n == 0:
    return 1
  return n * fac(n-1)

def main():
  return fac(3)

print('{}!={}'.format(3,main()))

def ls(l):
  if len(l) == 0:
    return 0
  return l[0] + ls(l[1:])

l = [1,2,3,4]
print('ls({})={}'.format(l,ls(l)))

def myr(s):
  if len(s) == 0:
    return s
  return myr(s[1:]) + s[0]

s = 'abcd'
print('myr({})={}'.format(s,myr(s)))

def toStr(n,base):
  characters = '0123456789ABCDEF'
  if n < base:
    return characters[n]
  return toStr(n//base,base) + \
         characters[n%base]

for n in [17,1234,837373]:
  for b in [2,8,16]:
    print('{}\t{}'.format(n,toStr(n,b)))

# http://www.pythontutor.com/visualize.html#code=def%20palindrome%28s%29%3A%0A%20%20%20%20if%20len%28s%29%20%3C%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20return%20s%5B0%5D%20%3D%3D%20s%5B-1%5D%20and%20palindrome%28s%5B1%3A-1%5D%29%0A%20%20%20%20%0Afor%20w%20in%20%5B'kayak','radar'%5D%3A%0A%20%20%20%20assert%20palindrome%28w%29&cumulative=false&curInstr=12&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def palindrome(s):
  if len(s) == 0 or len(s) == 1:
    return True
  return s[0] == s[-1] and palindrome(s[1:-1])

for w in ['kayak','radar','wassamassaw','madam','level','noon']:
  assert palindrome(w)

for w in ['abca','ab','abc','abab','abba']:
  assert not palindrome(w)
