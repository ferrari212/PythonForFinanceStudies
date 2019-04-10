import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates


mcdon = pd.read_csv('mc.csv',index_col='Date',parse_dates=True)
print(mcdon.head())

# Check that the order of the two coluns are different
# mcdon['Adj. Close'].plot()
# plt.show()
# mcdon['Adj. Volume'].plot()
# plt.show()

# One way is to insert x limits and why limits
# mcdon['Adj. Close'].plot(xlim=['2007-01-01','2009-01-01'], ylim=(20,50), c='red')

# To show dates index you can use plot_date
idx = mcdon.loc['2007-01-01':'2007-05-01'].index
stock = mcdon.loc['2007-01-01':'2007-05-01']['Adj. Close']

fig,ax = plt.subplots()
ax.plot_date(idx,stock,'-')
# print(stock)
# print(idx)

# This is the type of locators
ax.yaxis.grid(True)
ax.xaxis.grid(True)
# Locatting
ax.xaxis.set_major_locator(dates.MonthLocator())
# Formating
ax.xaxis.set_major_formatter(dates.DateFormatter('\n\n%b-%y'))

# insert minor format
# byweekday is the type of week day it will start
ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=0))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))



fig.autofmt_xdate()
plt.tight_layout()


plt.show()
