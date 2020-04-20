#!/usr/bin/env python3

score = 39

if score >= 85:
  print('sehr gut')
else:
  if score >= 70:
    print('gut')
  else:
    if score >= 55:
      print('befriedigend')
    else:
      if score >= 40:
        print('ausreichend')
      else:
        print('nicht bestanden')

score = 40

if score >= 85:
  print('sehr gut')
elif score >= 70:
  print('gut')
elif score >= 55:
  print('befriedigend')
elif score >= 40:
  print('ausreichend')
else:
  print('nicht bestanden')
