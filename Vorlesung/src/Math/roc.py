#!/usr/bin/env python3
import re
import matplotlib.pyplot as plt
from normal_dist_class import NormalDist

def plot_pdfs(d_red,d_green,ax):
  ax.set_title('probability densities',size = 12)
  ax.set_ylabel('counts', size = 12)
  ax.set_xlabel('score', size = 12)
  ax.set_xlim(0,1)
  ax.set_ylim(0,4)
  d_red.plot(ax)
  d_green.plot(ax)

# could also use metrics.auc if import sklearn.metrics as metrics

def annotate(ax):
  threshold=0.6
  ax.axvline(x=threshold,color='black')
  ax.text(threshold,2,'threshold $t$',rotation='vertical')
  ax.text(threshold + 0.015, 0.1, 'FP')
  ax.text(threshold + (0.75 - threshold)/2 , 2, 'TP')
  ax.axvspan(threshold, 1, alpha=0.1, color='grey')
  x_t = 0.78
  y_t = 2.6
  for text in ['negatives = red',
               r'$FP(t) = red \geq t$',
               'positives = green',
               r'$TP(t) = green \geq t$',
               r'$FPR(t) = \frac{|FP(t)|}{|negatives|}$',
               r'$TPR(t) = \frac{|TP(t)|}{|positives|}$',
               r'$ROC: FPR(t) \mapsto TPR(t)$',
               'for varying $t$']:
    ax.text(x_t,y_t,text)
    if re.search(r'\\frac',text):
      y_t -= 0.3
    else:
      y_t -= 0.2

def integral_pointlist(fprs,tprs):
  assert len(fprs) == len(tprs)
  pairs = sorted(zip(fprs,tprs))
  area = 0
  prev_x, prev_y = pairs[0]
  for x, y in pairs[1:]:
    assert prev_x <= x
    area += 0.5 * (x - prev_x) * (prev_y + y)
    prev_x, prev_y = x, y
  return area

def roc_curve_collect(d_red, d_green):
  tot_d_red = d_red.sum()
  tot_d_green = d_green.sum()
  FPRs = [v/tot_d_red for v in d_red.tail()]
  TPRs = [v/tot_d_green for v in d_green.tail()]
  auc = integral_pointlist(FPRs,TPRs)
  return FPRs, TPRs, auc

def roc_curve_plot(d_red, d_gr, ax):
  x = d_gr.domain()
  FPRs, TPRs, auc = roc_curve_collect(d_red, d_gr)
  ax.plot(FPRs,TPRs,'b-')
  ax.plot(x,x, 'm--')
  ax.set_xlim([0,1])
  ax.set_ylim([0,1])
  ax.set_title('ROC Curve', fontsize=14)
  ax.set_ylabel('TPR', fontsize=12)
  ax.set_xlabel('FPR', fontsize=12)
  ax.grid()
  ax.legend(['AUC=0.5','AUC={:.3}'.format(auc)])

def main():
  num_points = 1000
  stddev = 0.1
  d_red = NormalDist(num_points,0.4,stddev,'r')
  d_green = NormalDist(num_points,0.6,stddev,'g')

  fig, ax = plt.subplots(figsize=(10, 5))
  plot_pdfs(d_red,d_green,ax)
  annotate(ax)
  fig.savefig('normal_plot_annotate.pdf')

  fig, ax = plt.subplots(figsize=(5,5))
  roc_curve_plot(d_red, d_green, ax)
  fig.savefig('roc_curve.pdf')

  fig, ax = plt.subplots(1,2, figsize=(10,5))
  plot_pdfs(d_red, d_green, ax[0])
  roc_curve_plot(d_red, d_green, ax[1])
  fig.tight_layout()
  fig.savefig('normal_plot_roc.pdf')

  fig, ax = plt.subplots(3,2, figsize=(10,12))
  means_tuples = [(0.5,0.5),(0.4,0.6),(0.3,0.7)]
  for row, (d_red_mean, d_green_mean) in enumerate(means_tuples):
      d_red = NormalDist(num_points,d_red_mean,stddev,'r')
      d_green = NormalDist(num_points,d_green_mean,stddev,'g')
      plot_pdfs(d_red, d_green, ax[row,0])
      roc_curve_plot(d_red, d_green, ax[row,1])
  fig.tight_layout()
  fig.savefig('roc_curve_multi.pdf')

if __name__ == '__main__':
  main()
