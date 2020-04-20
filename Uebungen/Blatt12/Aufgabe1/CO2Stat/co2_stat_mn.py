#!/usr/bin/env python3
import sys, re, argparse
import co2_stat

def parse_arguments():
  p = argparse.ArgumentParser(description=('extract and process CO2-emission '
                                           'data from html or tsv file'))
  p.add_argument('--tmpfile',action='store_true',default=False,
                 help=('create file tmp.pdf for output rather than a filename '
                       'which reminds of the content'))
  og = p.add_mutually_exclusive_group(required=True)
  og.add_argument('--tsv',action='store_true',default=False,
                  help='show data as tab-seoarated output')
  og.add_argument('--developing',action='store_true',default=False,
                  help='show CO2-emmission plot for some developing countries')
  og.add_argument('--middle_european',action='store_true',default=False,
                  help=('show CO2-emmission plot for some middle european '
                        'countries'))
  og.add_argument('--worst',action='store_true',default=False,
                  help=('show CO2-emmission plot for countries with largest '
                        'means'))
  og.add_argument('--big',action='store_true',default=False,
                  help=('show CO2-emmission plot for countries with most '
                        'inhabitants'))
  og.add_argument('--histogram',action='store_true',default=False,
                  help='show histogram of CO2-emissions for all countries')
  og.add_argument('--boxplot_continent',action='store_true',default=False,
                  help='show boxplots of CO2-emissions by continent')
  og.add_argument('--boxplot_region',action='store_true',default=False,
                  help='show boxplots of CO2-emissions by region')
  p.add_argument('inputfile',type=str,
                 help='specify inputfile file (.html or .tsv)')
  return p.parse_args()

developing = ['Marokko',
              'Tunesien',
              'Indonesien',
              'Malaysia',
              'Pakistan',
              'Thailand',
              'China']

middle_european = ['Vereinigtes Königreich',
                   'Deutschland',
                   'Belgien',
                   'Österreich',
                   'Niederlande',
                   'Frankreich']

big = ['China',
       'Indien',
       'Vereinigte Staaten von Amerika',
       'Indonesien',
       'Pakistan',
       'Brasilien',
       'Nigeria']

worst = ['Katar',
         'Luxemburg',
         'Bahrain',
         'Kuwait',
         'Vereinigte Arabische Emirate',
         'Vereinigte Staaten von Amerika',
         'Australien',
         'Kanada']

color_list = ['b', # blue
              'g', # green:
              'r', # red
              'c', # cyan
              'm', # magenta
              'y', # yellow
              'k', # black
              'burlywood',
              'chartreuse']

def file_prefix(args,s):
  return 'tmp' if args.tmpfile else s

args = parse_arguments()

try:
  stream = open(args.inputfile)
except IOError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

if re.search(r'\.html$',args.inputfile):
  co2_stat_table_lines = co2_stat.co2_stat_table_lines_get(stream.read())
elif re.search(r'\.tsv$',args.inputfile):
  co2_stat_table_lines = stream.readlines()
else:
  sys.stderr.write(('{}: can only process HTML files (suffix .html) or tab '
                    'separated files (suffix .tsv)\n'))
  exit(1)

co2_stat_obj = co2_stat.CO2Stat(co2_stat_table_lines)

if args.tsv:
  co2_stat_obj.show_orig()
elif args.developing:
  co2_stat_obj.plot_for_country_list(developing,
                                     color_list,
                                     'some developing',
                                     file_prefix(args,'developing'))
elif args.worst:
  co2_stat_obj.plot_for_country_list(worst,
                                     color_list,
                                     'worst',
                                     file_prefix(args,'worst'))
elif args.big:
  co2_stat_obj.plot_for_country_list(big,
                                     color_list,
                                     'big',
                                     file_prefix(args,'big'))
elif args.middle_european:
  co2_stat_obj.plot_for_country_list(middle_european,
                                     color_list,
                                     'middle_european',
                                     file_prefix(args,'middle_european'))
elif args.histogram:
  co2_stat_obj.histogram_all_emissions(file_prefix(args,'histogram'))
elif args.boxplot_continent:
  co2_stat_obj.boxplot_by_unit(True,file_prefix(args,'boxplot_continent'))
elif args.boxplot_region:
  co2_stat_obj.boxplot_by_unit(False,file_prefix(args,'boxplot_region'))
