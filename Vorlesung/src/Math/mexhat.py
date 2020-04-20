import numpy as np

def mexhat_np(sigma, t):
    '''Computes Mexican hat shape using numpy, see
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet for
    equation (13 Dec 2011)'''
    c = 2.0 / np.sqrt(3 * sigma) * np.pi ** 0.25
    return c * (1 - t ** 2 / sigma ** 2) * \
           np.exp(-t ** 2 / (2 * sigma ** 2))
