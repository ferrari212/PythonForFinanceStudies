import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
plt.style.use('ggplot')
# plt.style.use('dark_background')

df3 = pd.read_csv('df3')

print(df3.info())

print(df3.head())

# df3.plot.scatter(x='a', y='b', edgecolors='black', color='red', s=50, figsize=(12,3))

# df3['a'].plot.hist()

# df3['a'].plot.hist(bins=30, color='red', alpha=0.5)

# df3[['a','b']].plot.box()

# df3['d'].plot.density(color='red')

# df3['d'].plot.density(color='red',lw=5, ls='--')

# df3.ix[0:30].plot.area(alpha=0.4)

# df3.iloc[0:30].plot.area(alpha=0.4)
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
