# Exercises: manipulating the data introduced in the html file
import numpy as np
import pandas as pd

data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
banks = data[0]

print("\n Show the head of the dataframe")
print (banks.head())

print("\n What are the column names?")
print (banks.columns)

print("\n How many states (ST) are represented in this data set?")
print (banks['ST'].nunique())

print("\n Get a list of array of all the states in the data set?")
print (banks['ST'].unique())

print("\n What are the top 5 states with the most failed banks?")
print (banks.groupby('ST').count().nlargest(5,'Bank Name')['Bank Name'])
# Simmilary
# print (banks.groupby('ST').count().sort_values('Bank Name', ascending=False).iloc[:5]['Bank Name'])

print("\n What are the top 5 acquiring institutions?")
print (banks.groupby('Acquiring Institution').count().nlargest(5,'Bank Name')['Bank Name'])
# Simmilary
# print (banks['Acquiring Institution'].value_counts().iloc[:5])

print("\n How many banks has the State Bank of Texas acquired? How many of them were actyally in Texas?")
list_banks_acquired = banks [banks['Acquiring Institution'] == 'State Bank of Texas']
print (list_banks_acquired )
print (banks [banks['Acquiring Institution'] == 'State Bank of Texas'].count()['Bank Name'])
print (banks [banks['Acquiring Institution'] == 'State Bank of Texas'][banks [banks['Acquiring Institution'] == 'State Bank of Texas']['ST'] == 'TX'].count()['Bank Name'])

print ("\n What is most common city in California for a bank to fail in?")
print (banks[banks['ST'] == 'CA'].groupby('City').count().nlargest(1,'Bank Name')['Bank Name'])

print("\n How many banks don't have the word 'Bank' in their name?")
print (sum(banks['Bank Name'].apply(lambda name: 'Bank' not in name)))

print("\n How many bank start with the letter 's'?")
print (sum(banks['Bank Name'].apply(lambda name: 's' in name[0].lower())))

print("\n How many CERT values are above 20000?")
print (banks[banks['CERT'] > 20000].count())

print("\n How many banks consists of just two words?")
print (sum(banks['Bank Name'].apply(lambda name: len(name.split()) == 2)))

print("\n How many banks closed in the year of 2008?")
# print (banks.info())
print (sum(banks['Closing Date'].apply(lambda date: date[-2:] == '08')))
# using date expression in the last Exercises
dates = pd.to_datetime(banks['Closing Date'])
print (sum(dates.apply(lambda date: date.year == 2008)))
