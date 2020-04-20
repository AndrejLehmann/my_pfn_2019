import argparse

def temp_parse_arguments(with_hsmth=True,with_heat=True,with_lag=True,
                         with_acor=True):
  p = argparse.ArgumentParser(description='plot time series')
  plotgroup = p.add_mutually_exclusive_group(required=True)
  plotgroup.add_argument('--std',action='store_true',default=False,
                         help='standard plot')
  plotgroup.add_argument('--scatter',action='store_true',default=False,
                         help='show scatter plot')
  plotgroup.add_argument('--hist',action='store_true',default=False,
                         help='show histograms black dots for plot')
  if with_hsmth:
    plotgroup.add_argument('--hsmth',action='store_true',default=False,
                           help='show smoothed histogram')
  plotgroup.add_argument('--boxp',action='store_true',default=False,
                         help='show boxplots for each year')
  plotgroup.add_argument('--violinp',action='store_true',default=False,
                         help='show violinplot for each year')
  plotgroup.add_argument('--ysub',action='store_true',default=False,
                         help='show subplots for each year')
  if with_heat:
    plotgroup.add_argument('--heat',action='store_true',default=False,
                           help='show heatmap of distribution of temperatures')
  if with_lag:
    plotgroup.add_argument('--lag',action='store_true',default=False,
                           help='show lag plot of temperatures')
  if with_acor:
    plotgroup.add_argument('--acor',action='store_true',default=False,
                           help='show auto correlation plot of temperatures')
  plotgroup.add_argument('--year',type=int,default=None,
                         help='show boxplots for month of the given year')
  return p.parse_args()
