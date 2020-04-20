#!/usr/bin/env python3

import re
import sys

dna1 = 'ACGT'
dna2 = 'TATA'
dna3 = dna1 + dna2

num1 = 42
num2 = 56
print('sum is',num1 + num2)
print('sum is {}'.format(num1 + num2))

dna = 'AGCTATCAGCGATCTACGAGCGACGCA'
rna = re.sub('T','U',dna)

if 1 == 1:
  print('1 equals 1')

if 1:
  print('1 evaluates to True')

if 1 == 0:
  print('1 equals 0')
else:
  print('1 does not equal 0')

if not 1 == 0:
  print('1 does not equal 0')

if 1 != 0:
  print('1 does not equal 0')

word = 'MNIDDKL'
if word == 'QSTVSGE':
  print('QSTVSGE')
elif word == 'MRQQDMISHDEL':
  print('MRQQDMISHDEL')
elif word == 'MNIDDKL':
  print('MNIDDKL-the magic word!')
else:
  print('Cannot decide if "{}" is peptide'.format(word))

seq = 'ACGT'
if seq == 'AAAAAA':
  print('may be Poly-A tail')
elif seq == 'TATAAT':
  print('may be a Pribnow Box')
elif seq == 'GGCCAATCT':
  print('may be a CCAAT Box')
else:
  print('Cannot decide if "{}" is regulatory element'.format(seq))

filename = input('type filename of the sequence: ')
filename = filename.rstrip()

sequence_lines = ['AGCTACG','ATTCAGC']
sequence = ''.join(sequence_lines)

sequence = re.sub(r'\s','',sequence)

motif = 'E{2}J'
m = re.search(r'{}'.format(motif), sequence)
if m is not None:
  print('found')

dna = sys.argv[0]

english2german = {
  'Hydrogen' : 'Wasserstoff',
  'Carbon'   : 'Kohlenstoff',
  'Sulfur'   : 'Schwefel'
  }

english2german['Iron'] = 'Eisen'

germanword = english2german['Iron']

translatedwords = list(english2german.keys())
translations = list(english2german.values())

def codon2aa(codon):
  codon = codon.upper()
  if   codon == 'TCA': return 'S'     # Serine
  elif codon == 'TCC': return 'S'     # Serine
  elif codon == 'TCG': return 'S'     # Serine
  elif codon == 'TCT': return 'S'     # Serine
  # ... 64 - 7 similar lines
  elif codon == 'GGC': return 'G'     # Glycine
  elif codon == 'GGG': return 'G'     # Glycine
  elif codon == 'GGT': return 'G'     # Glycine
  else:
    sys.stderr.write('Bad codon "{}"\n'.format(codon))
    exit(1)

def codon2aa(codon):
  codon = codon.upper()
  if   re.search(r'GC.',codon):    return 'A'  # Alanine
  elif re.search(r'TG[TC]',codon): return 'C'  # Cysteine
  elif re.search(r'GA[TC]',codon): return 'D'  # Aspartic Acid
  elif re.search(r'GA[AG]',codon): return 'E'  # Glutamic Acid
  elif re.search(r'TT[TC]',codon): return 'F'  # Phenylalanine
  # ...  20 + 1 - 9 similar lines
  elif re.search(r'GT.',codon):        return 'V'  # Valine
  elif re.search(r'TGG',codon):        return 'W'  # Tryptophan
  elif re.search(r'TA[TC]',codon):     return 'Y'  # Tyrosine
  elif re.search(r'TA[AG]|TGA',codon): return '_'  # Stop
  else:
    sys.stderr.write('Bad codon "{}"\n'.format(codon))
    exit(1)

genetic_code = {
  'TCA' : 'S',    # Serine
  'TCC' : 'S',    # Serine
  'TCG' : 'S',    # Serine
  'TCT' : 'S',    # Serine
  'TTC' : 'F',    # Phenylalanine
  # ...  55 more similar lines
  'GGA' : 'G',    # Glycine
  'GGC' : 'G',    # Glycine
  'GGG' : 'G',    # Glycine
  'GGT' : 'G',    # Glycine
}
def codon2aa(codon):
  if codon in genetic_code:
    return genetic_code[codon]
  else:
    sys.stderr.write('Bad codon {}\n'
                      .format(codon))
    exit(1)

def dna2peptide(dna):
  return ''

dna = 'CGACGTCTTCGTACGGGACTAGCTCGTGTCGGTCGC'
peptide = dna2peptide(dna)
print('translated DNA {}\ninto protein {}'.format(dna, peptide))

a = 'cruel world'
pattern = re.compile(r'(\w+)')
for w in re.findall(pattern, a):
  print('<{}> '.format(w), end='')         # print words in brackets
print('\n', end='')
pattern = re.compile(r'(.)(.)')
for (c, b) in re.findall(pattern, a):
  print('{}{}'.format(b, c), end='')# flip pairs of consecutive chars
print('\n', end='')

arr = ['a', 'b', 'c', 'd']
for elem in range(len(arr)):
  arr[elem] = arr[elem] + 'X'

x = 9
y = 8
if ((3 <= x) and (x <= 10)) \
    or ((y % 2) != 0):
  if 9 * (x + 2) >= 99:
    print('success')

l = list()
l.append(1)
l.append(4)

def fahr2kelv(temp):
  return ((temp - 32) * (5/9)) + 273.15

print('freezing point of water in K: {}'.format(fahr2kelv(32)))
print('boiling point of water in K: {}'.format(fahr2kelv(212)))

def kelv2cels(temp):
  return temp - 273.15

print('absolute zero in C: {}'.format(kelv2cels(0.0)))

def fahr2cels(temp_f):
  temp_k = fahr2kelv(temp_f)
  return kelv2cels(temp_k)

print('freezing point of water in C: {}'.format(fahr2cels(32.0)))
