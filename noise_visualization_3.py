# Import all the relevant packages and libraries
import numpy as np
import matplotlib.pyplot as plt

N=100000
dt=0.0001

r=np.random.randn(N)
t=np.arange(0, N)*dt

print("dt=", dt, "sps=", 1/dt)
print("N=", N, "T=", N*dt)

[h,x]=np.histogram(r, bins=50,range=(-5.0,5.0) )
width=(x[1]-x[0])*0.9

f,(ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(t,r,'r')
ax1.grid()
ax2.plot(x[0:-1],h)
ax2.barh(x[0:-1], h, width, color="red")
ax2.grid()
plt.show()

