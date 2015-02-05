import random
import matplotlib.pyplot as plt
import numpy as np
import sys
from mpl_toolkits.mplot3d import Axes3D


if len(sys.argv) != 2:
    print "Este programa necesita un (1) argumento para funcionar"
    sys.exit()


N=int(sys.argv[1])
x_walk = np.zeros(N)
y_walk = np.zeros(N)
z_walk = np.zeros(N)
for i in range(0,N-1):
    x0=2*random.random()-1
    y0=2*random.random()-1
    z0=2*random.random()-1
    
    r=np.sqrt(x0**2 +y0**2 +z0**2)
    
    x0=x0/r
    y0=y0/r
    z0=z0/r
    
    x_walk[i+1] = x_walk[i]+ x0
    y_walk[i+1] = y_walk[i]+ y0
    z_walk[i+1] = z_walk[i]+ z0

fig = plt.figure()
ax = Axes3D(fig)
ax.set_aspect('equal')
ax.set_xlabel("$x$",fontsize=25)
ax.set_ylabel("$y$",fontsize=25)
ax.set_zlabel("$z$",fontsize=25)
ax.set_title("$\mathrm{Trayectoria}$", fontsize=25)
ax.plot(x_walk, y_walk, z_walk)
plt.show()