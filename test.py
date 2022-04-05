import pandas as pd  
import numpy as np 
import math 

def MyDist(d):
    dx = 0.01
    x = np.arange(-1, d, dx)
    y = []
    sigma = 1.0
    summation = 0.158
    for i in x:
        value = (1/(sigma*np.sqrt(2*np.pi)))*(np.exp((-0.5)*(i/sigma)**2))
        summation += value*dx
        y.append(summation)
    
    N = y[-1:]
    return N[0]

def call(s, k, r, t, C):
    d1 = (np.log(s/k) + ((r + (vol**2)/2))*t)/(vol*np.sqrt(t))
    N_1 = MyDist(d1)
    d2 = d1 - vol*np.sqrt(t)
    N_2 = MyDist(d2)

    call_price = s*N_1 - k*(np.exp(-r*t))*N_2


    return call_price

s = 48.67
k = 50.0
r = 0.01
t = 9/365.0
vol = 0.2471
C = 0.29

hello = call(s,k,r,t,C)
print('call price', hello)