# Complete exercise to see the analyses of solutions from two types of companies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
print ("\n The Ford company announced the massive investment on new car lines")

print ("\n Interesting, looks like there was huge amount of money traded for Tesla somewhere in early 2014. What date was that and what happened?")
tesla['Total Traded'] = tesla['Volume']*tesla['Open']
gm['Total Traded'] = gm['Volume']*gm['Open']
ford['Total Traded'] = ford['Volume']*ford['Open']
print (tesla[tesla['Total Traded'] == tesla['Total Traded'].max()].index.values)
print ('\n Announced a much higher than profit expected ')

tesla['Total Traded'].plot(figsize=(12,6), label='Tesla')
gm['Total Traded'].plot(figsize=(12,6), label='GM')
ford['Total Traded'].plot(figsize=(12,6), label='Ford')

plt.legend()
plt.show()

print ("\n Let's practice plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for GM.")
gm['Open 50 day MA'] = gm['Open'].rolling(window=50).mean()
gm['Open 200 day MA'] = gm['Open'].rolling(window=200).mean()
gm[['Open 50 day MA','Open 200 day MA','Open']].plot(figsize=(12,6))


plt.legend()
plt.show()
