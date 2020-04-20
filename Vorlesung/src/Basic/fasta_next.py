#!/usr/bin/env python3


import sys, re

def fasta_next(filename):
  try:
    fo = open(filename,'r')
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0], err))
    exit(1)
  curr_seq_list = list()
  prevheader = None
  for line in fo:
    m = re.match('^>(.*)', line)
    if m is not None:
      if curr_seq_list:
        seq_list = re.sub('\s', '', (''.join(curr_seq_list)))
        yield prevheader, seq_list
      prevheader = m.group(1)
      curr_seq_list.clear()
    else:
      curr_seq_list.append(line)
  if curr_seq_list:
    seq_list = re.sub('\s', '', (''.join(curr_seq_list)))
    yield prevheader, seq_list

if __name__ == '__main__':
  inputfile = 'at100.fna'
  import print_sequence
  for header, seq in fasta_next(inputfile):
    print('>{}'.format(header))
    print_sequence.print_sequence(seq,70)
