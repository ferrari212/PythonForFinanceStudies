# Exercises
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

# Exercise 1
plt.plot([0, 100],[0, 200])
plt.title('Exercise 1')

# Exercise 2
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.set_title('Exercise 2')
axes2 = fig.add_axes([0.2,0.5,0.2,0.2])

# Exercise 3
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.set_title('Exercise 3')
axes2 = fig.add_axes([0.2,0.5,0.2,0.2])
axes2.set_title('Minor Graph')
axes1.plot(x,y,color='red')
axes2.plot([0, 100],[0, 200])

# Exercise 3
fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(8,2))
axes[0].plot([0, 100],[0, 200],color='blue',ls='-.')
axes[0].set_title('Exercise 4')
axes[1].plot(x,y,color='red')
axes[1].set_title('Exercise 4')

plt.tight_layout()
plt.show()
