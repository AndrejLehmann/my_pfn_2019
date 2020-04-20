#!/usr/bin/env python3

import numpy as np
from numba import jit

@jit
def mandelbrot_iter(c,nmax):
  z = c
  for n in range(nmax):
    if abs(z) > 2:
      return n
    z = z * z + c
  return nmax

def mandelbrot_series(c,nmax):
  z = c
  for i in range(nmax):
    yield i, z
    if abs(z) > 2:
      return
    z = z * z + c

@jit
def mandelbrot_set(bw,rmin,rmax,imin,imax,imgwidth,imgheight,nmax):
  repart = np.linspace(rmin, rmax, imgwidth)
  impart = np.linspace(imin, imax, imgheight)
  matrix = np.empty((imgwidth,imgheight),dtype=int)
  for i in range(imgwidth):
    for j in range(imgheight):
      c = repart[i] + impart[j] * 1j# imaginary const => complex n.
      if bw:
        matrix[i,j] = mandelbrot_iter(c,nmax) == nmax
      else: # colored
        miter = mandelbrot_iter(c,nmax)
        matrix[i,j] = 0 if miter == nmax else (miter + 1)
  return matrix

from matplotlib import pyplot as plt
plt.switch_backend('agg') # disable X-server
# needed on Linux when running program via remote ssh login

def mandelbrot_image(bw,rmin,rmax,imin,imax,nmax,width,height):
  dpi = 72 # dots per inch
  imgwidth = dpi * width
  imgheight = dpi * height
  matrix = mandelbrot_set(bw,rmin,rmax,imin,imax,
                          imgwidth,imgheight,nmax)
  this_cmap = 'gist_yarg' if bw else 'jet'
  fig, ax = plt.subplots()
  ax.matshow(matrix,cmap=this_cmap)
  fig.savefig('mandelbrot-{}.png'.format('bw' if bw else 'color'))

mandelbrot_image(False,-2.0,0.5,-1.25,1.25,256,10,10)

nmax = 8
for c in [-1.5 + 1j,-1 + 0 * 1j]:
  for i, z in mandelbrot_series(c,nmax):
    print('{}\t{}\t{:.2f}'.format(i+1,z,abs(z)))
