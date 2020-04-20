#!/usr/bin/env python3

import sys, re, os
from multiseq import Multiseq

class RestrictFind: # class definition: keyword class and name
  iub2character = { # class var: exists only once
                          'A' : 'A',
                          'C' : 'C',
                          'G' : 'G',
                          'T' : 'T',
                          'R' : '[GA]',
                          'Y' : '[CT]',
                          'M' : '[AC]',
                          'K' : '[GT]',
                          'S' : '[GC]',
                          'W' : '[AT]',
                          'B' : '[CGT]',
                          'D' : '[AGT]',
                          'H' : '[ACT]',
                          'V' : '[ACG]',
                          'N' : '[ACGT]'
                    }
  def __init__(self, seqfile, rebase_file = 'REBASE.txt'):
    self.rebase_dict = self._parseREBASE(rebase_file) # inst var
    multiseq = Multiseq(seqfile)
    self.dna = multiseq[0].sequence

  def get_restriction_matches(self, query):
    if query in self.rebase_dict:
      recognition_site, regexp = self.rebase_dict[query]
      poslist = self._match_positions_fwd(regexp)
    else:
      raise Exception('"{}" is not a valid name'.format(query))
    return (recognition_site, poslist)
  # all methods above are public, private methods begin with _
  def _match_positions_fwd(self, regexp):
    poslist = list()
    for m in re.finditer(regexp,self.dna, flags=re.I):
      poslist.append(m.start())
    return poslist

  def _iub_to_regexp(self, iub):
    mapped = list()
    for iubchar in iub: # Replace IUB item with its character class
      if iubchar in self.iub2character:
        mapped.append(self.iub2character[iubchar])
      else:
        raise Exception('unknown IUB-character {}'.format(iubchar))
    return ''.join(mapped)

  def _parseREBASE(self, rebasefile):
    rebase_dict = dict()   # dict to be returned
    stream = open(rebasefile,'r')
    for line in stream:
      if not re.findall('^(\s+|REBASE|Rich Roberts)',line):
        fields = line.split()     # split the 2 or 3 fields
        # Remove parenthesized names by not saving the middle
        # field (if any), just the first and last
        re_name = fields.pop(0)        # extract first element
        re_site = fields.pop()          # extract last element
        # Remove ^ signs from the recognition sites
        re_site = re.sub(r'\^','',re_site)
        regex = self._iub_to_regexp(re_site)  # translate recog. site
        rebase_dict[re_name] = (re_site,regex)
    return rebase_dict  # Return dictionary with REBASE content

if __name__ == '__main__':   # called program is current file

  if len(sys.argv) < 3:
    sys.stderr.write('Usage: {} <dnafile> <rest. enzym. 1> [rest. enzym. 2..]'
                      .format(sys.argv[0]))
    exit(1)
  inputfile = sys.argv[1]
  queries = sys.argv[2:]
  try:
    rf = RestrictFind(inputfile)  # create instance rf of class
    for query in queries:  # iterate over queries = sys.args[2:]
      site, poslist = rf.get_restriction_matches(query)
      if not poslist:
        print('{}={} does not occur in DNA'.format(query,site))
      else:
        print('{}={} occurs at pos {}'
               .format(query,site,', '.join(map(str,poslist))))
  except Exception as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
