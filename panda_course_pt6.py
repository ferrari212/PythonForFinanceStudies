import numpy as np
import pandas as pd

data = {'Company': ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales': [200,120,340,124,243,350]}

#group elements by the same ID
df = pd.DataFrame(data)
print (df)

byComp = df.groupby('Company')
print (byComp)

# It ignores non numerical
print (byComp.mean())
print (byComp.std())
print (byComp.sum())
print (byComp.sum().loc['FB'])
print (df.groupby('Company').sum().loc['FB'])

# Agregate by values
print (df.groupby('Company').count())
print (df.groupby('Company').max())
print (df.groupby('Company').min())

# Use describe
print (df.groupby('Company').describe())
print (df.groupby('Company').describe().transpose())
print (df.groupby('Company').describe().transpose()['FB'])
