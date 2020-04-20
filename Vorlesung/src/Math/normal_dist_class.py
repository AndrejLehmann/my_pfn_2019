import numpy as np
import matplotlib.pyplot as plt
from normal_pdf import normalProbabilityDensity

class NormalDist:
  def __init__(self,num_points,mean,stddev,color):
    self._mean = mean
    self._stddev = stddev
    self._color = color
    self._x_vec = np.linspace(0, 1, num=num_points)
    self._y_vec = normalProbabilityDensity(mean,stddev,self._x_vec)
    self._tail = [None] * num_points
    tail_sum = 0
    for idx in range(num_points-1,-1,-1):
      tail_sum += self._y_vec[idx]
      self._tail[idx] = tail_sum
  def domain(self):
    return self._x_vec
  def __getitem__(self,idx):
    assert idx >= 0 and idx < len(self._y_vec)
    return self._y_vec[idx]
  def tail(self):
    return iter(self._tail)
  def sum(self):
    return np.sum(self._y_vec)
  def plot(self,ax):
    ax.plot(self._x_vec, self._y_vec,self._color,alpha=0.5,
            label='$\mu={}, \sigma={}$'.format(self._mean,self._stddev))
    ax.legend()

