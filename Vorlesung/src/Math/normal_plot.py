#!/usr/bin/env python3

from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import argparse
from normal_pdf import normalProbabilityDensity

def parse_arguments():
  p = argparse.ArgumentParser(description='plot normal distribution')
  default_left=-3.0
  p.add_argument('-l','--left',type=float,default=default_left,metavar='<float>',
                 help=('specify left boundary of range for plot, default: {}')
                       .format(default_left))
  default_right=3.0
  p.add_argument('-r','--right',type=float,default=default_right,
                 metavar='<float>',
                 help=('specify right boundary of range for plot, default: 3.0')
                       .format(default_right))
  default_mean=0.0
  p.add_argument('-m','--mean',type=float,default=default_mean,
                 metavar='<float>',
                 help=('specify mean of normal distribution, default: {}')
                      .format(default_mean))
  default_stddev=1.0
  p.add_argument('-s','--stddev',type=float,default=default_stddev,
                 metavar='<float>',
                 help=('specify stddev of normal distribution, default: {}')
                       .format(default_stddev))
  return p.parse_args()

def plot_normal(left,right,mean,stddev):
  x_vec = np.linspace(left,right,num = 100)
  y_vec = normalProbabilityDensity(mean,stddev,x_vec)
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.plot(x_vec, y_vec)
  ax.set_ylim(0)
  ax.set_title('Normal Distribution for $\mu={}, \sigma={}$'
               .format(mean,stddev),
                size = 12)
  ax.set_ylabel('Probability Density', size = 12)
  fig.savefig('normal_plot.pdf')

def quad_123(mean,stddev):
  for diff in range(1,3+1):
    integral, _ = quad(lambda x: normalProbabilityDensity(mean,stddev,x),
                       mean - diff, mean + diff, limit = 1000)
    print('{}\t{}'.format(diff,result))

args = parse_arguments()

plot_normal(args.left,args.right,args.mean,args.stddev)
