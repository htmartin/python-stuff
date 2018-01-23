Drop an observation (row)

name	reports	year
Cochice	Jason	4	2012
Pima	Molly	24	2012
Santa Cruz	Tina	31	2013
Maricopa	Jake	2	2014
Yuma	Amy	3	2014

df.drop(['Cochice', 'Pima'])

name	reports	year
Santa Cruz	Tina	31	2013
Maricopa	Jake	2	2014
Yuma	Amy	3	2014


Drop a variable (column)

Note: axis=1 denotes that we are referring to a column, not a row

df.drop('reports', axis=1)


Drop a row if it contains a certain value (in this case, "Tina")

Specifically: Create a new dataframe called df that includes all rows 
where the value of a cell in the name column does not equal "Tina"

df[df.name != 'Tina']

Drop a row by row number (in this case, row 3)

Note that Pandas uses zero based numbering, so 0 is the first row, 1 is the second row, etc.

df.drop(df.index[2])

name	reports	year
Cochice	Jason	4	2012
Pima	Molly	24	2012
Maricopa	Jake	2	2014
Yuma	Amy	3	2014
can be extended to dropping a range

df.drop(df.index[[2,3]])

name	reports	year
Cochice	Jason	4	2012
Pima	Molly	24	2012
Yuma	Amy	3	2014
or dropping relative to the end of the DF.

df.drop(df.index[-2])

name	reports	year
Cochice	Jason	4	2012
Pima	Molly	24	2012
Santa Cruz	Tina	31	2013
Yuma	Amy	3	2014

you can select ranges relative to the top or drop relative to the bottom of the DF as well.

df[:3] #keep top 3

name	reports	year
Cochice	Jason	4	2012
Pima	Molly	24	2012
Santa Cruz	Tina	31	2013

df[:-3] #drop bottom 3 

name	reports	year
Cochice	Jason	4	2012
Pima	Molly	24	2012
