#!/usr/bin/env python3

import sys, re, math
#lst{TimeSeriesplt}
import matplotlib.pyplot as plt
plt.switch_backend('agg')
#lstend#

def leapyear(year):
  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    return True
  return False

def daysinmonth(is_leapyear,m):
  if m == 2:
    return 29 if is_leapyear else 28
  elif m == 4 or m == 6 or m == 9 or m == 11:
    return 30
  else:
   assert m in [1,3,5,7,8,10,12]
   return 31

#lst{TimeSeriesGroupBy}
from collections import OrderedDict

def groupby(data_list,select_func):
  groups = OrderedDict()
  for key, value in data_list:
    y = select_func(key)
    if not y in groups:
      groups[y] = list()
    groups[y].append(value)
  return groups
#lstend#

#lst{TimeSeriesDateClassClassVars}
class Date:
  _month_day2daynum = dict()
  _month_day2daynum_leap = dict()
  dyear = 1
  dyear_leap = 1
  for m in range(1,12+1):
    _month_day2daynum[m] = dict()
    _month_day2daynum_leap[m] = dict()
    for d in range(1,daysinmonth(False,m)+1):
      _month_day2daynum[m][d] = dyear
      dyear += 1
    for d in range(1,daysinmonth(True,m)+1):
      _month_day2daynum_leap[m][d] = dyear_leap
      dyear_leap += 1
#lstend#
#lst{TimeSeriesDateClassInit}
  def __init__(self,datestring):
    mo = re.search(r'(\d{4})-(\d{2})-(\d{2})',datestring)
    if not mo:
      sys.stderr.write('{}: cannot parse datastring {}\n'
                        .format(sys.argv[0],datestring))
      exit(1)
    self._year = int(mo.group(1))
    self._month = int(mo.group(2))
    self._day = int(mo.group(3))
    if leapyear(self._year):
      divisor = 366
      daynum = Date._month_day2daynum_leap[self._month][self._day]
    else:
      divisor = 365
      daynum = Date._month_day2daynum[self._month][self._day]
    self._fraction = float(self._year) + (daynum - 1)/divisor
#lstend#
#lst{TimeSeriesDateAccessors}
  def year(self):
    return self._year
  def month(self):
    return self._month
  def day(self):
    return self._day
  def fraction(self):
    return self._fraction
#lstend#
#lst{TimeSeriesDateOverloaded}
  def __str__(self):  # overload str
    return '{}-{}-{}'.format(self._year,self._month,self._day)
  def __lt__(self,other):  # overload <
    if self._year < other._year:
      return True
    if self._year <= other._year:
      if self._month < other._month:
        return True
      if self._month == other._month:
        if self._day < other._day:
          return True
    return False
#lstend#

#lst{TimeSeriesInit}
class TimeSeries:
  def __init__(self,filename,sep='\t'):
    try:
      stream = open(filename)
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],filename))
      exit(1)
    self._tsdata = list()
    self._key_name = self._value_name = previous_date = None
    for line in stream:
      values = line.strip().split(sep)
      assert len(values) >= 2
      if not self._key_name:
        self._key_name, self._value_name = values
      else:
        date = Date(values[0])
        self._tsdata.append((date,float(values[1])))
        assert not previous_date or previous_date < date
        previous_date = date
    self._firstyear = self._tsdata[0][0].year()
    self._lastyear = self._tsdata[-1][0].year()
    stream.close()
#lstend#
#lst{TimeSeriesAccessors}
  def __len__(self):
    return len(self._tsdata)
  def selectby_year(self,year):
    return [(d,v) for d, v in self._tsdata if d.year() == year]
  def data_lists(self):
    x_list = [d.fraction() for d,v in self._tsdata]
    y_list = [v for d,v in self._tsdata]
    return x_list, y_list
#lstend#
#lst{TimeSeriesGroupByYear}
  def groupby_year(self):
    return groupby(self._tsdata,lambda d: d.year())
#lstend#
#lst{TimeSeriesPlot}
  def plot(self):
    x_list, y_list = self.data_lists()
    fig, ax = plt.subplots()
    ax.set_xlabel(self._key_name)
    ax.set_ylabel(self._value_name.split()[0])
    ax.set_title('{}, {}-{}'.format(self._value_name,
                                    self._firstyear,
                                    self._lastyear))
    ax.grid(True)
    ax.plot(x_list,y_list)
    fig.savefig('temp_plot.pdf')  # save figure as pdf file
