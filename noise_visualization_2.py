
# Import all the relevant packages and libraries
import numpy as np
import matplotlib.pyplot as plt

N=100000
dt=0.0001

r=np.random.randn(N)
t=np.arange(0, N)*dt

print("dt=", dt, "sps=", 1/dt)
print("N=", N, "T=", N*dt)

plt.plot(t,r,'r')
plt.xlabel('Time [s]')
plt.ylabel( 'h(t)')
plt.show()

[h,x]=np.histogram(r, bins=50,range=(-5.0,5.0) )
width=(x[1]-x[0])*0.9

plt.bar(x[0:-1], h, width, color="red")
plt.plot(x[0:-1],h)
plt.xlabel('h(t)')
plt.ylabel('Counts')
plt.show()

