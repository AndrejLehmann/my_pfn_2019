#!/usr/bin/env python3

from math import floor, ceil

from data_matrix_class import DataMatrix
#lst{webscrapestathtmlget}
import re, argparse, requests

def gb_stat_html_get(from_web):
  if from_web:
    urlstring = 'https://www.ncbi.nlm.nih.gov/genbank/statistics/'
    request_gb_stat = requests.get(urlstring)
    gb_stat_html = request_gb_stat.content
  else:
    stream = open('statistics2019-01-02.html')
    gb_stat_html = stream.read()
    stream.close()
  return gb_stat_html
#lstend#

#lst{webscrapestattablelinesget}
from bs4 import BeautifulSoup

def gb_stat_table_lines_get(gb_stat_html):
  soup = BeautifulSoup(gb_stat_html,features='html.parser')
  table = soup.find('table', attrs = {'id': 'stats_table'})
  assert table
  thead = table.find('thead') # not used
  tbody = table.find('tbody')
  h_list = ['release','date','gb_bp','gb_seqs','wgs_bp','wgs_seqs']
  gb_stat_table_lines = ['\t'.join(h_list)]
  for six_tup in tbody.find_all('tr'):
    data_fields = [td.text for td in six_tup.find_all('td')]
    assert len(data_fields) == 6
    gb_stat_table_lines.append('\t'.join(data_fields))
  return gb_stat_table_lines
#lstend#

def gb_stat_data_matrix_get(gb_stat_tables_lines):
#lst{webscrapestatdatamatrixget}
  key_col = 0 # the release number
  gb_stat_data_matrix = DataMatrix(gb_stat_table_lines,key_col,
                                   sep='\t',ordered=True)
#lstend#
  return gb_stat_data_matrix

#lst{webscrapemonthdictget}
def month_dict_get():
  month_list = ['Jan','Feb','Mar','Apr','May','Jun',\
                'Jul','Aug','Sep','Oct','Nov','Dec']
  month_dict = dict()
  for idx, m in enumerate(month_list):
    month_dict[m] = idx
  return month_dict
#lstend#

#lst{webscrapedatetofloat}
def date2float(month_dict,date_string):
  mo = re.search(r'(^[A-Z][a-z]{2}) (\d+)$',date_string)
  assert mo
  month = mo.group(1)
  assert month in month_dict
  return float(mo.group(2)) + month_dict[month]/12.0
#lstend#

#lst{webscrapeprepareplotdata}
def prepare_plot_data(gb_stat_matrix):
  month_dict = month_dict_get()
  dates = [date2float(month_dict,date) \
           for date in gb_stat_matrix.attribute_select('date')]
  gb_bp = [int(s)\
           for s in gb_stat_matrix.attribute_select('gb_bp')]
  assert len(dates) == len(gb_bp)
  wgs_bp = [int(s)\
            for s in gb_stat_matrix.attribute_select('wgs_bp')\
            if s != '']
  wgs_dates = dates[len(dates) - len(wgs_bp):]
  assert len(wgs_dates) == len(wgs_bp)
  return dates, gb_bp, wgs_dates, wgs_bp
#lstend#

#lst{webscrapeplotthedata}
import matplotlib.pyplot as plt
plt.switch_backend('agg') # to allow remote use

def plot_the_data(scatter, dates, gb_bp, wgs_dates, wgs_bp):
  fig, ax = plt.subplots()
  ax.grid(True)
  ax.set_title('size of Genbank/WGS from {:.0f} to {:.0f}'
               .format(floor(dates[0]),floor(dates[-1])))
  ax.set_xlabel('years')
  ax.set_ylabel('log(size) (bp)')
  ax.set_yscale('log')
  ax.set_xlim(floor(dates[0]),ceil(dates[-1]))
  if scatter:
    ax.scatter(dates, gb_bp, s=0.5, color='blue', label='Genbank')
    ax.scatter(wgs_dates, wgs_bp, s=0.5, color='red', label='WGS')
  else:
    ax.plot(dates, gb_bp, color='blue',label='Genbank')
    ax.plot(wgs_dates, wgs_bp, color='red', label='WGS')
  ax.legend(loc='upper left')
  fig.savefig('genbank_{}.pdf'
              .format('scatter' if scatter else 'plot'))
#lstend#

#lst{webscrapeparsearguments}
def parse_arguments():
  p = argparse.ArgumentParser(description=('plot statistics '
                                           'of Genbank size'))
  p.add_argument('-w','--web',action='store_true',default=False,
                 help='get information from web via URL')
  p.add_argument('-s','--scatter',action='store_true',
                 default=False,help=('show scatter plot rather '
                                     'than continuous plot'))
  return p.parse_args()
#lstend#

#lst{webscrapemain}
args = parse_arguments()
gb_stat_html = gb_stat_html_get(args.web)
gb_stat_table_lines = gb_stat_table_lines_get(gb_stat_html)
key_col = 0 # the release number
gb_stat_matrix = DataMatrix(gb_stat_table_lines,key_col,
                            sep='\t',ordered=True)
dates, gb_bp, wgs_dates, wgs_bp = prepare_plot_data(gb_stat_matrix)
plot_the_data(args.scatter,dates, gb_bp, wgs_dates, wgs_bp)
#lstend#
