import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

d = pd.read_csv('output.csv')


for id in d:
    id_ex = d[id]

    print(id)

    # # Plot time series of mood
    # plt.figure(figsize=(15, 5))
    # plt.plot(id_ex['time'], id_ex['mood'])
    # plt.title('Mood over time')
    # plt.xlabel('Time')
    # plt.ylabel('Mood')
    # plt.show()

    
