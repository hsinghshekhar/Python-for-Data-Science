# Which of the following are libraries in Python?
#Pandas
#Matplotlib
#NumPy
#All of the above  (Ans-d)

# Which of the following is the correct approach to fill missing values in case of categorical variable?
# Mean
# median
# Mode
# None of the above

# Ans-(c) 

# What will be the output of the following code?
import numpy as np
B=[True, 2,3.0,np.nan,"False"]
print([type(i) for i in B])

# Ans-[<class 'bool'>, <class 'int'>, <class 'float'>, <class 'float'>, <class 'str'>]

# What will be the output of the following code?
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[::2])

# Ans- [1 3 5] 

# Read the ‘flavors_of_cocoa.csv’ file as a dataframe ‘df_cocoa’ and answer questions . The description of features/variables is given below
import pandas as pd
df_cocoa=pd.read_csv('flavors_of_cocoa (1).csv')
print(df_cocoa) 






# What does df.info() provide?
# Summary of the DataFrame, including the number of non-null entries.
# The first 5 rows of the DataFrame
# The data types of the columns
# The correlation matrix of the DataFrame

# Ans- (a) 


# Assume a pandas dataframe df_cars which when printed is as shown below. Based on this information,
import pandas as pd
toto_csv=pd.read_csv('/Users/shekhar55003gmail.com/Desktop/Data Science/Python for Data Science/Toyota.csv')
print(toto_csv)
print(toto_csv.loc[:,'Age'])  # example
print(toto_csv.describe())

# Of the following set of statements, which of them can be used to extract the column Type as a separate dataframe?
# df_cars[[‘Type’]]
# df_cars.iloc[[:, 1]
# df_cars.loc[:, [‘Type’]]
# None of the above

# Ans-  (a) and (c)

# The method df_cars.describe() will give description of which of the following column?
# Car name
# Brand
# Price (in lakhs)
# All of the above

# Ans- (d) 

# Which pandas function is used to stack the dataframes vertically?
# pd.merge()
# pd.concat()
# join()
# None of the above

# Ans- (b) 













