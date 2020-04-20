#!/usr/bin/env python3

import numpy as np

class Quarter:
  def __init__(self,origin,divisor):
    self._number = 0  # Quarter number (0,1,2,3)
    self._center = [origin[0],origin[1]]
    assert divisor >= 1.0
    self._multiplier = 1.0 - 1.0/divisor
  def center(self):
    return self._center[0], self._center[1]
  def number(self):
    return self._number
  def next(self,radius):
    distance = radius * self._multiplier
    distance_values = [distance,distance,-distance,-distance] 
    self._center[self._number % 2] += distance_values[self._number]  # self._number % 2 : update x or y ?
    self._number = (self._number + 1) % 4  # nach 3 Quatern ist man wider beim ersten

def num_points_get(density,radius):
                                     #--- KreisUmfang --#
  num_points = int(np.ceil(density * radius * 0.5 * np.pi))
  return max(num_points,20)

def total_points_get(radius,divisor,num_quarters,density):
  total_points = 0
  for _ in range(num_quarters):
    total_points += num_points_get(density,radius)
    radius /= divisor
  return total_points

def quarter_circle_add(x_vec,y_vec,offset,center,start_angle,end_angle,radius,
                       num_points):
  angles = np.linspace(np.radians(start_angle),np.radians(end_angle),
                       num=num_points)
  x_vec[offset:offset+num_points] \
    = (lambda a: center[0] + radius * np.cos(a))(angles)
  y_vec[offset:offset+num_points] \
    = (lambda a: center[1] + radius * np.sin(a))(angles)

def spiral_coords(origin,radius,divisor,num_quarters,density):
  angle_pairs = [(270,360),(0,90),(90,180),(180,270)]
  quarter = Quarter(origin,divisor)
  total_points = total_points_get(radius,divisor,num_quarters,density)
  x_vec = np.zeros((total_points,))
  y_vec = np.zeros((total_points,))
  offset = 0
  for q in range(num_quarters):
    number = quarter.number()
    num_points = num_points_get(density,radius)
    start_angle, end_angle = angle_pairs[number]
    quarter_circle_add(x_vec,y_vec,offset,quarter.center(),start_angle,
                       end_angle,radius,num_points)
    quarter.next(radius)
    radius /= divisor
    offset += num_points
  return x_vec, y_vec

if __name__ == '__main__':
  import argparse
  from math import sqrt
  def parse_arguments():
    golden_ratio = (1 + sqrt(5))/2
    default_divisor = golden_ratio
    default_start_radius = 3.0
    default_quarters = 10
    default_density = 20
    p = argparse.ArgumentParser(description='output coordinates of a spiral')
    p.add_argument('-s','--start_radius',metavar='<float>',type=float,
                   default=default_start_radius,
                   help=('specify initial radius, default {}'
                          .format(default_start_radius)))
    p.add_argument('-q','--quarters',metavar='<int>',type=int,
                   default=default_quarters,
                   help=('specify number of quarters for which coordinates '
                         'are created, default: {}'.format(default_quarters)))
    p.add_argument('-d','--divisor',metavar='<float>',type=float,
                   default=default_divisor,
                   help=('specify divisor for computing next radius from '
                         'current radius, default is golden ratio {:.5}')
                         .format(golden_ratio))
    p.add_argument('--density',metavar='<int>',type=int,
                   default=default_density,
                   help=(('specify density of points on quarter circle:'
                          'default is {}').format(default_density)))
    return p.parse_args()
  def main():
    args = parse_arguments()
    origin = (0,0)
    x_vec, y_vec = spiral_coords(origin,args.start_radius,args.divisor,
                                 args.quarters,args.density)
    lines = ['#x\ty']
    for x,y in zip(x_vec,y_vec):
      lines.append('{:.5f}\t{:.5f}'.format(x,y))
    print('\n'.join(lines))
  main()
