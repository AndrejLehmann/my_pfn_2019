#!/usr/bin/env python3

import sys, re, argparse

def is_leap_year(year):
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def date2daynum(year,month,day):
  daysinmonth = {1: 31, 2: 28, 3: 31,  4: 30,  5: 31,  6:30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}
  dayofyear = 0
  assert month <= 12
  for m in range(1,month):
    dayofyear += daysinmonth[m]
    if m == 2 and is_leap_year(year):
      dayofyear += 1
  dayofyear += day
  return dayofyear

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
    mo = re.search(r'(\d{2})\.(\d{2})\.(\d{4})',line)
    if not mo:
      sys.stderr.write('{}: line {} has incorrect format\n'
                        .format(sys.argv[0],line))
      exit(1)
    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))
    dayofyear = date2daynum(year,month,day)
    print('{}\t{}'.format(line,dayofyear))
  stream.close
