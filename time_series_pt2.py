# Mean Decomposition
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

airline = pd.read_csv('airline_passengers.txt', index_col='Month')
airline.dropna(inplace=True)

print (airline.head())
print (airline.index)

airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()

airline.plot()
plt.show()

# EWMA Decomposition
# Insert more weight on more recently data
airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline[['Thousands of Passengers','EWMA-12']].plot()
plt.show()

# ETS Decoposition
# This index must be introduced in this way for ETS work
airline.index = pd.to_datetime(airline.index)
print (airline.head())

result = seasonal_decompose(airline['Thousands of Passengers'], model='addtive')

print (result)
result.seasonal.plot()
plt.show()
result.trend.plot()
plt.show()
fig = result.plot()
plt.show()
