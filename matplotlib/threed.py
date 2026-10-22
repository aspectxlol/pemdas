import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
xpos = 10
ypos = 10
zpos = 10

dx = 10
dy = 10
dz = 10

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', alpha=0.8)
plt.show()