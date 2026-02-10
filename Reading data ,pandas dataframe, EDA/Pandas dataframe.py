                               ########## Toyota datasheet


import os
import pandas as pd
import numpy as np
cars_csv=pd.read_csv('/Users/shekhar55003gmail.com/Desktop/Data Science/Python for Data Science/Toyota.csv')  ## give path name, not file
print(cars_csv)
cars_csv=pd.read_csv('/Users/shekhar55003gmail.com/Desktop/Data Science/Python for Data Science/Toyota.csv',index_col=0)
print(cars_csv)

### create copy of orginal data
## using shallow copy function .copy(deep=false) and deep copy using function .copy(deep=true)

## to get row labels of the data frame using function .index
print(cars_csv.index)

## to get row labels of the data frame using function .columns
print(cars_csv.columns)

## to get sixe of the data frame using function .size
print(cars_csv.size)

## to get shape of the data frame using function .shape
print(cars_csv.size)


##### indexing and selecting data
# the head function give the first n rows from data using .head([n])
print(cars_csv.head(4))

# the tail function give last n rows from data using .tail()
print(cars_csv.tail(12))

## to ascess group of rows and column using .loc[] function
print(cars_csv.loc[:, 'FuelType'])