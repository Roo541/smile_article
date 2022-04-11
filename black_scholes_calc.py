from math import sqrt, exp, log, pi
from statistics import NormalDist

def d(sigma,S,k,r,t):
    d1 = 1/(sigma*sqrt(t)) * (log(S/k) + (r + sigma**2/2) * t)
    d2 = d1 - sigma * sqrt(t)
    return d1, d2 

def call_price(sigma, S, k, r, t, d1, d2):
    C = NormalDist(mu=0, sigma=1).cdf(d1) * S - NormalDist(mu=0, sigma=1).cdf(d2) * k * exp(-r * t)
    return C

def iv(S,k,t,r,c0):

    tol = 1e-3
    epsilon = 1

    count = 0
    max_iter = 1000

    vol = 0.99 

    while epsilon > tol:
        count += 1
        orig_vol = vol

        d1, d2 = d(vol, S, k, r, t)
        function_value = call_price(vol, S, k, r, t, d1, d2) - c0  

        vega = S * NormalDist(mu=0, sigma=1).pdf(d1) * sqrt(t)
        if vega != 0.0:
        
            vol = -function_value/ vega + vol

            epsilon = abs( (vol - orig_vol) / orig_vol )
        
        else:
            vol = 0.99

        if count > max_iter:
            break

    return vol


S = 48.01
k = 49.00
t = 5.0/365.0
r = 0.01
c0 = 0.34

a = iv(S,k,t,r,c0)
print(a)

