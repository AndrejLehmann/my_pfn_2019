import os, sys
from myopen import myopen

# split the entire file on sep and return the resulting units
def get_file_data(filename, sep = '\n'): # default sep is newline
  stream = myopen(filename)
  units = stream.read().split(sep)
  stream.close()
  assert len(units) > 0 and units[-1] == ''
  units.pop()
  return units
