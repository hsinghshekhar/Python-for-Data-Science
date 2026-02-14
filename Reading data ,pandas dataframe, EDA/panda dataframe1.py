                ##### checking data types

## for checking type of data using .dtypes function
import pandas as pd
toto_csv=pd.read_csv('/Users/shekhar55003gmail.com/Desktop/Data Science/Python for Data Science/Toyota.csv')
print(toto_csv)
print(toto_csv.dtypes) 

## for summary of a dataframe using function .info()
print(toto_csv.info())

## for get unique element in column using function numpy.unique() from numpy library
import numpy as np
print(np.unique(toto_csv['Age']))    # this is for float64

print(np.unique(toto_csv['KM']))

import pandas as pd
print(pd.unique(toto_csv['FuelType']))  # this is for string 

print(np.unique(toto_csv['Doors']))  # Doors is variable

## to replace string to number and vice versa using function .replace()

print(toto_csv.replace('three',3,inplace=True))
print(toto_csv.replace('four',4,inplace=True))
print(toto_csv.replace('five',5,inplace=True))

## To detect missing value in each column of dataframe using function .isnull.sum()

print(toto_csv.isnull().sum()) 
