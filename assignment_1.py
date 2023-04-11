import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(os.getcwd())

data = pd.read_csv('dataset_mood_smartphone.csv')

# Print all values of variable 'appCat.builtin':
print(data[data['variable'] == 'appCat.builtin']['value'].unique())


# Print total length of data set:
print('Total length of dataset: ', data.shape[0])

# Print number of unique ids:
print('number of unique ids:', len(data['id'].unique()))

data2 = data[data['variable'] == 'mood']



# Print number of instances for each unique id:
print('Number of instances for each unique id:')

for id in data['id'].unique():
    print(id, data2[data2['id'] == id].shape[0])


allvar = data['variable'].unique()
selectedvar = np.delete(allvar, [1,2,5,6])




df['mood'] = data_mood_only['mood']
df['circumplex.arousal'] = circumplex_arousal_only['circumplex.arousal']
df['circumplex.valence'] = circumplex_valence_only['circumplex.valence']
df['activity'] = activity['activity']
df['screen'] = screen['screen']
df['sms'] = sms['sms']
df['appCat.builtin'] = appCat_builtin['appCat.builtin']
df['appCat.communication'] = appCat_communication['appCat.communication']
df['appCat.entertainment'] = appCat_entertainment['appCat.entertainment']
df['appCat.finance'] = appCat_finance['appCat.finance']
df['appCat.game'] = appCat_game['appCat.game']
df['appCat.office'] = appCat_office['appCat.office']
df['appCat.other'] = appCat_other['appCat.other']
df['appCat.social'] = appCat_social['appCat.social']
df['appCat.travel'] = appCat_travel['appCat.travel']
df['appCat.unknown'] = appCat_unknown['appCat.unknown']
df['appCat.utilities'] = appCat_utilities['appCat.utilities']
df['appCat.weather'] = appCat_weather['appCat.weather']
df




plt.subplot(4, 3, 1)
plt.scatter(range(len(df['appCat.game'])), df['appCat.game'])
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.title('game')
plt.plot

plt.subplot(4, 3, 2)
plt.scatter(range(len(df['appCat.travel'])), df['appCat.travel'])
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.title('travel')
plt.plot

plt.subplot(4, 3, 3)
plt.scatter(range(len(df['appCat.builtin'])), df['appCat.builtin'])
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.title('builtin')
plt.plot

plt.subplot(4, 3, 4)
plt.scatter(range(len(df['appCat.communication'])), df['appCat.communication'])
plt.title('communication')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 5)
plt.scatter(range(len(df['appCat.entertainment'])), df['appCat.communication'])
plt.title('entertainment')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 6)
plt.scatter(range(len(df['appCat.office'])), df['appCat.communication'])
plt.title('office')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 7)
plt.scatter(range(len(df['appCat.other'])), df['appCat.other'])
plt.title('other')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 8)
plt.scatter(range(len(df['appCat.weather'])), df['appCat.weather'])
plt.title('weather')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 9)
plt.scatter(range(len(df['appCat.utilities'])), df['appCat.utilities'])
plt.title('utilities')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 10)
plt.scatter(range(len(df['appCat.social'])), df['appCat.social'])
plt.title('social')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3,11)
plt.scatter(range(len(df['appCat.unknown'])), df['appCat.unknown'])
plt.title('unknown')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(4, 3, 12)
plt.scatter(range(len(df['appCat.finance'])), df['appCat.finance'])
plt.title('finance')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.show






plt.subplot(3, 2, 1)
plt.scatter(range(len(df['activity'])), df['activity'])
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.title('activity')
plt.plot

plt.subplot(3, 2, 2)
plt.scatter(range(len(df['screen'])), df['screen'])
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.title('screen')
plt.plot

plt.subplot(3, 2, 3)
plt.scatter(range(len(df['sms'])), df['sms'])
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.title('sms')
plt.plot

plt.subplot(3, 2, 4)
plt.scatter(range(len(df['circumplex.arousal'])), df['circumplex.arousal'])
plt.title('circumplex.arousal')
ax = plt.gca()
ax.get_xaxis().set_visible(False)


plt.subplot(3, 2, 5)
plt.scatter(range(len(df['circumplex.valence'])), df['circumplex.valence'])
plt.title('circumplex.valence')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot

plt.subplot(3, 2, 6)
plt.scatter(range(len(df['mood'])), df['mood'])
plt.title('mood')
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.plot





