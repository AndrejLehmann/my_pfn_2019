import math
def curvedM(x):
  return 2.0 + math.sin(5.0 * x) + math.cos(10.0 * x) + 0.1 * x * x

def velocity(t):
  return 3 * t * t * (math.pow(math.e,t * t * t))

def velocity_anti_derivative(t):
  return math.pow(math.e,t * t * t)

import numpy as np
def np_velocity(t):
  return 3 * t * t * (np.power(np.e,t * t * t))
