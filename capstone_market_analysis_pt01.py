# Complete exercise to see the analyses of solutions from two types of companies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY
# from matplotlib.finance import candlestick_ohlc
from mpl_finance import candlestick_ohlc

from pandas.plotting import scatter_matrix

import pandas_datareader.data as web
import datetime


print ("\n Use pandas_datareader to obtain the historical stock information for Tesla from Jan 1, 2012 to Jan 1, 2017.")
tesla = pd.read_csv('Tesla_Stock.txt', index_col='Date', parse_dates=True)
print (tesla.head())

print ("\n Repeat the same steps to grab data for Ford and GM (General Motors).")
gm = pd.read_csv('GM_Stock.txt', index_col='Date', parse_dates=True)
print (gm.head())

print ("\n Use pandas_datareader to obtain the historical stock information for Tesla from Jan 1, 2012 to Jan 1, 2017.")
ford = pd.read_csv('Ford_Stock.txt', index_col='Date', parse_dates=True)
print (ford.head())

print ("\n Recreate this linear plot of all the stocks' Open price ! Hint: For the legend, use label parameter and plt.legend().")
tesla['Open'].plot(figsize=(12,6), label='Tesla')
gm['Open'].plot(figsize=(12,6), label='GM')
ford['Open'].plot(figsize=(12,6), label='Ford')

plt.legend()
plt.title('Open Price', fontweight="bold", fontsize=20)
plt.show()

print ("\n Plot the Volume of stock traded each day.")

tesla['Volume'].plot(figsize=(12,6), label='Tesla')
gm['Volume'].plot(figsize=(12,6), label='GM')
ford['Volume'].plot(figsize=(12,6), label='Ford')

plt.legend()
plt.title('Volume traded', fontweight="bold", fontsize=20)
plt.show()

print ("\n Interesting, looks like Ford had a really big spike somewhere in late 2013. What was the date of this maximum trading volume for Ford? What happened that day?")
print (ford[ford['Volume'] == ford['Volume'].max()].index.values)
# Alternatively could be used
# print (ford['Volume'].argmax())
print ("\n The Ford company announced the massive investment on new car lines")

tesla['Total Traded'] = tesla['Volume']*tesla['Open']
gm['Total Traded'] = gm['Volume']*gm['Open']
ford['Total Traded'] = ford['Volume']*ford['Open']

print ("\n Interesting, looks like there was huge amount of money traded for Tesla somewhere in early 2014. What date was that and what happened?")
print (tesla[tesla['Total Traded'] == tesla['Total Traded'].max()].index.values)
print ('\n Announced a much higher than profit expected ')

tesla['Total Traded'].plot(figsize=(12,6), label='Tesla')
gm['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label='Ford')

plt.legend()
plt.title('Total Traded', fontweight="bold", fontsize=20)
plt.show()

print ("\n Let's practice plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for GM.")
gm['Open 50 day MA'] = gm['Open'].rolling(window=50).mean()
gm['Open 200 day MA'] = gm['Open'].rolling(window=200).mean()
gm[['Open 50 day MA','Open 200 day MA','Open']].plot(figsize=(12,6))

plt.legend()
plt.show()

print ("\n Finally lets see if there is a relationship between these stocks.")
print (tesla['Open'].values)
# df = pd.DataFrame([tesla['Open'], gm['Open'], ford['Open']], columns=['Tesla', 'GM', 'Ford'])
df1 = pd.DataFrame({'Tesla': tesla['Open'].values,
                    'GM': gm['Open'].values,
                    'Ford': ford['Open'].values,})
scatter_matrix(df1, alpha=0.2, figsize=(6, 6), diagonal='hist', hist_kwds={'bins':50})

plt.legend()
plt.show()

print ("\n Let's plot candle sticks.")

ford_reset = ford.loc['2012-01'].reset_index()
ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))

list_of_cols = ['date_ax', 'Open', 'High', 'Low', 'Close']
ford_values = [tuple(vals) for vals in ford_reset[list_of_cols].values]

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values, width=0.6, colorup='g',colordown='r');

plt.legend()
plt.show()

print ("\n First we will begin by calculating the daily percentage change.")
# Pandas give us also a way to pct_change
# tesla['returns'] = tesla['Close'].pct_change(1)
tesla['returns'] = (tesla['Open']/tesla.shift(1, axis = 0)['Open'])-1
gm['returns'] = (gm['Open']/gm.shift(1, axis = 0)['Open'])-1
ford['returns'] = (ford['Open']/ford.shift(1, axis = 0)['Open'])-1
print (tesla.head())
print (gm.head())
print (ford.head())

print ("\n Now plot a histogram.")
print (tesla['returns'].values)
df2 = pd.DataFrame({'Tesla': tesla['returns'].values,
                    'GM': gm['returns'].values,
                    'Ford': ford['returns'].values},
                    columns=['Tesla', 'GM', 'Ford'])

df2.plot.hist(alpha=0.4, bins=100)
plt.show()

print ("\n Try also plotting a KDE instead of histograms.")
df2.plot.kde()
plt.show()

print ("\n Try also creating some box plots comparing the returns.")
df2.plot.box()
plt.show()

print ("\n Create a scatter matrix plot to see the correlation.")
scatter_matrix(df2, alpha=0.2, figsize=(6, 6), diagonal='hist', hist_kwds={'bins':50})
plt.show()

print ("\n It loo ks like Ford and GM do have some sort of possible relationship.")
df2.plot.scatter(x='Ford', y='GM', edgecolors='black', s=50, alpha=0.5)
plt.show()

print ("\n Cumulative Daily Returns.")
tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()
gm['Cumulative Return'] = (1 + gm['returns']).cumprod()
ford['Cumulative Return'] = (1 + ford['returns']).cumprod()

print (tesla.head())
print (gm.head())
print (ford.head())

print ("\n  Now plot the Cumulative Return columns against the time series index.")
tesla['Cumulative Return'].plot(figsize=(12,6), label='Tesla')
gm['Cumulative Return'].plot(figsize=(12,6), label='GM')
ford['Cumulative Return'].plot(figsize=(12,6), label='Ford')

plt.legend()
plt.title('Cumulative Return', fontweight="bold", fontsize=20)

plt.show()
