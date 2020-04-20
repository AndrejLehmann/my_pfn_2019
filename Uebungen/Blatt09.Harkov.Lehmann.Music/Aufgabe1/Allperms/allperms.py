#!/usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 3h

from math import factorial
import sys,argparse

def all_permutations(elems):
    all_perms = []
    all_perms_rec(all_perms,elems)
    return all_perms

#                                   [0,1,2]
# 1.pop:             [1,2]           [0,2]           [0,1]
# 2.pop:            [2] [1]         [2] [0]         [1] [0]
# append 2.pop:   [2,1] [1,2]     [2,0] [0,2]     [1,0] [0,1]
# append 1.pop: [2,1,0] [1,2,0] [2,0,1] [0,2,1] [1,0,2] [0,1,2]
def all_perms_rec(all_perms, elems):   # all_perms = [], elems = [0,1]

    if len(elems) == 0:
        all_perms.append(elems)
        return
    if  len(elems) == 1:
        all_perms.append(elems)        # new_subset_perms = [[1]]
        return

    for idx, elem in enumerate(elems): # elems = [0,1]
        new_subset = elems.copy()      #
        new_subset.pop(idx)            # new_subset = [1], [0] # [1], [2]
        new_subset_perms = []
        all_perms_rec(new_subset_perms, new_subset) # all_perms_rec(new_subset_perms=[], [1])
        for p in new_subset_perms:                  # new_subset_perms = [[1]]
            p.append(elem)                          # [1].append(0) = [1,0]
            all_perms.append(p)                     # [].append([1,0])



def all_permutations_verify(all_perms,elems):
  elems.sort()

  assert len(all_perms) == factorial(len(elems))

  all_perms_uniq = [ele for ind, ele in enumerate(all_perms) if ele not in all_perms[:ind]]
  assert all_perms_uniq == all_perms

  all_perms_copy = all_perms.copy()
  #print(id(all_perms_copy), id(all_perms)) # are different
  #print(id(all_perms_copy[0]), id(all_perms[0])) # are the same
  for perm in all_perms_copy:
      assert sorted(perm) == elems

  return


if __name__ == '__main__':
  def parse_arguments():
    p = argparse.ArgumentParser(description='generate and verify permutations')
    p.add_argument('max_setsize',type=int,
                    help='specify maximum size of set to permute')
    return p.parse_args()

  args = parse_arguments()
  for num_elems in range(0,args.max_setsize + 1):
    elems = list(range(num_elems))
    all_perms = all_permutations(elems)
    all_permutations_verify(all_perms,elems)
