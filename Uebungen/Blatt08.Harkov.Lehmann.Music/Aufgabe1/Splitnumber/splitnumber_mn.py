#!/usr/bin/env python3

import sys
from splitnumber import split_number

if len(sys.argv) < 3:
  sys.stderr.write('Usage: {} <number> <term_of_sum1> [<term_of_sum2> ...]>\n'
                    .format(sys.argv[0]))
  exit(1)

numbers = list()
for arg in sys.argv[1:]:
  try:
    number = int(arg)
  except ValueError:
    sys.stderr.write('{}: cannot convert "{}" to integer\n'
                      .format(sys.argv[0],arg))
    exit(1)
  numbers.append(number)

print('{}'.format('\t'.join(map(str,numbers))),end='')
best_split = split_number(numbers[0],sorted(numbers[1:]))
if best_split[1] is None:
  print('\tNone')
else:
  print('\t{:.2f}\t{}'.format(best_split[1],best_split[0]))
