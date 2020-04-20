#!/usr/bin/env python3

import sys, re

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <DNA sequence file>\n'
                   .format(sys.argv[0]))
  exit(1)

try:
  stream = open(sys.argv[1], 'r')
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

dna = stream.read()  # return string of chars from stream
stream.close()
dna = re.sub(r'\s', '', dna)    # remove whitespace

countA = countC = countG = countT = errs = 0

# look at each base in turn, and increment
# appropriate count.
for base in dna:
  if base == 'A':
    countA += 1
  elif base == 'C':
    countC += 1
  elif base == 'G':
    countG += 1
  elif base == 'T':
    countT += 1
  else:
    sys.stderr.write('unknown base {}\n'
                       .format(base))
    errs += 1

print('A\t{}\nC\t{}\nG\t{}\nT\t{}\nerrs\t{}'
      .format(countA,countC,countG,countT,
              errs))

count_all = countA + countC + countG + countT
print('[ACGT]\t{}'.format(count_all))
print('relative frequencies')
print('A\t{:>6.2f}%'.format(100.0 * countA/count_all))
print('C\t{:>6.2f}%'.format(100.0 * countC/count_all))
print('G\t{:>6.2f}%'.format(100.0 * countG/count_all))
print('T\t{:>6.2f}%'.format(100.0 * countT/count_all))
print('G/C\t{:>6.2f}%'
       .format(100.0 * (countG+countC)/count_all))
exit(0)
