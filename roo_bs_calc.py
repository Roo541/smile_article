import numpy as np
from statistics import NormalDist

def iv_calc(s,k,t,r,C):
    vol = np.arange(0,1,0.001)
    tolerance = 0.001
    for i in vol:
        d1 = (np.log(s/k) + ((r + (i**2)/2))*t)/(i*np.sqrt(t))
        N_1 = NormalDist(mu=0, sigma=1).cdf(d1)
        d2 = d1 - i*np.sqrt(t)
        N_2 = NormalDist(mu=0, sigma=1).cdf(d2)
        call_price = s*N_1 - k*(np.exp(-r*t))*N_2

        if (C - C*tolerance) <= call_price and (C + C*tolerance) >= call_price:
            iv = i
            break
        else:
            pass

    return iv



