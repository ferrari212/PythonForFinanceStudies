import matplotlib.pyplot as plt
import numpy as np
# uncomment plt.show() to show the graphs

x = np.linspace(0,5,11)
y = x ** 2

# Using subplot in object oriented
fig,axes = plt.subplots(nrows=1, ncols=2)

# plt.show()

# Interation
# for current_ax in axes:
#     current_ax.plot(x,y)


# each one index
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Seccond Plot')
plt.tight_layout()
plt.show()

# Figure Size and DPI
# fig = plt.figure(figsize=(8,2))
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)
#
# plt.tight_layout()
# plt.show()

# Subplots
fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()
plt.show()

# creating hight quality figures
# it is possible to create figures in different formats like .png, .jpeg, .jpgw
# dpi is the quality of the figure exported
# fig.savefig('my_picture.png', dpi=200)

# two graphs in same graphs
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,.9,.9])
ax.plot(x,x**2, label='X Squared')
ax.plot(x,x**3, label='X Cubed')
ax.legend(loc=0)

plt.show()
