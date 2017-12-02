'''
	Project - Lakshya Priyadarshi : official.18lakshya@gmail.com
	B.Tech 3rd Semester, Computer Science & Engineering

	Analysis of a binary system of neutron stars by mathematical modeling of gravitational wave signal
	Supervised by Dr Prof Rajesh Nayak, IISER Kolkata under Gavitational Waves Workshop at NSSC, IIT Kharagpur

'''

import numpy as np
import matplotlib.pyplot as plt

# Geometrized Solar Mass (geometrical units)
Ms=4.92549095e-6

# Conversion factor for parsec unit
pc=1.0292712503e8

# Mass of first neutron star / black hole, expressed in solar mass
m1=35.000000000000000000000000000000000000

# Mass of second neutron star / black hole, expressed in solar mass
m2=30.000000000000000000000000000000000000

# Mass of individual neutron star / black hole expressed in seconds
m1=m1*Ms
m2=m2*Ms

# Luminosity distance, expressed in mega parsec
D=400*1e6
D=D*pc

# Initial phase angle of gravitational wave
phi0=0.0

# Net mass of neutron star / black hole binary system
M= m1+m2

# Reduced mass of neutron star / black hole binary system 
mu = m1*m2/M

# Chirp mass of binary system
Mc = (mu**(3.0/5.0)) * (M**(2.0/5.0))

print("chirp mass", Mc/Ms, "Ms")

# Initial frequency of oscillations
f0 = 20.0000000000000000000000000000

t1= 256.0 *((np.pi*f0)**(8.0/3.0)) *(Mc**(5.0/3.0))

# Coalescence Time, approximation breaks down 
tc= 5.0 / t1

# Differential terms
print("Chirp Time", tc, "Sec")
sps = 1024.0*2
dt = 1.0/sps
T= 1.0
df=1.0/T;

N=int(sps*T)
ff=np.arange(0,N/2)*df
t=np.arange(0.0, tc, dt)

# Instantaneous frequency evolution of Gravitational Waves
ft= ((Mc*f0**9.0)**(1.0/8.0))/(((Mc*f0)**(1.0/3.0) - 256.0/5* f0**(3.0)* (Mc**2) * (np.pi**(8.0/3))*t)**(3.0/8))

ph=np.cumsum(2*np.pi*ft*dt)

# Time- variant phase angle function
phi= phi0- 2.0 *( 1.0/256*(np.pi*Mc*f0)**(-8.0/3)  - t/5/Mc)**(5.0/8)

# Time-variant amplitude function of gravitational wave
amplitude=4.0*(Mc**(5.0/3))*(np.pi**(2.0/3))*ft**(2.0/3.0)/D

# Linear combination (superposition) of polarizations h+ and h-
# Time variant signal (function) for observed gravitational wave
h=amplitude*np.cos(phi)

hf=np.fft.fft(h);
hf=np.copy(hf[0:N/2])

# Plot phase angle vs time
plt.figure()
plt.plot(t, phi)
plt.xlabel('Time')
plt.ylabel('Phase')
plt.show()

# Plot frequency vs time
plt.plot(t, ft)
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()

# Plot amplitude vs time
plt.figure()
plt.plot(t, A)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# Plot signal vs time
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(t,h)
ax1.set_xlabel('Time')
ax1.set_ylabel('signal')
ax2.loglog(ff,np.abs(hf))
plt.show()
