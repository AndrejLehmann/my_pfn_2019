#!/usr/bin/env python3

#lst{SortedListofStrings}
unsorted_word_list = ['ag','ga','a','aaa','ca']
sorted_word_list = sorted(unsorted_word_list)
print('unsorted_word_list={}'.format(unsorted_word_list))
print('  sorted_word_list={}'.format(sorted_word_list))
unsorted_int_list = [5,3,1,-4,0,6]
unsorted_int_list.sort()
print('unsorted_list2={}'.format(unsorted_int_list))
#lstend#

#lst{SortDictionarybyKeys}
eop_dist = {'=' : 5, 'I' : 3, 'X' : 4, 'D' : 1}
print('sorted keys of eop_dist={}'.format(sorted(eop_dist)))
#lstend#

#lst{SortWordListbyLength}
length_sorted_word_list = sorted(unsorted_word_list,key=len)
print('length_sorted_word_list = {}'
       .format(length_sorted_word_list))
#lstend#

#lst{ValuesSortedDictKeysFunction}
def values_sorted_dict_keys(d):
  def apply_dict(k):
    return d[k]
  return sorted(d,key=apply_dict)

print('values_sorted_eop_dist_keys={}'
        .format(values_sorted_dict_keys(eop_dist)))
#lstend#

#lst{ValuesSortedDictKeysLambda}
print('values_sorted_eop_dist_keys={}'
       .format(sorted(eop_dist,key=lambda k: eop_dist[k])))
#lstend#

#lst{ProteintripleslistsortbyLength}
protein_triples = [('Q65209','African swine fever virus',141),
                   ('Q00020','Broad bean mottle virus',1164),
                   ('P03588','Brome mosaic virus',961),
                   ('Q83264','Cucumber mosaic virus',993)]

for protein in sorted(protein_triples,key=lambda p: p[2]):
  print('{}\t{}'.format(protein[1],protein[2]))
#lstend#

#lst{ProteinlistsortbyLength}
class Protein:
  def __init__(self, accession, name, length):
    self.accession = accession
    self.name = name
    self.length = length
  def __str__(self):
    return '{}\t{}'.format(self.name,self.length)

protein_list = [Protein('Q65209','African swine fever virus',141),
                Protein('Q00020','Broad bean mottle virus',1164),
                Protein('P03588','Brome mosaic virus',961),
                Protein('Q83264','Cucumber mosaic virus',993)]
for protein in sorted(protein_list,key=lambda p: p.name):
  print(protein)
#lstend#

#lst{ProteinlistsortItemAttrGetter}}
from operator import itemgetter, attrgetter

for protein in sorted(protein_triples,key=itemgetter(2)):
  print('{}\t{}'.format(protein[1],protein[2]))

for protein in sorted(protein_list,key=attrgetter('length')):
  print(protein)
#lstend#

#lst{SortedEopDictItemGetter}}
for eop, count in sorted(eop_dist.items(),\
                         key=itemgetter(1),\
                         reverse=True):
  print('{}\t{}'.format(eop,count))
#lstend#

#lst{SortColorsStable}
colors = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(colors,key=itemgetter(0)))
#lstend#
