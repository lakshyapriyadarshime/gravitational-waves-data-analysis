# Import all the relevant packages and libraries

import numpy as np
import matplotlib.pyplot as plt

N=1000
dt=0.0001
r=np.random.randn(N)
t=np.arange(0, N)*dt

print ("dt=", dt, "sps=", 1/dt)
print ("N=", N, "T=", N*dt)

plt.plot(t,r,'r')
plt.xlabel('Time [s]')
plt.ylabel( 'h(t)')
plt.show()
