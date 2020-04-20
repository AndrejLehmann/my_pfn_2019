#!/usr/bin/env python3
import matplotlib.pyplot as plt
from mexhat import mexhat_np
import numpy as np

x_vec = np.linspace(-7,7,500)
sigma_list = [0.8,0.9,1,1.5,2]
fig, ax = plt.subplots()
ax.set_title('mexican hat function for varying $\sigma$')
for sigma in sigma_list:
  def mexhat_sigma(t):
    return mexhat_np(sigma,t)
  y_vec = mexhat_sigma(x_vec)
  ax.plot(x_vec,y_vec)

ax.legend(['$\sigma={}$'.format(sigma) for sigma in sigma_list])
fig.savefig('mexican_hat.pdf')
