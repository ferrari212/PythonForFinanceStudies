import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This import is to Opitimization
from scipy.optimize import minimize

aapl = pd.read_csv('AAPL_CLOSE', index_col='Date', parse_dates=True)
cisco = pd.read_csv('CISCO_CLOSE', index_col='Date', parse_dates=True)
ibm = pd.read_csv('IBM_CLOSE', index_col='Date', parse_dates=True)
amzn = pd.read_csv('AMZN_CLOSE', index_col='Date', parse_dates=True)


stocks = pd.concat([aapl,cisco,ibm,amzn], axis=1)
stocks.columns = ['aapl','cisco','ibm','amzn']
print (stocks.head())

# percentage change
print ('\n')
print (stocks.pct_change(1).mean())
print ('\n')
print (stocks.pct_change(1).corr())

# Logarritime return
log_ret = np.log(stocks/stocks.shift(1))
print ('\n')
print (log_ret.head())

log_ret.hist(bins=100)
plt.tight_layout
plt.show()

print ('\n')
print (log_ret.mean())

# covarience of Logarritime
print ('\n Multipling by Days')
print (log_ret.cov() * 252)

# Randonly choosing the alocation
# for educational propose let's get always same random number with seed
np.random.seed(101)

# Weights
weights = np.array(np.random.random(4))
print ('\n Random Weights:')
print (weights)

print ('\n Rebalance:')
weights = weights/np.sum(weights)
print (weights)

# Expected Return
print ('\n Expected Portfolio Return')
exp_ret = np.sum(log_ret.mean()*weights*252)
print (exp_ret)

# Expected Volatility
print ('\n Expected Volatility')
exp_vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
print (exp_vol)

# Sharpe Ratio
print ('\n Sharpe Ratio')
SR = exp_ret/exp_vol
print (SR)

# Now qhat we are going to do is to putt the above method in a for loop
# number of portfolios analysed
num_ports = 2500
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for ind in range(num_ports):
    # Weights
    weights = np.array(np.random.random(4))
    weights = weights/np.sum(weights)

    # Save Weights
    all_weights[ind,:] = weights

    # Expected Return
    ret_arr[ind] = np.sum(log_ret.mean()*weights*252)

    # Expected Volatility
    vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))

    # Sharpe Ratio
    sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]

print ('\n Maximum Sharpe Ratio Possible')
print (sharpe_arr.max())

print ('\n Maximum Index Sharpe Ratio Possible')
print (sharpe_arr.argmax())

print ('\n Optimal Alocation Possible')
print (all_weights[sharpe_arr.argmax(),:])

plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

plt.scatter(vol_arr[sharpe_arr.argmax()],ret_arr[sharpe_arr.argmax()],c='red',s=50,edgecolors='black')

# Opitimization function
def get_ret_vol_sr (weights):
    weights = np.array(weights)
    ret = np.sum(log_ret.mean()*weights)*252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
    sr = ret/vol
    return np.array([ret,vol,sr])

# Trying to reduce the minimized volativity
def neg_sharpe (weights):
    return get_ret_vol_sr(weights)[2]*(-1)

# return 0 if the sum of the weights is 1
def check_sum(weights):
    return np.sum(weights) - 1

cons = ({'type':'eq', 'fun':check_sum})
# Those are the bounds of experimentation
bounds = ((0,1),(0,1),(0,1),(0,1))
# Initial test
init_guess = [0.25,0.25,0.25,0.25]

# function for minimize
opt_results = minimize(neg_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=cons)
print ('\n Distributions that gives best results with Maximum Sharpie')
print (opt_results.x)
print ('\n Values of [return, volative, Sharpe ratio] of Maximum Sharpie')
print (get_ret_vol_sr(opt_results.x))

# See best frontier
frontier_y = np.linspace(0,0.3,100)

# function to minimize Volatility
def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]

frontier_volatility = []
for possible_reutn in frontier_y:
    cons = ({'type':'eq', 'fun':check_sum},
                    {'type':'eq', 'fun': lambda w: get_ret_vol_sr(w)[0]-possible_reutn})
    result = minimize(minimize_volatility,init_guess,method='SLSQP',bounds=bounds,constraints=cons)

    frontier_volatility.append(result['fun'])

plt.plot(frontier_volatility, frontier_y, 'g--', linewidth=3)
plt.show()
