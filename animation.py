import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd 
from datetime import time
#from scipy.optimize import curve_fit

df = pd.read_csv('3_29_to_4_1.csv')
df_2 = pd.read_csv('4_4_to_4_8_new.csv')

fig, ax = plt.subplots()
fig_2, ax_2 = plt.subplots()

def func(x, a, b):
    return a*np.exp(x*b)

def animation_frame(i):
    dh = df.loc[df['date'] == i]
    x_data = dh['pct_away']
    y_data = dh['vol']
    #popt, pcuv = curve_fit(func, x_data, y_data)
    #xFit = np.arange(-5,5,0.01)
    plt.clf()
    plt.scatter(x_data,y_data, label= i)
    #plt.plot(xFit, func(xFit, *popt), 'r', label = 'y= a*exp(b*x)'+ str(popt))
    plt.title('SPY implied volatility tracking')
    plt.xlabel('pct from strike (%)')
    plt.ylabel('implied volatility')
    plt.legend()

    return 
def animation_frame_2(i):
    dh = df_2.loc[df_2['date'] == i]
    x_data = dh['pct_away']
    y_data = dh['vol']
    #popt, pcuv = curve_fit(func, x_data, y_data)
    #xFit = np.arange(-5,5,0.01)
    plt.clf()
    plt.scatter(x_data,y_data, label= i)
    #plt.plot(xFit, func(xFit, *popt), 'r', label = 'y= a*exp(b*x)'+ str(popt))
    plt.title('SPY implied volatility tracking')
    plt.xlabel('pct from strike')
    plt.ylabel('implied volatility')
    plt.legend()

    return 

dates = df['date']
dates = dates.drop_duplicates()

wk_2_dates = df_2['date']
wk_2_dates = wk_2_dates.drop_duplicates()

#animation = FuncAnimation(fig, func=animation_frame, frames = dates, interval=1)
animation_2 = FuncAnimation(fig_2, func=animation_frame_2, frames = wk_2_dates, interval=1)

animation_2.save('smile_curve.gif')
plt.show()

