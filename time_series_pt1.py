# Time series
# Statsmodules is the one more similar to R
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data

print (df.head())
print (df.columns)
print (sm.datasets.macrodata.NOTE)

# Making the statsmodels to put year as index (this can be done with pandas)
index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1','2009Q3'))
df.index = index

print (df.head())

# df['realgdp'].plot()
# plt.show()

gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df['realgdp'])
df['trend'] = gdp_trend
# df[['realgdp','trend']].plot()
# plt.show()

df[['realgdp','trend']]['2000-03-31':].plot()
plt.show()
