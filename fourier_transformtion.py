import numpy as np
import matplotlib.pyplot as plt
N=1000
sps=40.0
dt=1.0/sps
f0=10.0
df=sps/N
f=np.arange(0,N/2)*df
t=np.arange(0,N)*dt
y=np.sin(2*np.pi*f0*t)+3.0*np.random.randn(N)
fy=np.fft.fft(y)
f=np.arange(0,N/2)*df
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(t,y,'r')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('h(t)')
ax2.plot(f, np.abs(fy[0:(N//2)]),'r',label='abs')
ax2.plot(f, np.real(fy[0:int(N//2)]),'b', label='real')
ax2.plot(f, np.imag(fy[0:int(N//2)]),'g', label='imaginary')
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('Amplitude')
ax2.legend()
plt.show()
