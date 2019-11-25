#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 1.5h

import sys, re
from math import log10


if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <inputfile>\n'.format(sys.argv[0]))
  exit(1)

inputfile = sys.argv[1]
try:
  stream = open(inputfile)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)


score_dict = {}
log10expectVal_dict = {}
relIdent_dict = {}


def addToDict(dic,val):
    val = int(val)
    if val not in dic:
        dic[val] = 1 
    else:
        dic[val] += 1 

for line in stream:
    # Expect format: e.g. 5e-32 = 5*10**(-32)
    ScoreExpect_line = re.search(
                  r'^Score = (\S+) bits \(\S+\), Expect = (\S+)', 
                  line)
    if ScoreExpect_line:

        score = round(float(ScoreExpect_line.group(1)))
        expectVal = float(ScoreExpect_line.group(2))
        if expectVal == 0.0: 
            log10expectVal = 0.0
        else:
            log10expectVal = round(log10(expectVal))
        addToDict(score_dict,score)
        addToDict(log10expectVal_dict,log10expectVal)

    else:

        Identities_line =  re.search(
                      r'^Identities =+ \S+ \((\S+)%\)',
                      line)
        relIdentities = Identities_line.group(1)
        addToDict(relIdent_dict,relIdentities)


print("# distribution of bitscores")
print("# Fields: bitscore, occurrences")
for k in sorted(score_dict):
    print("{}\t{}".format(k,score_dict[k]))

print("# distribution of identities")
print("# Fields: identity, occurrences")
for k in sorted(relIdent_dict):
    print("{}\t{}".format(k,relIdent_dict[k]))

print("# distribution of log10(expect)")
print("# Fields: log10(expect), occurrences")
for k in sorted(log10expectVal_dict):
    print("{}\t{}".format(k,log10expectVal_dict[k]))
