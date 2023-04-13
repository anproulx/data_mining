import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import csv
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(os.getcwd())

data = pd.read_csv('dataset_mood_smartphone.csv')

del data['Unnamed: 0']

for col in data['variable'].unique():
    newcol = data[data['variable'] == col]
    newcol = newcol.rename(columns={'value': col})
    data[col] = newcol[col]


d = {}
ids = data['id'].unique()
for id in ids:
    data_per_id = data.loc[(data['id'] == id)]

    ## Set timestamp to 24 hour
    data_per_id_time = data_per_id.set_index(['time'])
    data_per_id_time.index = pd.to_datetime(data_per_id_time.index)

    # Get the values for each variable
    # Mean of in range values
    new_data = pd.DataFrame()
    set_time = False
    for col in data['variable'].unique():

        if col in ['mood', 'circumplex.arousal', 'circumplex.valence']:
            col_agg = data_per_id_time.resample('24H').agg({col: 'mean'})
        else:
            col_agg = data_per_id_time.resample('24H').agg({col: 'sum'})

        if set_time == False:
            new_data['id'] = [id]*len(col_agg.index.values.flatten())
            new_data['time'] = col_agg.index

            set_time = True

        new_data[col] = col_agg.values.flatten()

    d["user{0}".format(id)] = new_data


### Plots of mood
for id in d:
    id_ex = d[id]

    first = id_ex['mood'].first_valid_index()
    last = id_ex['mood'].last_valid_index()

    print(first, last)

    # Delete all rows before first and after last:
    id_ex = id_ex.drop(id_ex.index[last:])
    id_ex = id_ex.drop(id_ex.index[:first])
    id_ex = id_ex.reset_index(drop=True)

    for col in id_ex.columns:
       # print nr of missing values
         print(col, id_ex[col].isna().sum())

    
# Plot time series of mood
    plt.figure(figsize=(15, 5))
    plt.plot(id_ex['time'], id_ex['mood'])
    plt.title('Mood over time')
    plt.xlabel('Time')
    plt.ylabel('Mood')
    plt.show()

    