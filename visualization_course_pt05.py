import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# import matplotlib as mpl
#
# mpl.rcParams['patch.force_edgecolor'] = True

df1 = pd.read_csv('df1',index_col=0)
print(df1.head())

df2 = pd.read_csv('df2')
print(df2.head())

# One way by pandas library
# df1['A'].hist()

# Another way by pandas library
# df1['A'].plot(kind='hist',bins=30)

# A third way to do that
# df1['A'].plot.hist()
#
# df2.plot.area(alpha=0.4)
#
# df2.plot.bar(stacked=True)

# df1['A'].plot.hist(bins=50)

# df1.plot.line(y='B',figsize=(12,3), lw=1)

# c means the color will be equal to collom C, edgecolors is the edge of the circles collors
# df1.plot.scatter(x='A', y='B', c='C', edgecolors='black')

# cmap means the color map type
# df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm', edgecolors='black')

# s is telling that each point are going to have the size of "C" multiplied by 100
# df1.plot.scatter(x='A', y='B', s=df1['C']*100, edgecolors='black')

# box graphs
# df2.plot.box()

df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
print(df.head())

# Hexagon plot
# df.plot.hexbin(x='a',y='b', gridsize=25, cmap='coolwarm')

# Density estimation (both kde or density are valued4)
# df2['a'].plot.kde()
df2['a'].plot.density()
df2.plot.density()

plt.show()
