#!/usr/bin/env python

import numpy as np 
import pandas as pd 

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()


#Plot all columns together on one figure by calling df.plot(), and noting the vertical scaling problem.
#Plot all columns as subplots. To do so, you need to specify subplots=True inside .plot().
#Plot a single column of dew point data. To do this, define a column list containing a single column name 'Dew Point (deg F)', and call df[column_list1].plot().
#Plot two columns of data, 'Temperature (deg F)' and 'Dew Point (deg F)'. To do this, define a list containing those column names and pass it into df[], as df[column_list2].plot().