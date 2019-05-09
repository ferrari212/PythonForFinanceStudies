# ARIMA (AutoRegressive integrated moving avarege)
# Variance should not be a function of time, mean must be constant, and convariance should not change
# We can take a look if we are going to use AR or MA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

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

# Test if data is stationary or not using adfuller
# if p-value is big it seems like non-stationary
result = adfuller(df['Milk in Pounds per Cow'])

def adf_check(time_series):
    result = adfuller(time_series)
    print ("Augmented Dicky-Fuller Test")
    labels = ['ADF Test Statistic', 'p-value', '# of lags', 'Num of observations used']

    for value, label in zip(result, labels):
        print(label+ " : " +str(value))

    if result[1] <= 0.05:
        print ('strong evidence against null hypothesis')
        print ('reject null hypothesis')
        print ('Data has no unit root and is stationary')
    else:
        print ('weak evidence against null hypothesis')
        print ('Fail to reject null hypothesis')
        print ('Data has unit root and is non-stationary')

adf_check(df['Milk in Pounds per Cow'])

df['First Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(1)

df['First Difference'].plot()
plt.show()

print ('\n')
adf_check(df['First Difference'].dropna())

df['Seccond Difference'] = df['First Difference'] - df['First Difference'].shift(1)

df['Seccond Difference'].plot()
plt.show()

print ('\n')
adf_check(df['Seccond Difference'].dropna())
