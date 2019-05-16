import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# CAPM Code Along
from scipy import stats

start = pd.to_datetime('2010-01-04')
end = pd.to_datetime('2017-07-25')

spy_etf = web.DataReader('SPY','yahoo', start, end)
aapl = web.DataReader('AAPL','yahoo', start, end)

print (spy_etf.head())
print (aapl.head())


aapl['Close'].plot(label='AAPL')
spy_etf['Close'].plot(label='SPY Index')
plt.legend()
plt.show()

# With CAPM we can have some idea about cumulative returns coef. (alpha, beta)
aapl['Cumulative'] = aapl['Close']/aapl['Close'].iloc[0]
spy_etf['Cumulative'] = spy_etf['Close']/spy_etf['Close'].iloc[0]

aapl['Cumulative'].plot(label='AAPL')
spy_etf['Cumulative'].plot(label='SPY')
plt.legend()
plt.show()

aapl['Daily Return'] = aapl['Close'].pct_change(1)
spy_etf['Daily Return'] = spy_etf['Close'].pct_change(1)
plt.scatter(aapl['Daily Return'], spy_etf['Daily Return'], alpha=0.25)
plt.show()

beta,alpha,r_value,p_value,std_err = stats.linregress(aapl['Daily Return'].iloc[1:],
                                                        spy_etf['Daily Return'].iloc[1:])
print ('\n Beta:')
print (beta)
print ('\n Alpha:')
print (alpha)

# Let's understand the concept by some fake stock
noise = np.random.normal(0, 0.001, len(spy_etf.iloc[1:]))
print ('\n Noise:')
print (noise)

fake_stock = spy_etf['Daily Return'].iloc[1:] + noise
plt.scatter(fake_stock, spy_etf['Daily Return'].iloc[1:],alpha=0.25)
plt.show()

beta,alpha,r_value,p_value,std_err = stats.linregress(fake_stock,
                                                        spy_etf['Daily Return'].iloc[1:])

print ('\n Beta for Fake Stock (notice it is almost equals to one):')
print (beta)
print ('\n Alpha for Fake Stock:')
print (alpha)
