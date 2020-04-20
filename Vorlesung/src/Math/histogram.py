#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from normal_pdf import normalProbabilityDensity

def evaluate_scores(mean,stddev):
  return np.random.normal(mean, stddev, 2000)

stddev = 0.1
red_mean = 0.4
red_scores = evaluate_scores(red_mean,stddev)
red_hist, red_edges = np.histogram(red_scores, density=True, bins=50)

green_mean = 0.6
green_scores = evaluate_scores(green_mean,stddev)
green_hist, green_edges = np.histogram(green_scores, density=True, bins=50)

def show_histogram(ax,scores,counts,title,bar_width,color):
  ax.set_ylabel('counts', size = 12)
  ax.set_xlabel('score', size = 12)
  ax.bar(scores,counts,width=width,color=color)

def show_hist(with_hist,with_pdf,filename):
  fig, ax = plt.subplots(figsize=(10, 5))
  if with_hist:
    if with_pdf:
      title = 'counts of scores of red and green objects/probability density'
    else:
      title = 'counts of scores of red and green objects'
  else:
    assert with_pdf
    title = 'probability density'
  ax.set_title(title,size=12)
  ax.set_ylabel('counts', size = 12)
  ax.set_xlabel('score', size = 12)
  if with_hist:
    ax.bar(red_edges[:-1], red_hist, width=0.01,color='r')
    ax.bar(green_edges[:-1], green_hist, width=0.01,color='g')
  if with_pdf:
    num_points = 1000
    x_vec = np.linspace(0, 1, num=num_points)
    for mean, color in [(red_mean,'r'),(green_mean,'g')]:
      y_vec = normalProbabilityDensity(mean,stddev,x_vec)
      ax.plot(x_vec, y_vec,color,alpha=0.5,
              label='$\mu={}, \sigma={}$'.format(mean,stddev))
      if not with_hist:
        ax.set_xlim(0,1)
        ax.set_ylim(0,4)
      ax.legend()
  fig.savefig(filename)

#show_hist(True,False,'red_green_histogram.pdf')
#show_hist(True,True,'red_green_histogram_pdf.pdf')
show_hist(False,True,'red_green_pdf.pdf')
