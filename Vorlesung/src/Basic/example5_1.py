#!/usr/bin/env python3
# Example 5-1   if-elsif-else

word = 'MNIDDKL'

# if-elsif-else conditionals
if word == 'QSTVSGE':
  print('QSTVSGE')
elif word == 'MRQQDMISHDEL':
  print('MRQQDMISHDEL')
elif word == 'MNIDDKL':
  print('MNIDDKL-the magic word!')
else:
  print('Is "{}" a peptide? This program is not sure.'.format(word))

exit(0)
