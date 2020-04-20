#!/usr/bin/env python3

import re, sys

text = ('now is the time for all good men '
        'to come to the aid of their party')

countwords = dict() # emtpy dictionary
for w in re.findall(r'\w+',text):
  if not (w in countwords): # new word?
    countwords[w] = 0  # first initialize
  countwords[w] += 1   # increment count

for key, value in countwords.items():
  print('{}\t{}'.format(key,value))

def distribution_dict_new(t):
  countwords = dict()
  for w in re.findall(r'\w+',t):
    if not (w in countwords):
      countwords[w] = 0
    countwords[w] += 1
  return countwords

def distribution_dict_show(dist):
  for key, value in dist.items():
    print('{}\t{}'
           .format(key,value))

def distribution_dict_freq_show(dist):
  sum_count = 0   # sum of counts
  for count in dist.values():
    sum_count += count  # add count
  for key, count in dist.items():
    print('{}\t{:.2f}%'
           .format(key,100.0 * count/sum_count))

try:
  stream = open(__file__, 'r') # open this source file
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))

text = stream.read()
stream.close()

# now the functions declared
# above are executed
cw = distribution_dict_new(text)
distribution_dict_show(cw)
distribution_dict_freq_show(cw)
