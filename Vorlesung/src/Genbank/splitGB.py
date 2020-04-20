import re, sys
from get_file_data import get_file_data

def split_genbank(filename):
  records = get_file_data(filename,'//\n')
  for record in records:
    mo = re.search(r'^(LOCUS.*ORIGIN\s*\n)(.*)',record,
                   flags = re.M | re.S)
    assert mo
    annotation = mo.group(1)
    sequence = re.sub('[\s0-9]','', mo.group(2))
    yield annotation, sequence
