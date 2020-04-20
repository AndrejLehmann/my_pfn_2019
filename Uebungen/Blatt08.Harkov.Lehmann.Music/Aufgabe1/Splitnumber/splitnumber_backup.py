#!/usr/bin/env python3
# Bearbeitungszeit: 4.0h
import math
import sys

testArray = [2,3,3,3,3]

def quality_function(intArray):
    mean = sum(intArray)/len(intArray)
    quality  = 0.
    for n in intArray:
        quality += (n - mean)**2
    quality = math.sqrt(quality)
    return quality

#print(quality_function(testArray))




def split_number_rec(terms_of_sum, best_split, remain, terms_idx, l):
    '''
    terms_of_sum : list of positiv int numbers
    best_split   : list with 2 values
                   [0] = additive split with min quality value (default: None)
                   [1] = quality value of [0] (default: None)
    remain       : number for which the additive split from terms_of_sum[terms_idx:]
                   suppose to be calculated
    l            : is a list containing sums from terms_of_sum

    The result is saved in best_split
    '''


    print(remain,terms_of_sum[terms_idx])
    if remain - terms_of_sum[terms_idx] == 0:
        l.append(terms_of_sum[terms_idx])
        print(l)
        if  best_split[1] is None or quality_function(l) < best_split[1]:
            best_split[0] = l
            best_split[1] = quality_function(l)

    elif remain - terms_of_sum[terms_idx] > terms_of_sum[terms_idx]:
        remain -= terms_of_sum[terms_idx]
        l.append(terms_of_sum[terms_idx])
        split_number_rec(terms_of_sum, best_split, remain, terms_idx, l)

    else:
        if terms_idx + 1 < len(terms_of_sum):
            terms_idx += 1
            split_number_rec(terms_of_sum, best_split, remain, terms_idx, l)


def split_number(number, terms_of_sum):
    best_split = [None, None]
    l = []
    #split_number_rec(terms_of_sum, best_split, remain, terms_idx, l)
    split_number_rec(terms_of_sum, best_split, number, 0, []) # [2,2,2,2,3]
    split_number_rec(terms_of_sum, best_split, 5, 1, [2,2,2]) # [2,2,2,5]
    split_number_rec(terms_of_sum, best_split, 7, 1, [2,2]) # []
    split_number_rec(terms_of_sum, best_split, 9, 1, [2]) # [2,3,3,3]

    return best_split


n  = 11
l  = []
S = [2, 3, 5]
split_number_rec(S, [None,None], n, 0, l) # [2,2,2,2,3]

n  = 32
l  = []
S = [7, 11, 13]
split_number_rec(S, [None, None], n, 0, l) # [7,7,7,11]]

n  = 38
l  = []
S = [7, 11, 13]
split_number_rec(S, [None, None], n, 0, l) # [7,7,11,13]
sys.exit()

n  = 45
l  = []
S = [8, 9]
split_numbers_test(S, [None, None], n, 0, l) # [9,9,9,9,9]]
n  = 47
l  = []
S = [11, 12, 13, 14]
split_numbers_test(S, [None, None], n, 0, l) # [11,12,12,12]]
n  = 47
l  = []
S = [13, 14]
split_numbers_test(S, [None, None], n, 0, l) # None






'''
S = [s1, s2, ..., si, ..., sk]
sort(S)
n = n1*s1 + n2*s2 + n3*s3 + ... + nk*sk


SCAN PARAMETER SPACE ALGORITHM:
    0 <= n1, n2, ..., ni, ..., nk <= N  # parameter space for ni
    N = max( ni | ni*min(S) <= n )
    go through all ni in parameter space to find n


INT DIVIDE ALGORITHM:
    nk = n//sk
    rk = n%sk
    n(k-1) = rk//s(k-1)
    r(k-1) = rk%s(k-1)
    ...
    n2 = r3//s2
    r2 = r3%s2
    n1 = r2//s1
    r1 = r2%s1 = 0

    save quality

    n(k-1) = rk//s(k-1)
    r(k-1) = rk%s(k-1)
    ...
    n1 = r2//s1
    r1 = r2%s1 = 0

    compare quality
    replace with parameters with better quality

    n(k-2) = rk//s(k-2)
    r(k-2) = rk%s(k-2)
    ...

'''
