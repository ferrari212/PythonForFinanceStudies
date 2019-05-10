# ARIMA (AutoRegressive integrated moving avarege)
# Variance should not be a function of time, mean must be constant, and convariance should not change
# We can take a look if we are going to use AR or MA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Libraries from time-series correlation
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from pandas.tseries.offsets import DateOffset

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

# First Difference
df['First Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(1)

df['First Difference'].plot()
plt.show()

print ('\n')
adf_check(df['First Difference'].dropna())

# Seccond Difference
df['Seccond Difference'] = df['First Difference'] - df['First Difference'].shift(1)

df['Seccond Difference'].plot()
plt.show()

print ('\n')
adf_check(df['Seccond Difference'].dropna())

# Seasonal Difference
df['Seasonal Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(12)

df['Seasonal Difference'].plot()
plt.show()

print ('\n')
adf_check(df['Seasonal Difference'].dropna())

# Seasonal First Difference
df['Seasonal First Difference'] = df['First Difference'] - df['First Difference'].shift(12)

df['Seasonal First Difference'].plot()
plt.show()

print ('\n')
adf_check(df['Seasonal First Difference'].dropna())

fig_first = plot_acf(df['First Difference'].dropna())
plt.show()

fig_first = plot_acf(df['Seasonal First Difference'].dropna())
plt.show()

autocorrelation_plot(df['Seasonal First Difference'].dropna())
plt.show()

# Using ARIMA models with seasona arima SARIMAX
# help(ARIMA)
model = sm.tsa.statespace.SARIMAX(df['Milk in Pounds per Cow'], order=(0,1,0), seasonal_order=(1,1,1,12))
results = model.fit()
print(results.summary())
results.resid.plot()
plt.show()

results.resid.plot(kind='kde')
plt.show()

# does not show future forecast
df['forecast'] = results.predict(start=150, end=168)
df[['Milk in Pounds per Cow','forecast']].plot()
plt.show()

# This will predict future dates
future_dates = [df.index[-1] + DateOffset(months=x) for x in range(1,24)]
print(future_dates)
future_df = pd.DataFrame(index=future_dates, columns=df.columns)
final_df = pd.concat([df, future_df])
final_df['forecast'] = results.predict(start=168, end=192)
final_df[['Milk in Pounds per Cow','forecast']].plot()
plt.show()
