#!/usr/bin/env python3

import sys, re, argparse

def is_leap_year(year):
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

class Date:
  daysinmonth = {1: 31, 2: 28, 3: 31,  4: 30,  5: 31,  6:30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}
  def __init__(self,dstring):
    mo = re.search(r'(\d{2})\.(\d{2})\.(\d{4})',dstring)
    if mo:
      self._day = int(mo.group(1))
      self._month = int(mo.group(2))
      self._year = int(mo.group(3))
    else:
      mo = re.search(r'(\d{4})-(\d{2})-(\d{2})',dstring)
      if mo:
        self._year = int(mo.group(1))
        self._month = int(mo.group(2))
        self._day = int(mo.group(3))
      else:
        raise Exception('"{}" is not a valid date'.format(dstring))
  def date2number(self):
    dayofyear = 0
    assert self._month <= 12
    for m in range(1,self._month):
      dayofyear += Date.daysinmonth[m]
      if m == 2 and is_leap_year(self._year):
        dayofyear += 1
    dayofyear += self._day
    return dayofyear
  def __str__(self):
    return '{:02d}.{:02d}.{}'.format(self._day,self._month,self._year)

def parse_arguments():
  p = argparse.ArgumentParser(description='parse dates and output')
  p.add_argument('-d','--day2number',action='store_true',default=False,
                  help='show day of date in year')
  p.add_argument('--inputfile',type=str,default='../../../../exercises/programmierung/python/Datetonumber/randomdates.csv',help='specify input file')
  return p.parse_args()
     
if __name__ == '__main__':
  args = parse_arguments()

  try:
    stream = open(args.inputfile,'r')
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  
  for line in stream:
    line = line.rstrip()
    try:
      dt = Date(line)
    except Exception as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    values = [str(dt)]
    if args.day2number:
      values.append(str(dt.date2number()))
    print('\t'.join(values))
  stream.close
