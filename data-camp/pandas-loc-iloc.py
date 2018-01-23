#Select rows
cars[0:2]
>>> cars[0:2]
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False


#loc and iloc
cars.loc['MOR']

>>> cars.loc['MOR']
cars_per_cap         70
country         Morocco
drives_right       True
Name: MOR, dtype: object

cars.loc[['MOR']]
>>> type(cars.loc[['MOR']])
<class 'pandas.core.frame.DataFrame'>

>>> type(cars.loc['MOR'])
<class 'pandas.core.series.Series'>


cars.loc[['MOR', 'US', 'IN']]
    cars_per_cap        country drives_right
MOR            76        Morocco         True
US            815  United States         True
IN             24          India        False

cars.loc[['MOR', 'US', 'IN'], ['country', 'cars_per_cap']]
           country  cars_per_cap
MOR        Morocco            76
US   United States           815
IN           India            24

cars.loc[:, ['country', 'cars_per_cap']]
gives all rows, 2 columns

iloc does number indexing for rows(ISH)

cars.iloc[:,[0,1]]

    cars_per_cap        country
US            815  United States
AUS           737      Australia
JAP           594          Japan
IN             24          India
RU            206         Russia
MOR            76        Morocco
EG             51          Egypt

>>> cars
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False
IN             18          India        False
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True
>>> for row in cars:
...     cars['cars_per_cap']=cars['cars_per_cap']+1
... 
>>> 
>>> cars
     cars_per_cap        country drives_right
US            812  United States         True
AUS           734      Australia        False
JAP           591          Japan        False
IN             21          India        False
RU            203         Russia         True
MOR            73        Morocco         True
EG             48          Egypt         True




#Their exercies
# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#loc and iloc (1)

#With loc and iloc you can do practically any data selection operation 
#on DataFrames you can think of. loc is label-based, 
#which means that you have to specify rows and columns 
#based on their row and column labels. iloc is integer index based, 
#so you have to specify rows and columns by their integer index 
#like you did in the previous exercise.

# Print out observation for Japan
cars.loc['JAP']
cars.iloc[2]

cars.loc[['JAP']]
cars.iloc[[2]]
# Print out observations for Australia and Egypt

cars.loc['AUS', 'EG']

# Print out drives_right value of Morocco
cars.loc['MOR','cars_per_cap']

cars.loc['MOR'],['cars_per_cap']
print(cars.loc[['MOR'],['cars_per_cap']])
# Print sub-DataFrame

cars.loc[['MOR','RU'],['country','drives_right']]
cars.iloc[[4,5],[1,2]]

# Print out drives_right column as Series
cars.loc[:,'drives_right']
cars.iloc[:,2]

# Print out drives_right column as DataFrame
cars.loc[[:,'drives_right']]
cars.iloc[[:,2]]

# Print out cars_per_cap and drives_right as DataFrame


cars.loc[:,['cars_per_cap','drives_right']]

cars.iloc[:,[1,2]]



