# parse a REBASE datafile parseREBASE-Parse REBASE bionet file

# Here is an extract of a REBASE file, bionet.301.
# ftp://ftp.neb.com/pub/rebase/bionet.301


# REBASE version 301                                              bionet.301

#    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#    REBASE, The Restriction Enzyme Database   http://rebase.neb.com
#    Copyright (c)  Dr. Richard J. Roberts, 2002.   All rights reserved.
#   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Rich Roberts                                                    Dec 27 2002

#AaaI (XmaIII)                     C^GGCCG
#AacI (BamHI)                      GGATCC
#AaeI (BamHI)                      GGATCC
#AagI (ClaI)                       AT^CGAT
#AaqI (ApaLI)                      GTGCAC
#AarI                              CACCTGCNNNN^
#AarI                              ^NNNNNNNNGCAGGTG
#AasI (DrdI)                       GACNNNN^NNGTC
#AatI (StuI)                       AGG^CCT
#AatII                             GACGT^C
#...
#
#YenCI (PstI)                      CTGCAG
#YenDI (PstI)                      CTGCAG
#YenEI (PstI)                      CTGCAG
#ZanI (EcoRII)                     CC^WGG
#ZhoI (ClaI)                       AT^CGAT
#ZraI (AatII)                      GAC^GTC
#Zsp2I (AvaIII)                    ATGCA^T
#
#return a dictionary where
#  key is restriction enzyme name denoted re_name
#  value is array with recognition site and regular expression

import re
from iub import iub_to_regexp
from myopen import myopen
def parseREBASE(rebasefile):
  rebase_dict = dict()   # dictionary to be returned
  stream = myopen(rebasefile)

  for line in stream:
    if not re.search(r'^(\s+|REBASE|Rich Roberts)',line):
      fields = line.split()     # split the 2 or 3 fields
      # Remove parenthesized names by not saving the middle
      # field (if any), just the first and last
      re_name = fields.pop(0)        # extract first element
      re_site = fields.pop()         # extract last element
      # Remove ^ signs from the recognition sites
      re_site = re.sub(r'\^','',re_site)
      regex = iub_to_regexp(re_site)  # translate recog. site
      rebase_dict[re_name] = (re_site,regex)

  print('parsed {} restriction enzymes'.format(len(rebase_dict)))
  return rebase_dict # Return dictionary with reformatted REBASE
