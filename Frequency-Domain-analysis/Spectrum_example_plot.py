"""
    produce DFT of signal
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1024
t = np.arange(0, 1, 1/fs)
N = 512

f1 = 20
f2 = 100
y1 = 5 * np.cos(2*np.pi*f1*t)
y2 = np.cos(2*np.pi*f2*t)
y =  y1 + y2

plt.title("fs = %d, N = %d" % (fs, N))
plt.plot(t, y)

dft = np.fft.fft(y[0:N])

plt.figure()
plt.title("DFT results")
n = np.arange(0, N)* fs/N
plt.stem( n, abs(dft[0:N]), use_line_collection=True )
plt.title("N = %d" % N)

#  zoom in
plt.figure()
plt.title("zoom in around 20Hz")
plt.stem( n[0:15], abs(dft[0:15]), use_line_collection=True )

plt.tight_layout()
plt.show()

