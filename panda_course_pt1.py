#working with numpy and panda
import numpy as np
import pandas as pd

#using series
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':100}

print ( pd.Series(my_list))
print ( pd.Series(my_list, index=labels))

print ( pd.Series(arr))
print ( pd.Series(arr, labels))

print ( pd.Series(d))

print ( pd.Series(data=labels))

#inserting functions as Series
print (pd.Series([sum,print,len]))

print (pd.Series([1,2,3,4], index = ['USA','CHINA','FRANCE','GERMANY']))

ser1 = pd.Series([1,2,3,4], index = ['USA','CHINA','FRANCE','GERMANY'])
ser2 = pd.Series([1,2,3,4], index = ['USA','CHINA','ITALY','JAPAN'])
print (ser1['CHINA'])
print (ser1 + ser2)
