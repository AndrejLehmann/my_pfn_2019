#!/usr/bin/env python3

import sys

english2german =  {
  'dog'   : 'Hund',
  'robin' : 'Rotkehlchen',
  'asp'   : 'Natter'
  }

english2german['pearl'] = 'Perle'

print('dog={}'.format(english2german['dog']))
print('pearl={}'.format(english2german['pearl']))

print('{}'.format(','.join(english2german.keys())))
print('{}'.format(','.join(english2german.values())))

if 'dog' in english2german:
  print('dog={}'.format(english2german['dog']))
else:
  sys.stderr.write('{}: no translation for "dog"\n'.format(sys.argv[0]))
