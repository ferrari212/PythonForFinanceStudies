import numpy as np
import pandas as pd

from numpy.random import randn

#Makes every cell same random number
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df)

print(df > 0)

print(df[ df > 0])

print(df['W']>0)
print(df[df['Z']<0])
print(df[df['W']<0]['X'])
print(df[df['W']<0][['X','Y']])

boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
print(result[mycols])

# AND operator for a matrix
print(df[(df['W']>0) & (df['Y']>1)])
# OR operator for a matrix
print(df[(df['W']>0) | (df['Y']>1)])

print(df.reset_index())
# Pass a inplace to have it ocurring inplace

newind = 'CA NY WY OR CO'.split()
print (newind)

df['States'] = newind
print(df)

print(df.set_index('States'))
