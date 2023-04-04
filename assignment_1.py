import os
import pandas as pd

print(os.getcwd())

data = pd.read_csv('dataset_mood_smartphone.csv')
print(data.head())

for col in data.columns:
    print('------------------------')
    print('Column name: ', col)
    print(data[col].unique())


# Print number of instances with id == 'AS14.01':
print(data[data['id'] == 'AS14.01'].shape[0])

# Print total length of data set:
print(data.shape[0])

# Print number of unique ids:
print(len(data['id'].unique()))

# Print number of instances for each unique id:
for id in data['id'].unique():
    print(id, data[data['id'] == id].shape[0])


# Print minimum, maximum, mean, and standard deviation of 'variable' column:
for var in data['variable'].unique():
    print(var)
    newd = data[data['variable'] == var]
    min = 'Min: ', newd['value'].min()
    max = 'Max: ', newd['value'].max()
    mean = 'Mean: ', newd['value'].mean()
    std = 'Std: ', newd['value'].std()

    # Put these values in a new data frame, for each variable:
    print(pd.DataFrame([min, max, mean, std], columns=[var]))
    



