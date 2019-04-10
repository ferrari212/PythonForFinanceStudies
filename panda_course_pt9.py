# data imput and output
import numpy as np
import pandas as pd
import os

# print (os.getcwd())
# print (os.listdir(os.getcwd()))

# pd.read_excel('example.xlsx')
# pd.read_excel('teste2.xls')

# It is because the incriptions it is not working
# df = pd.read_csv("example.csv", encoding = "ISO-8859-1", names=["col1", "col2", "col3", "col4"], error_bad_lines=False, engine='c')
df = pd.read_csv("comma.csv")
print (df)
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
# print (type(data))
# print (data)
print (data[0].head())

# to work with sql
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

data[0].to_sql('my_table', engine)
sqldf = pd.read_sql('my_table', con=engine)

print (sqldf)