#lstend#
#lst{TimeSeriesScatter}
  def scatter(self):
    x_list, y_list = self.data_lists()
    fig, ax = plt.subplots()
    ax.set_xlabel(self._key_name)
    ax.set_ylabel(self._value_name.split()[0])
    ax.set_title('{}, {}-{}'.format(self._value_name,
                                    self._firstyear,
                                    self._lastyear))
    ax.grid(True)
    ax.scatter(x_list,y_list,s=0.5,color='black')
    fig.savefig('temp_scatter.pdf')  # save figure as pdf file
#lstend#
#lst{TimeSeriesHistogram}
  def histogram(self):
    def temp_bound(t):
      return math.ceil(t) if t > 0.0 else math.floor(t)
    _, value_list = self.data_lists()
    min_value = temp_bound(min(value_list))
    max_value = temp_bound(max(value_list))
    fig, ax = plt.subplots()
    ax.set_xlabel(self._value_name)
    ax.set_ylabel('number of events')
    ax.set_title('histogram of {}, {}-{}'
                 .format(self._value_name,self._firstyear,
                                          self._lastyear))
    ax.grid(True)
    ax.hist(value_list,bins=max_value - min_value + 1)
    fig.savefig('temp_hist.pdf')  # save figure as pdf file
#lstend#
#lst{TimeSeriesBoxplot}
  def boxplot(self):
    groups = self.groupby_year()
    fig, ax = plt.subplots()
    ax.set_title('{}, {}-{}'
                 .format(self._value_name,min(groups.keys()),
                                          max(groups.keys())))
    ax.set_xlabel('year')
    ax.set_ylabel(self._value_name.split()[0])
    ax.boxplot(groups.values(),labels=groups.keys())
    fig.savefig('temp_boxplot.pdf')  # save figure as pdf file
#lstend#
#lst{TimeSeriesViolinplot}
  def violinplot(self):
    groups = self.groupby_year()
    fig, ax = plt.subplots()
    ax.set_title('{}, {}-{}'
                 .format(self._value_name,min(groups.keys()),
                                          max(groups.keys())))
    ax.set_xlabel('year')
    ax.set_ylabel(self._value_name.split()[0])
    ax.violinplot(groups.values(),showmedians=True)
    keys = list(groups.keys())
    ax.set_xticks(list(range(1,len(keys)+1)))
    ax.set_xticklabels(keys)
    fig.savefig('temp_violinplot.pdf')  # save figure as pdf file
#lstend#
#lst{TimeSeriesSubplot}
  def subplot(self):
    groups = self.groupby_year()
    rows = len(groups)
    fig, ax = plt.subplots(rows,1)
    ax[0].set_title('{}, {}-{}'.format(self._value_name,
                                       min(groups.keys()),
                                       max(groups.keys())))
    ax[rows-1].set_xticks([1] + list(range(25,365,25)))
    for idx, year in enumerate(groups.keys()):
      ax[idx].set_ylabel('{}'.format(year),fontsize=9)
      ax[idx].plot(groups[year])
    fig.savefig('temp_subplot.pdf')  # save figure as pdf file
#lstend#
#lst{TimeSeriesBoxplotMonthly}
  def boxplot_monthly(self,year):
    date_one_year = self.selectby_year(year)
    groups = groupby(date_one_year,lambda d: d.month())
    fig, ax = plt.subplots()
    ax.set_title('{} in {} over 12 month'
                 .format(self._value_name,year))
    ax.set_xlabel('month')
    ax.set_ylabel('temperature (C)')
    ax.boxplot(groups.values(),labels=groups.keys())
    fig.savefig('temp_monthly_{}.pdf'.format(year))  # save as pdf
#lstend#

#lst{TimeSeriesMain}
from temp_args import temp_parse_arguments
args = temp_parse_arguments(\
           with_hsmth=False,with_heat=False,
           with_lag=False,with_acor=False)
tseries = TimeSeries('temperature.tsv')
print('{} data points in time series'
       .format(len(tseries)))
if args.std:
  tseries.plot()
elif args.scatter:
  tseries.scatter()
elif args.hist:
  tseries.histogram()
elif args.boxp:
  tseries.boxplot()
elif args.violinp:
  tseries.violinplot()
elif args.ysub:
  tseries.subplot()
elif args.year:
  tseries.boxplot_monthly(args.year)
else:
  assert False
#lstend#
