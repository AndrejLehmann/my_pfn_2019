#!/usr/bin/env python3

import sys, re

def print_sequence(seq,linelength = 70):
  for startpos in range(0,len(seq),linelength):
    print(seq[startpos:startpos+linelength])

def seq_list2sequence(seq_list):
  sequence = ' '.join(seq_list)
  return re.sub('\s','',sequence)

def fasta_next(filename):
  if filename == '-':
    stream = sys.stdin
  else:
    try:
      stream = open(filename,'r')
    except IOError as err:
      sys.stderr.write('{}: {}\n'
                        .format(sys.argv[0],err))
      exit(1)
  seq_list = list()
  header = None
  for line in stream:
    if not re.search(r'^(>|\s*$|\s*#)',line):
      seq_list.append(line.rstrip())
    else:
      m = re.search(r'^>(.*)',line)
      if not (m is None):
        if not (header is None):
          yield header, seq_list2sequence(seq_list)
          seq_list.clear()
        header = m.group(1)
  if not (header is None):
    yield header, seq_list2sequence(seq_list)
  if filename != '-':
    stream.close()

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write('Usage: {} <fastafile>\n'.format(sys.argv[0]))
    exit(1)
  for header, sequence in fasta_next(sys.argv[1]):
    print('>{}'.format(header))
    print_sequence(sequence, 64)
