#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import argparse, re

def parse_arguments():
  p = argparse.ArgumentParser(description=('plot file with X/Y coordiates in '
                                           'given .tsv file'))
  p.add_argument('inputfile',type=str,
                  help='specify input file')
  return p.parse_args()

args = parse_arguments()

coors = np.loadtxt(args.inputfile)
x_list, y_list = coors.T
fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x_list,y_list)
m = re.search(r'(.*)\.tsv',args.inputfile)
if m:
  outputfile = '{}.pdf'.format(m.group(1))
else:
  outputfile = 'tmp.pdf'

fig.savefig(outputfile)
