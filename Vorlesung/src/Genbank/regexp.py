#!/usr/bin/env python3
import re
def show_regexp(a,regex, flags = 0):
  m = re.search(regex, a, flags = flags)
  if m:
    return a[0:m.start()] + '<<' + a[m.start():m.end()] + '>>' + a[m.end():]
  else:
    return 'no match'


#Multiline Mode: ^ and $ match at start/end
print('result: ' + show_regexp('AAC\nGTT','^.*$', flags = re.M))
print('result: ' + show_regexp('AAC\nGTT','^.*$', flags = re.M | re.S))
