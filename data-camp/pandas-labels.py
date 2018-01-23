

Labeling your data
100xp
You can use the DataFrame attribute df.columns to view and assign new string labels to columns in a pandas DataFrame.

In this exercise, we have imported pandas as pd and defined a DataFrame df containing top Billboard hits from the 1980s (from Wikipedia). Each row has the year, artist, song name and the number of weeks at the top. However, this DataFrame has the column labels a, b, c, d. Your job is to use the df.columns attribute to re-assign descriptive column labels.

# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels


#no header row (will give numbers, then you can assign names)

sunspots = pd.read_csv(filepath, header=None)
header=1, header=2, header=3 #this tells pd how many header rows there are

#look at rows 10-19, all columns
sunspots.iloc[10:20, :]

col_names = ['year','month','day', 'dec_date','sunspots','definite']

sunspots = pd.read_csv(filepath, header=None, names=col_names)


#now for nans, which here are -1 and -1 with spaces in front

sunspots = pd.read_csv(filepath, header=None, names=col_names, na_values=' -1')

#Can also do different nans for different cols, just use dict



sunspots = pd.read_csv(filepath, header=None, names=col_names, na_values={'sunspots':[' -1'], 'month':['13']})

#for better date parsing, 
#he used this in the read_csv command to put together the separate year, month, and day values
parse_dates=[[0, 1, 2]]


sunspots = pd.read_csv(filepath, header=None, names=col_names, na_values={'sunspots':[' -1'], 'month':['13']}, parse_dates=[[0, 1, 2]])


#specify the index
sunspots.index=sunspots['year_month_day']
sunspots.index.name='date'




















