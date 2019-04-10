#Data Frames
import numpy as np
import pandas as pd

from numpy.random import randn

#Makes every cell same random number
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df)

print (df['W'])
print (type(df['W']))
print (df[['W','Z']])

#do not use it because can make it mess
print (df.W)

df['NEW'] = df['W'] + df['Y']
print(df)

# axis equals to one are related to colums
# implace is to change deleting the source
df.drop('NEW',axis=1, inplace = True)

print (df)

df.drop('E', axis=0)

print (df.shape)

# select rows
print (df.loc['A'])

# select rows by index
print (df.iloc[2])

# select specific place
print (df.loc['B','Y'])

# select a list
print (df.loc[['A','B'],['W','Y']])
