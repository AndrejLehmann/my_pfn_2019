#!/usr/bin/env python3

import math, re
from temp_args import temp_parse_arguments
import pandas as pd
from matplotlib import pyplot
from pandas.plotting import lag_plot, autocorrelation_plot

args = temp_parse_arguments()

series = pd.read_csv('temperature.tsv', header=0,
                     sep='\t', squeeze=True, index_col=0)
series.index = pd.to_datetime(series.index, dayfirst=True)

x_min = min(series)
x_max = max(series)
print(series.head())

key = None
if args.std:
  key = 'std'
  series.plot()
elif args.scatter:
  key = 'scatter'
  series.plot(style='k.')
elif args.hist:
  key = 'hist'
  pyplot.xlim(math.ceil(x_min),math.ceil(x_max))
  series.hist()
elif args.lag:
  key = 'lag'
  lag_plot(series)
elif args.acor:
  key= 'acor'
  autocorrelation_plot(series)
elif args.hsmth:
  key = 'hsmth'
  pyplot.xlim(math.ceil(x_min),math.ceil(x_max))
  series.plot.kde()
elif args.boxp or args.ysub or args.heat:
  years = pd.pivot(columns=series.index.year,
                   index=series.index.dayofyear,
                   values=series)
  years = years.drop(366)
  if args.boxp:
    key = 'boxp'
    years.boxplot()
  elif args.ysub:
    key = 'ysub'
    years.plot(subplots=True, legend=False)
  else:
    key = 'heat'
    years = years.T
    pyplot.matshow(years, interpolation=None, aspect='auto')
elif args.year:
  key = 'year_{}'.format(args.year)
  one_year = series[str(args.year)]
  months = pd.pivot(columns=one_year.index.month,
                    index=one_year.index.day,
                    values=one_year)
  months.boxplot()
else:
  assert False
assert key
print('key={}'.format(key))
pyplot.savefig('temp_pd.pdf')
