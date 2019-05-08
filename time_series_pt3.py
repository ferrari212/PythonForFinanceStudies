# ARIMA (AutoRegressive integrated moving avarege)
# Variance should not be a function of time, mean must be constant, and convariance should not change
# We can take a look if we are going to use AR or MA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('monthly-milk-production-pounds-production.txt')
print (df.head())

# Rename columns
df.columns = ['Month', 'Milk in Pounds per Cow']

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
print (df.head())

print (df.describe().transpose())

df.plot()

time_series = df['Milk in Pounds per Cow']
time_series.rolling(12).mean().plot(label='12 Month Rolling Mean')
time_series.rolling(12).std().plot(label='12 Month Rolling Std')

plt.show()

# Using statsmodels to separete mean and deviation
decomp = seasonal_decompose(time_series)
decomp.plot()

plt.show()