d = {}
ids = df['id'].unique()
for id in ids:
    data_per_id = df.loc[(df['id'] == id)]
    ## Set timestamp to 24 hour
    data_per_id_time = data_per_id.set_index(['time'])
    data_per_id_time.index = pd.to_datetime(data_per_id_time.index)
    # Get the values for each variable
    # Mean of in range values
    mood_agg = data_per_id_time.resample('24H').agg({'mood': 'mean'})
    arousal_agg = data_per_id_time.resample('24H').agg({'circumplex.arousal': 'mean'})
    valence_agg = data_per_id_time.resample('24H').agg({'circumplex.valence': 'mean'})
    ## Sum duration of each activity 
    activity_agg = data_per_id_time.resample('24H').agg({'activity': 'sum'})
    screen_agg = data_per_id_time.resample('24H').agg({'screen': 'sum'})
    sms_agg = data_per_id_time.resample('24H').agg({'sms': 'sum'})
    builtin_agg = data_per_id_time.resample('24H').agg({'appCat.builtin': 'sum'})
    communication_agg = data_per_id_time.resample('24H').agg({'appCat.communication': 'sum'})
    entertainment_agg = data_per_id_time.resample('24H').agg({'appCat.entertainment': 'sum'})
    finance_agg = data_per_id_time.resample('24H').agg({'appCat.finance': 'sum'})
    game_agg = data_per_id_time.resample('24H').agg({'appCat.game': 'sum'})
    office_agg = data_per_id_time.resample('24H').agg({'appCat.office': 'sum'})
    other_agg = data_per_id_time.resample('24H').agg({'appCat.other': 'sum'})
    social_agg = data_per_id_time.resample('24H').agg({'appCat.social': 'sum'})
    travel_agg = data_per_id_time.resample('24H').agg({'appCat.travel': 'sum'})
    unknown_agg = data_per_id_time.resample('24H').agg({'appCat.unknown': 'sum'})
    utilities_agg = data_per_id_time.resample('24H').agg({'appCat.utilities': 'sum'})
    weather_agg = data_per_id_time.resample('24H').agg({'appCat.weather': 'sum'})
    # create dataframe for each user!
    new_data = pd.DataFrame()
    new_data['id'] = [id]*len(mood_agg.index.values.flatten())
    new_data['time'] = mood_agg.index
    new_data['mood'] = mood_agg.values.flatten()
    new_data['circumplex.arousal'] = arousal_agg.values.flatten()
    new_data['circumplex.valence'] = valence_agg.values.flatten()
    new_data['activity'] = activity_agg.values.flatten()
    new_data['screen'] = screen_agg.values.flatten()
    new_data['sms'] = sms_agg.values.flatten()
    new_data['appCat.builtin'] = builtin_agg.values.flatten()
    new_data['appCat.communication'] = communication_agg.values.flatten()
    new_data['appCat.entertainment'] = entertainment_agg.values.flatten()
    new_data['appCat.finance'] = finance_agg.values.flatten()
    new_data['appCat.game'] = game_agg.values.flatten()
    new_data['appCat.office'] = office_agg.values.flatten()
    new_data['appCat.other'] = other_agg.values.flatten()
    new_data['appCat.social'] = social_agg.values.flatten()
    new_data['appCat.travel'] = travel_agg.values.flatten()
    new_data['appCat.unknown'] = unknown_agg.values.flatten()
    new_data['appCat.utilities'] = utilities_agg.values.flatten()
    new_data['appCat.weather'] = weather_agg.values.flatten()
    ##
    d["user{0}".format(id)] = new_data






# for col in selectedvar:
#     print(col)
#     values = data[data['variable'] == col]

#     plt.boxplot(np.log(values['value']))
#     plt.title(col)
#     plt.show()


# for col in data.columns:
#     print('------------------------')
#     print('Column name: ', col)
#     print(data[col].unique())


# # Print number of instances with id == 'AS14.01':
# print(data[data['id'] == 'AS14.01'].shape[0])







# # Print minimum, maximum, mean, and standard deviation of 'variable' column:
# for var in data['variable'].unique():
#     print(var)
#     newd = data[data['variable'] == var]
#     min = 'Min: ', newd['value'].min()
#     max = 'Max: ', newd['value'].max()
#     mean = 'Mean: ', newd['value'].mean()
#     std = 'Std: ', newd['value'].std()

#     # Put these values in a new data frame, for each variable:
#     print(pd.DataFrame([min, max, mean, std], columns=[var]))
    



