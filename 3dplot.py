import numpy as np
import matplotlib.pyplot as plt

points = np.array([[3, 4, 3], [1, 2, 3]])

z = 15 * np.random.random(100)
x = 15 * np.random.random(100)
y = 15 * np.random.random(100)

dx = []
dy = []

for i, d in enumerate(z):
    dx.append(x[i] / d)
    dy.append(y[i] / d)


fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111, projection='3d')

ax2 = fig.add_subplot(222)
gca = plt.gca()
gca.set_xlim([0, 5])
gca.set_ylim([0, 5])

ax.scatter(x, y, z)

ax2.scatter(dx, dy)

# ok
plt.show()

