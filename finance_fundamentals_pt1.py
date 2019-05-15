# Sharpe Ration is the for measure for calculating risk-adjusted returns
# SR = (Mean Return - Mean Free Return)/(Std. Dev)

import pandas as pd
import quandl

import matplotlib.pyplot as plt

start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')

quandl.ApiConfig.api_key = "zBYuKnB1jL7x6nykV_28"
aapl = quandl.get('WIKI/AAPL.11', start_date=start, end_date=end)
cisco = quandl.get('WIKI/CSCO.11', start_date=start, end_date=end)
ibm = quandl.get('WIKI/IBM.11', start_date=start, end_date=end)
amzn = quandl.get('WIKI/AMZN.11', start_date=start, end_date=end)

print (aapl.head())

for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Normed Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']

print (aapl.head())

# Let's take a look a application on portfolio
# 30% in apple
# 20% in cisco
# 40% in amazon
# 10% in ibm
for stock_df, allo in zip((aapl,cisco,ibm,amzn), [.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return']*allo

print (aapl.head())

for stock_df in (aapl, cisco, ibm, amzn):
    stock_df['Position Values'] = stock_df['Allocation']*1000000

all_pos_vals = [aapl['Position Values'], cisco['Position Values'],
                ibm['Position Values'], amzn['Position Values']]
portfolio_val = pd.concat(all_pos_vals, axis=1)

portfolio_val.columns = ['AAPL Pos', 'CISCO Pos', 'IBM Pos', 'AMZN Pos']
portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)

print (aapl.head())

portfolio_val['Total Pos'].plot()
plt.title('Total Portfolio Value')

plt.show()


portfolio_val.drop('Total Pos', axis=1).plot()
plt.title('Portfolio Share')
plt.show()

portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)
print ('\n Mean Daily Return:')
print (portfolio_val['Daily Return'].mean())

print ('\n Standard deviation:')
print (portfolio_val['Daily Return'].std())

portfolio_val['Daily Return'].plot(kind='hist', bins=100)
plt.show()
portfolio_val['Daily Return'].plot(kind='kde')
plt.show()

cumulative_return = 100*(portfolio_val['Total Pos'][-1]/portfolio_val['Total Pos'][0] - 1)
print ('\n Cumulative Return:')
print (cumulative_return)

# Sharpie Ration
SR = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std()
print ('\n Sharpie Ration:')
print (SR)

print ('\n Anual Sharpie Ration:')
ASR = (252**0.5)*SR
print (ASR)
