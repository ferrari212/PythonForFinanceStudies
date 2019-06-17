#!/usr/bin/env python
# coding: utf-8

# In[1]:


from quantopian.pipeline import Pipeline


# In[2]:


def make_pipeline():
    return Pipeline()


# In[3]:


pipe = make_pipeline()


# In[4]:


pipe


# In[5]:


from quantopian.research import run_pipeline


# In[6]:


result = run_pipeline(pipe, '2017-01-03', '2017-01-03')


# In[7]:


# result


# In[8]:


from quantopian.pipeline.data.builtin import USEquityPricing


# In[9]:


from quantopian.pipeline.factors import SimpleMovingAverage


# In[10]:


SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=30)


# In[11]:


def make_pipeline():
    
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=30)
    
    return Pipeline(columns={'30 Day Mean Close': mean_close_30})


# In[12]:


results = run_pipeline(make_pipeline(), '2017-01-03', '2017-01-03')


# In[13]:


results.head()


# In[14]:


def make_pipeline():
    
    latest_close = USEquityPricing.close.latest
    small_price = latest_close < 5
    
    
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=30, mask=small_price)
    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=10, mask=small_price)
    
    percent_diff = (mean_close_10 - mean_close_30)/mean_close_30
    
    perc_filter = percent_diff > 0
    
#     Combine Filters
    final_filter = perc_filter & small_price
    
    return Pipeline(columns={
        '30 Day Mean Close': mean_close_30,
        'Percent Diff': percent_diff,
        'Latest Close': latest_close,
        'Percent Filter': perc_filter
    }, screen = final_filter)


# In[15]:


results = run_pipeline(make_pipeline(), '2017-01-03', '2017-01-03')


# In[16]:


results.head()


# In[17]:


from quantopian.pipeline.data import morningstar
from quantopian.pipeline.classifiers.morningstar import Sector


# In[18]:


morningstar_sector = Sector()


# In[19]:


morningstar_sector


# In[20]:


exchange = morningstar.share_class_reference.exchange_id.latest


# In[21]:


exchange


# In[22]:


nyse_filter = exchange.eq('NYS')


# In[23]:


def make_pipeline():
    
    latest_close = USEquityPricing.close.latest
    small_price = latest_close < 5
    
#     Classifier
    nyse_filter = exchange.eq('NYS')
    
    
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=30, mask=small_price)
    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=10, mask=small_price)
    
    percent_diff = (mean_close_10 - mean_close_30)/mean_close_30
    
    perc_filter = percent_diff > 0
    
#     Combine Filters
    final_filter = perc_filter & nyse_filter
    
    return Pipeline(columns={
        '30 Day Mean Close': mean_close_30,
        'Percent Diff': percent_diff,
        'Latest Close': latest_close,
        'Percent Filter': perc_filter
    }, screen = final_filter)


# In[25]:


results = run_pipeline(make_pipeline(),'2017-01-03','2017-01-03')


# In[26]:


results.info()

