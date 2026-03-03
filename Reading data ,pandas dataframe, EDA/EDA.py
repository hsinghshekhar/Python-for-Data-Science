                 ### Exploratory Data Analysis #####

import os
import pandas as pd
car_data=pd.read_csv('/Users/shekhar55003gmail.com/Desktop/Data Science/Python for Data Science/Toyota.csv')
print(car_data)
car_data1=pd.read_csv('/Users/shekhar55003gmail.com/Desktop/Data Science/Python for Data Science/Toyota.csv', index_col=0)
print(car_data1)

#### copy of original data

car_data2=car_data.copy()

###### Frequency table
name=pd.crosstab(index=car_data2['FuelType'], columns='count',dropna=True)
print(name)

### Two way table
# using pd.crosstab()

## to look the frequency distribution of gearbox types with respect to different fuel types of cars

name2=pd.crosstab(index=car_data2['Automatic'], columns=car_data2['FuelType'],dropna=True)
print(name2)

##### Two way- Joint probability
## Joint probability is the likelihood(the chance of something happening) of the two independent events hapenning at the same time

name3=pd.crosstab(index=car_data2['Automatic'], columns=car_data2['FuelType'],normalize=True,dropna=True)
print(name3)

#### Marginal Probability- is the probalility of the occurrence of single event

name4=pd.crosstab(index=car_data2['Automatic'], columns=car_data2['FuelType'], margins=True ,normalize=True,dropna=True)
print(name4) 


##### Conditional Probability- is the probability of the event A, given that another event B has already occured

name5=pd.crosstab(index=car_data2['Automatic'], columns=car_data2['FuelType'],margins=True,normalize='index',dropna=True) # index use for row sum equal to 1
print(name5) 

## use columns instead of index for column sum equal to 1

name6=pd.crosstab(index=car_data2['Automatic'], columns=car_data2['FuelType'],margins=True,normalize='columns',dropna=True) 
print(name6)


                              ##### Correlation ######
                              
# Correlation in statistics measures the strength and direction of the linear relationship between two variables, typically using a coefficient r
# visual representation of correlation is scatter plot

# using function dataframe.corr(self,method='pearson')
# compute pairwise correlation of columns excluding NA

numerical_data=car_data2.select_dtypes(exclude=[object])
print(numerical_data)

numerical_data.corr(method='pearson')
corr_matrix=numerical_data.corr()
print(corr_matrix)










