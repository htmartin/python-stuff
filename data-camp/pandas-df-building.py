#Dictionary to DataFrame (1)

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names, 'left_or_right':dr, 'cars_per':cpc}

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Print cars
>>> cars
   cars_per        country left_or_right
0       809  United States          True
1       731      Australia         False
2       588          Japan         False
3        18          India         False
4       200         Russia          True
5        70        Morocco          True
6        45          Egypt          True



#Dictionary to DataFrame (2)

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars

cars.index=row_labels

# Print cars again

#CSV to DataFrame (1)

# Import pandas as pd
import pandas as pd


# Import the cars.csv data: cars

cars = pd.read_csv('cars.csv')
# Print out cars

print(cars)

#CSV to DataFrame (2)

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)

>>> cars['country']
US     United States
AUS        Australia
JAP            Japan
IN             India
RU            Russia
MOR          Morocco
EG             Egypt
Name: country, dtype: object

cars['cars_per_cap']
>>> cars['cars_per_cap']
US     809
AUS    731
JAP    588
IN      18
RU     200
MOR     70
EG      45
Name: cars_per_cap, dtype: int64

##How to keep a column as a dataframe object
>>> type(cars)
<class 'pandas.core.frame.DataFrame'>

>>> type(cars['cars_per_cap'])
<class 'pandas.core.series.Series'>


>>> type(cars[['cars_per_cap']])
<class 'pandas.core.frame.DataFrame'>



#Delimiters, headers, and extensions

Not all data files are clean and tidy. 
Pandas provides methods for reading those not-so-perfect data files 
that you encounter far too often.

In this exercise, you have monthly stock data for four companies 
downloaded from Yahoo Finance. 
The data is stored as one row for each company and 
each column is the end-of-month closing price. 
The file name is given to you in the variable file_messy.

In addition, this file has three aspects that may cause trouble for 
lesser tools: multiple header lines, 
comment records (rows) interleaved throughout the data rows, 
and tab delimiters instead of commas.

Your job is to use pandas to read the data from this problematic 
file_messy using non-default input options with read_csv() 
so as to tidy up the mess at read time. 
Then, write the cleaned up data to a CSV file 
with the variable file_clean that has been prepared for you, 
as you might do in a real data workflow.

You can learn about the option input parameters needed by using help() 
on the pandas function pd.read_csv().

# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)



Use pd.read_csv() without using any keyword arguments to read file_messy into a pandas DataFrame df1.
Use .head() to print the first 5 rows of df1 and see how messy it is. Do this in the IPython Shell first so you can see how modifying read_csv() can clean up this mess.
Using the keyword arguments delimiter=' ', header=3 and comment='#', use pd.read_csv() again to read file_messy into a new DataFrame df2.
Print the output of df2.head() to verify the file was read correctly.
Use the DataFrame method .to_csv() to save the DataFrame df2 to the variable file_clean. Be sure to specify index=False.
Use the DataFrame method .to_excel() to save the DataFrame df2 to the file 'file_clean.xlsx'. Again, remember to specify index=False.

















