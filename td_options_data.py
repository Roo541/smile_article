import td_data as td
import pandas as pd
import numpy as np
import datetime as dt
import black_scholes_calc as calc
import matplotlib
from matplotlib import pyplot as plt

a = td.td_data('USO')

want = {'date':[], 'ticker':[], 'bid':[], 'ask':[], 'underlying':[], 'strike':[], 'days_maturity':[], 'interest':[]}

for i in a['callExpDateMap'].keys():
    key = i
    print(key)
for i in a['callExpDateMap'][key].keys():
    want['date'].append(dt.datetime.now())
    want['ticker'].append(a['symbol'])
    want['bid'].append(a['callExpDateMap'][key][i][0]['bid'])
    want['ask'].append(a['callExpDateMap'][key][i][0]['ask'])
    want['underlying'].append(a['underlyingPrice'])
    want['strike'].append(float(i))
    want['days_maturity'].append(float(key[11:]))
    want['interest'].append(2.0)

df = pd.DataFrame(want)

#df.to_csv('intc.csv')

df['vol'] = [0.0]*len(df)

for i in range(len(df)):
    S = float(df['underlying'][i])
    k = float(df['strike'][i])
    t = float(df['days_maturity'][i]/365.0)
    r = 0.015
    c0 = float((df['bid'][i]+df['ask'][i])/2)
    vol = calc.iv(S, k, t, r, c0)
    df['vol'][i] = float(vol)
    #print(type(S), type(k), type(t), type(r), type(c0))

values = df.loc[df['vol'] > 0.0]
values = values.loc[values['vol'] < 1]

plt.figure()
plt.scatter(values['strike'][:], values['vol'][:])
plt.show()
#print(df)
