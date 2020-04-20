import numpy as np

def normalProbabilityDensity(mean,stddev,x):
  stddev_sq = stddev ** 2
  const = 1.0 / np.sqrt(2 * np.pi * stddev_sq)
  return const * np.exp(-((x - mean) ** 2)/(2.0 * stddev_sq))
