import numpy as np

arr = np.arange(0,11)

print (arr[8])
print (arr[1:5])
print (arr[:5])
print (arr[3:])

#You can not do it with a normal python list
arr[0:5] = 100
print (arr)

#slicing your array
arr = np.arange(0,11)
slice_of_arr = arr[0:6]

#keeping the array data
print (slice_of_arr)
slice_of_arr[:] = 99
print (slice_of_arr)
print (arr)

#to make a copy
arr_copy = arr.copy()
print (arr)
arr_copy[:] = 200
print (arr)
print (arr_copy)

#To take a index (i,j) it is just use m[i,j] in numpy
# You can take a range by using : , for example mat[:2, 1:]

#CONDITIONAL SELECTION
arr = np.arange(1,11)
print (arr > 4)
bool_arr = arr > 4
#to send just the true values
print (arr[bool_arr])
print (arr[arr > 4])
print (arr[arr <= 9])
