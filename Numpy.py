                   ######## NUMPY Library




import numpy as np
my_list=[1,2,3,4]
array=np.array(my_list, dtype=int)
print(array)
print(type(array)) # type of object in array
print(len(array)) # how many object in array or length 
print(array.ndim)  # dim of array is number of column 
print(array.shape) # shape of array is like shape of matrix

array2=array.reshape(3, 2)   # change into shape 4 by 1 into 3 by 2
print(array2)




#### Nested Python List
import nupmy as np 
my_list2=[1,2,3,4,5]
my_list3=[2,3,4,5,6]
my_list4=[9,7,6,8,9]
mul_arr=np.array([my_list2,my_list3,my_list4])
print(mul_arr)


#### Numpy Attributes
a=np.array([1,2,3],[4,5,6])
print(a.shape) #2 by 3 shape

a.reshape(3,2)
print(a)

# range
r = range(24)
print(r)

## create range using sequence using arrange() function
p=np.arrange(24)
print(p) 
print(a.ndim)
