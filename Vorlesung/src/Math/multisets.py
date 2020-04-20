#!/usr/bin/env python3

import sys, argparse

def binom_evaluate(n,k):
  if k == 0 or n == k:
    return 1
  if n == 0:
    return 0
  result = 1
  for j in range(1,k+1):
    result = (result * (n - k + j))//j
  return result

def multisets_number(q,r):
  return binom_evaluate(r + q - 1, q)

def multisets_count1(multiset_size,
                     num_elems):
  def count_rec1(m,k):
    if m == 0:
      return 1
    count = 0
    if k > 0:
      for take in range(0,m+1):
        count += count_rec1(m - take,
                            k - 1)
    return count
  return count_rec1(multiset_size,
                    num_elems)

def multisets_count2(multiset_size,
                     num_elems):
  count_list = [0]
  def count_rec2(m,k):
    if m == 0:
      count_list[0] += 1
    elif k > 0:
      for take in range(0,m+1):
        count_rec2(m - take,k - 1)
  count_rec2(multiset_size,num_elems)
  return count_list[0]

def multisets_count3(multiset_size,
                     num_elems):
  stack = [(multiset_size,num_elems)]
  count = 0
  while stack:
    m, k = stack.pop()
    if m == 0:
      count += 1
    elif k > 0:
      for take in range(0,m+1):
        stack.append((m - take,k - 1))
  return count

def multisets_count(multiset_size,num_elems):
  mset_nums = list()
  mset_nums.append(multisets_number(multiset_size,num_elems))
  mset_nums.append(multisets_count1(multiset_size,num_elems))
  mset_nums.append(multisets_count2(multiset_size,num_elems))
  mset_nums.append(multisets_count3(multiset_size,num_elems))
  for idx in range(0,len(mset_nums)-1):
    assert mset_nums[idx] == mset_nums[idx+1]
  return mset_nums[0]

def multisets_enum_loops(multiset_size,
                         num_elems):
  assert multiset_size <= 4
  if multiset_size == 2:
    for i in range(0,num_elems):
      for j in range(i,num_elems):
        yield [i, j]
  elif multiset_size == 3:
    for i in range(0,num_elems):
      for j in range(i,num_elems):
        for k in range(j,num_elems):
          yield [i, j, k]
  elif multiset_size == 4:
    for i in range(0,num_elems):
      for j in range(i,num_elems):
        for k in range(j,num_elems):
          for l in range(k,num_elems):
            yield [i, j, k, l]

def multisets_enum_2loops(num_elems):
  for i in range(0,num_elems):
    for j in range(i,num_elems):
      yield [i, j]

def multisets_enum_rec(multiset_size,num_elems):
  multiset_list = list()
  multiset = [None] * multiset_size
  def multiset_rec(m,k):
    if m == 0:
      multiset_list.append(multiset.copy())
    elif k > 0:
      for take in range(0,m+1):
        for d in range(multiset_size - m,\
                       multiset_size - m + take):
          multiset[d] = num_elems - k
        multiset_rec(m-take,k-1)
  multiset_rec(multiset_size,num_elems)
  return multiset_list

def multisets_enum_stack(multiset_size,num_elems):
  stack = [(multiset_size,num_elems)]
  multiset = [None] * multiset_size
  while stack:
    m, k = stack.pop()
    if m == 0:
      yield multiset
    elif k > 0:
      for take in range(0,m+1):
        for d in range(multiset_size - m,\
                       multiset_size - m + take):
          multiset[d] = num_elems - k
        stack.append((m-take,k-1))

def multisets_enum(multiset_size,num_elems):
  if multiset_size <= 4:
    for ms in multisets_enum_loops(multiset_size,num_elems):
      yield ms
  else:
    for ms in multisets_enum_stack(multiset_size,num_elems):
      yield ms

def multiset_map2alphabet(multiset,alphabet):
  assert len(multiset) <= len(alphabet)
  return list(map(lambda i : alphabet[i],multiset))

def parse_command_line():
  p = argparse.ArgumentParser(
         formatter_class=argparse.RawDescriptionHelpFormatter,
         description='call generators for multisets of size q over alphabets of size r; output stattistics of sizes of depending on q and r')
  p.add_argument('-r','--num_elems',metavar='<int>',
                 help='specify size of base set',type=int,default=20)
  p.add_argument('-q','--multiset_size',metavar='<int>',
                 help='specify size of multiset',type=int,default=None)
  p.add_argument('-s','--str',action='store_true',
                 help='show strings, not indexes',default=False)
  args = p.parse_args()
  return args

args = parse_command_line()

if args.multiset_size is None:
  for multiset_size in range(2,7+1):
    mset_num = multisets_count(multiset_size,args.num_elems)
    print('{}&{}&\\numprint{{{}}}&\\numprint{{{}}}\\\\'
          .format(args.num_elems,multiset_size,mset_num,\
                                   args.num_elems ** multiset_size))
else:
  multiset_list1 = multisets_enum_rec(args.multiset_size,args.num_elems)
  assert len(multiset_list1) == multisets_number(args.multiset_size,
                                                  args.num_elems)
  multiset_list2 = list()
  for mset in multisets_enum(args.multiset_size,args.num_elems):
    multiset_list2.append(mset.copy())
  if args.num_elems == 4:
    alphabet = ['a','c','g','t']
  else:
    alphabet = list(map(chr,range(ord('a'),ord('a') + (args.num_elems+1))))
  assert len(multiset_list1) == len(multiset_list2)
  if sorted(multiset_list1) != sorted(multiset_list2):
    for a, b in zip(sorted(multiset_list1),sorted(multiset_list2)):
      print('{}\t{}'.format(a,b))
    exit(1)
  for ms in multiset_list1:
    if args.str:
      clist = multiset_map2alphabet(ms,alphabet)
      print(''.join(clist))
    else:
      print(ms)
