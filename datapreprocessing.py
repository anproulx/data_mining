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

# some feature engineering

for id in d.keys():

  # drop nas for mood target
  d[id] = d[id].dropna(subset = ['mood'])
  
  # add column #n entries for that each id
  n_days_id = len(d[id])
  list_days = [i for i in range(n_days_id)]
  d[id]['n_days_id'] = list_days
  
  # add target mood
  d[id]['target_mood_plus1'] = d[id]['mood'].shift(-1) 
  # d[id]['target_mood_plus2'] = d[id]['mood'].shift(-2)
    
  # day difference with previous obs
  d[id]['day_shift'] = d[id]['days'].shift(-1)
  
  # deal with prolonged period of missing
  d[id]['day_diff'] = d[id]['day_shift']- d[id]['days']
  
  # get time elapsed
  start = pd.DatetimeIndex(d[id]['time'])[0]
  d[id]['time_elapsed'] = pd.DatetimeIndex(d[id]['time']) - start
  
  # dropnans
  d[id] = d[id].dropna(subset = ['target_mood_plus1',	'target_mood_plus2', 'day_shift',	'day_diff'])
  
  # if difference day interval t vs t+1 is over 4, drop
  d[id] = d[id][d[id]['day_diff'] < 4]

# some more features if needed

# add day & month as binary variable
all_data['month'] = pd.DatetimeIndex(all_data['time']).month # needs to be hot encoded
all_data['day'] = pd.DatetimeIndex(all_data['time']).day 

# add seasons as categorical variable
season = {2 : 'winter', 3 : 'spring', 4 : 'spring', 5 :'summer', 6: 'summer'}
all_data['season'] = all_data.month
all_data['season'] = all_data['season'].replace(season) # to be hot encoded

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

    
