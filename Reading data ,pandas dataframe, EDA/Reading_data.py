           ############## Importing Data into Spyder or IDE

import os # os operator change working directory
import pandas as pd # pandas library work for dataframe or data


### Importing Data using function pd.read()
data_csv=pd.read_csv('Iris_data_sample.csv')  # inside the function give file name not path name

### Removing index column
data_csv=pd.read_csv('Iris_data_sample.csv', index_col=0)
print(data_csv)

## now replacing the value of ?? and ## and nan using na_values=["??"]
 #### Import excel spreadsheet
data_xlsx=pd.read_xlsx('Iris_data_sample.xlsx',sheet_name='Iris_data')
print(data_xlsx)

## remove index column and missing values ?? and ##
data_xlsx=pd.read_excel('Iris_data_sample.xlsx',index_col=0,na_values=["??","##"]) 

## Importing Text data
data_txt1=pd.read_table('Iris_data_sample.txt', delimiter="")
print(data_txt1)
