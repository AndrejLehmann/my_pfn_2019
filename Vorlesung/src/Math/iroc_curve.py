#!/usr/bin/env python3

# execute as
# bokeh serve iroc_curve.py

import numpy as np
from math import ceil
from multi_interactive_plot import MultiInteractivePlot
from normal_pdf import normalProbabilityDensity
from roc import integral_pointlist

MIN_X = 0
MAX_X = 1

sliders_spec = [('mean1 ','m1',0,1,0.4,0.01),
                ('stddev1 ','sd1',0.1,0.8,0.1,0.01),
                ('mean2 ','m2',0,1,0.6,0.01),
                ('stddev2 ','sd2',0.1,0.8,0.1,0.01),
                ('threshold ','t',MIN_X,MAX_X,0.5,0.01)]

def tail_dist(y_vec):
  tail = np.zeros((len(y_vec),))
  tail_sum = 0
  for idx in range(len(y_vec)-1,-1,-1):
    tail_sum += y_vec[idx]
    tail[idx] = tail_sum
  return tail

def normal_pdf_args(args):
  mean1 = args[0]
  stddev1 = args[1]
  def norm_pdf1(x):
    return normalProbabilityDensity(mean1,stddev1,x)
  mean2 = args[2]
  stddev2 = args[3]
  def norm_pdf2(x):
    return normalProbabilityDensity(mean2,stddev2,x)
  threshold = args[4]
  n_points = 200
  x_vec1 = np.linspace(MIN_X,MAX_X,n_points)
  y_vec1 = norm_pdf1(x_vec1)
  tail1 = tail_dist(y_vec1)
  total1 = np.sum(y_vec1)
  x_vec2 = np.linspace(MIN_X,MAX_X,n_points)
  y_vec2 = norm_pdf2(x_vec2)
  tail2 = tail_dist(y_vec2)
  total2 = np.sum(y_vec2)
  fprs = (lambda v: v/total1)(tail1)
  tprs = (lambda v: v/total2)(tail2)
  for idx in range(len(tail1)):
    if tprs[idx] < fprs[idx]:
      tprs[idx] = fprs[idx]
  x_vec3 = np.array([threshold] * n_points)
  y_vec3 = np.linspace(0,max(np.max(y_vec1),np.max(y_vec2)),n_points)
  x_roc_worst = np.linspace(0,1,n_points)
  y_roc_worst = x_roc_worst
  if MIN_X < 0:
    scaled_index = ceil((n_points - 1) *
                        (1 + (threshold + MIN_X)/(MAX_X - MIN_X)))
  else:
    scaled_index = ceil((n_points - 1) *
                        ((threshold - MIN_X)/(MAX_X - MIN_X)))
  this_fpr = fprs[scaled_index]
  this_tpr = tprs[scaled_index]
  auc = integral_pointlist(fprs,tprs)
  return [x_vec1,x_vec2,x_vec3,x_roc_worst,fprs,this_fpr,auc], \
         [y_vec1,y_vec2,y_vec3,y_roc_worst,tprs,this_tpr,None]

colors = ['red','green','black','magenta','blue']
MultiInteractivePlot(['norm PDF','ROC curce'],3,2,colors,normal_pdf_args,
                     sliders_spec)
