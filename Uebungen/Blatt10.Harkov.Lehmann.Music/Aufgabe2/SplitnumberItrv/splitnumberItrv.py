#!/usr/bin/env python3

import math

def quality_function(split):
    mean = sum(split)/len(split)
    quality = math.sqrt(sum([ (s - mean)**2 for s in split ]))
    return quality


def split_number_enumerate(number, terms_of_sum):
    stack = [(number, 0, [])]
    while stack:
        remain, terms_idx, l = stack.pop()
        if remain == 0:
            yield l
        else:
            for idx, this_num in enumerate(terms_of_sum[terms_idx:]):
                if this_num > remain:
                    break
                new_l = l.copy()
                new_l.append(this_num)
                stack.append((remain - this_num, idx, new_l))


def split_number_itrv(number, terms_of_sum):
    best_split = [None, None]
    for split in split_number_enumerate(number, terms_of_sum):
        quality = quality_function(split)
        if best_split[0] is None or quality < best_split[1]:
            best_split[0] = split
            best_split[1] = quality
        best_split[0].sort()
    return best_split #Zerlegung mit dem kleinsten qualityWert. Falls gleichWertig, dann lexographisch.
