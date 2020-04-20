#!/usr/bin/env python3
from numpy import linspace, zeros, exp
import matplotlib.pyplot as plt
from math import sqrt

def ode_FE(f, U_0, delta_t, numyears, other):
    N_t = int(round(numyears/delta_t))
    t = linspace(0, N_t*delta_t, N_t+1)
    u = zeros(N_t+1)
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + delta_t*f(u[n], t[n],other)
    return t, u

def population_growth_exp():
    '''Test case: u'=r*u, u(0)=100.'''
    def growth(u, t):
        return 0.1*u
    U_0 = 100
    delta_t = 0.083
    numyears = 20
    t, u = ode_FE(growth, U_0, delta_t, numyears, None)
    fig, ax = plt.subplots()
    ax.plot(t, u,t, U_0*exp(0.1*t))
    ax.legend(['numerical','exact'],loc='upper left')
    fig.savefig('exponential.pdf')

def population_growth_logistic():
    def growth(u, t, other):
      maxpop = 500
      tfactor = 0.01 * other * sqrt(t)
      return tfactor * (1 - u/maxpop) * u
    legends = list()
    U_0 = 100
    delta_t = 0.083
    numyears = 50
    fig, ax = plt.subplots()
    for growthrate in range(3,9):
      t, u = ode_FE(growth, U_0, delta_t, numyears,growthrate)
      ax.plot(t, u)
      legends.append('gr=0.0{}'.format(growthrate))
    ax.legend(legends,loc='upper left')
    ax.set_xlabel('time (years)')
    ax.set_ylabel('population')
    ax.set_title('logistic population (max 500) for varying growth rates (gr)')
    fig.savefig('logistic.pdf')

if __name__ == '__main__':
    population_growth_logistic()
