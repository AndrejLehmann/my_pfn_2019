#!/usr/bin/env python3

import re, sys

class SeqEntry:
  def __init__(self,header,sequence):
    self.header = header
    self.sequence = sequence

  def show(self,line_width = 70):
    line_list = list()
    print('>{}'.format(self.header))
    for startpos in range(0,len(self.sequence),line_width):
      print(self.sequence[startpos : startpos + line_width])

def seq_list2seq(seq_list):
  sequence = ''.join(seq_list)
  return re.sub('\s','',sequence)

def filename2stream(filename):
  if filename != '-':
    try:
      stream = open(filename,'r')
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    return stream
  return sys.stdin

def fasta2seq_entries(stream):
  seq_entries = list()
  header, seq_list = None, list()
  for line in stream:
    if not re.search(r'^(>|\s*$)',line):
      seq_list.append(line.rstrip())
    elif len(line) > 0 and line[0] == '>':
      if header:
        seq_entry = SeqEntry(header,seq_list2seq(seq_list))
        seq_entries.append(seq_entry)
        seq_list.clear()
      header = line[1:-1]
  if header:
    seq_entry = SeqEntry(header,seq_list2seq(seq_list))
    seq_entries.append(seq_entry)
  return seq_entries

def genbank2seq_entries(stream):
#INCLUDE  return # implement this function here
#BEGIN{exclude}
  desc, header, seq_lines = None, None, None
  seq_entries = list()
  for line in stream:
    line = line.rstrip()
    if re.search(r'^\/\/$', line): # end-of-record line //
      seq_entry = SeqEntry(header,re.sub(r'[\s0-9]','', ''.join(seq_lines)))
      seq_entries.append(seq_entry)
      header = None
      seq_lines = None
      desc = None
    elif seq_lines is not None: # we are in a sequence
      seq_lines.append(line)   # add current line to array
    elif re.search(r'^ORIGIN', line): # line before sequence part
      seq_lines = list()    # now start with the sequences
    elif re.search(r'^DEFINITION',line):
      desc = re.sub(r'^DEFINITION\s*','',line)
    elif re.search(r'^ACCESSION', line): # line before sequence part
      accession = re.sub(r'^ACCESSION\s*','',line)
      header = '{} {}'.format(accession,desc)
      desc = None
    elif desc:
      desc += re.sub(r'\s+',' ',line)
  return seq_entries
#END{exclude}

class Multiseq:
  def __init__(self,filename):
    stream = filename2stream(filename)
    if re.search(r'\.gb$',filename):
      self.seq_entries = genbank2seq_entries(stream)
    else:
      self.seq_entries = fasta2seq_entries(stream)
    if filename != '-':
      stream.close()
  def __getitem__(self, idx):
    assert idx >= 0 and idx < len(self.seq_entries)
    return self.seq_entries[idx]

  def __iter__(self):
    return iter(self.seq_entries)

  def __len__(self):
    return len(self.seq_entries)

  def show(self,line_width):
    for seq_entry in self:
      seq_entry.show(line_width)

import argparse

def parse_arguments():
  p = argparse.ArgumentParser()
  p.add_argument('-t','--total_length',action='store_true',default=False,
                 help='output total length of sequences')
  p.add_argument('-s','--show',type=int,default=None,
                 metavar='<line_width>',
                 help=('show all sequences with line width given as argument'))
  p.add_argument('-p','--pattern',type=str,metavar='<p>',default=None,
                 help='select sequences matching pattern <p> in header line')
  p.add_argument('inputfile',type=str,
                  help='specify input file, - means stdin')
  return p.parse_args()

if __name__ == '__main__':
  args = parse_arguments()
  multiseq = Multiseq(args.inputfile)
  total_length = 0
  args = parse_arguments()
  for seq_entry in multiseq:
    if not args.pattern or \
       re.search(r'{}'.format(args.pattern),seq_entry.header):
      if args.show:
        seq_entry.show(args.show)
      if args.total_length:
        total_length += len(seq_entry.sequence)
  if args.total_length:
    print('total_length={}'.format(total_length))
