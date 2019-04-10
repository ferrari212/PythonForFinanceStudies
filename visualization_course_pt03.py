import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,.9,.9])

# RGB Basic colors, lw (linewidth), alpha (transparancy), ls (linestyle), markeredge is for border
ax.plot(x,y,color='purple', lw=3, alpha=1, ls='-.', marker='*', markersize = 20, markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green')
# RGB Hex code
# ax.plot(x,y,color='#FF8C00')

# zoom in the part you want
# ax.set_xlim([0,1])
# ax.set_ylim([0,1])


# plt.tight_layout()
plt.show()
