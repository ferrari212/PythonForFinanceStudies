# This is part of quantopian algorith strategy
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


start = '2015-01-01'
end = '2017-01-01'

united = get_pricing('UAL', start_date=start, end_date=end)
american = get_pricing('AAL', start_date=start, end_date=end)


# In[4]:


united.head()


# In[5]:


american.head()


# In[7]:


american['close_price'].plot(label='AA', figsize=(12,8))
united['close_price'].plot(label='United')
plt.legend()


# In[8]:


np.corrcoef(american['close_price'], united['close_price'])


# In[11]:


spread = american['close_price'] - united['close_price']
spread.plot(label='Spread', figsize=(12,8))
plt.axhline(spread.mean(), c )


# In[13]:


def zscore(stocks):
    return (stocks - stocks.mean())/np.std(stocks)


# In[15]:


zscore(spread).plot(figsize=(14,8))
plt.axhline(zscore(spread).mean(), color='black')
plt.axhline(1.0,c='g',ls='--')
plt.axhline(-1.0,c='r',ls='--')


# In[17]:


spread_mavg1 = spread.rolling(1).mean()

spread_mav30 = spread.rolling(30).mean()

std_30 = spread.rolling(30).std()

zscore_30_1 = (spread_mavg1 - spread_mav30)/std_30


# In[18]:


zscore_30_1.plot(figsize=(12,8),label='Rolling 30 Day Z score')
plt.axhline(0, color='black')
plt.axhline(1.0, color='red', ls='--')


# In[ ]:





# In[ ]:
