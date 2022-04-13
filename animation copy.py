import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd 
from datetime import time

df = pd.read_csv('4_4_to_4_8_new.csv')
df = df[15561:]
fig, ax = plt.subplots()

def animation_frame(i):
    dh = df.loc[df['date'] == i]
    x_data = dh['pct_away']
    y_data = dh['vol']
    plt.clf()
    plt.scatter(x_data,y_data, label= i)
    plt.title('SPY implied volatility tracking')
    plt.xlabel('(%) from strike')
    plt.ylabel('implied volatility')
    plt.legend()

    return 
dates = df['date']
dates = dates.drop_duplicates()

animation = FuncAnimation(fig, func=animation_frame, frames = dates, interval=10)
animation.save('smile_curve.gif')
plt.show()

