"""
    produce DFT of signal; demonstrates spectral leakage
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


fs = 1024
t = np.arange(0, 1, 1/fs)

f1 = 20
f2 = 100
y1 = np.cos(2*np.pi*f1*t)
y2 = np.cos(2*np.pi*f2*t)
y =  y1 + y2

N = 500
f0 = fs/N

yPart = y[0:N]

plt.title("fs = %d, N = %d" % (fs, N))
plt.plot(t, y)

dft = np.fft.fft(yPart)

plt.figure()
plt.title("DFT results, f0 = %.3f" % f0)
n = np.arange(0, N)* f0
plt.stem( n, abs(dft), use_line_collection = True )

#  zoom in
plt.figure()
plt.title("zoom in around 20Hz")
plt.stem( n[0:15], abs(dft[0:15]), use_line_collection = True )

##############
#  apply Hamming window
hamming = signal.hamming(len(yPart))
newY = hamming*yPart
plt.figure()
plt.plot(t[0:N], newY)
plt.title("windowed signal")

plt.figure()
dft2 = np.fft.fft(newY)
plt.title("after applying Hamming window")
plt.stem( n, abs(dft2), use_line_collection = True )

#  zoom in
plt.figure()
plt.title("zoom in around 20Hz")
plt.stem( n[0:15], abs(dft2[0:15]), use_line_collection = True )

plt.tight_layout()
plt.show()

