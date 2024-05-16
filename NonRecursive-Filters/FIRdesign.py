"""
  design of lowpass and highpass filters using FIR filters
"""

import numpy as np
import matplotlib.pyplot as plt

def genData(fs) :
    Ts = 1/fs
    t = np.arange(0, 1, Ts)
    
    x1 = np.cos(2*np.pi*4*t)
    x2 = np.cos(2*np.pi*120*t)
    x3 = np.cos(2*np.pi*330*t)
    
    x = x1 + x2 + x3

    return x


def applyLowpass(x, fs, M) :
    fc = 50     # cut-off in Hertz
    ft = fc/fs  # normalized frequency
    
    # produce filter weights for lowpass filter
    h = np.zeros( taps )
    
    n = 0
    while n <= M :
        #  from http://www.labbookpages.co.uk/audio/firWindowing.html
        if n == M/2 :
            h[n] = 2*ft
        else :
            h[n] = np.sin(2*np.pi*ft*(n - M/2)) / (np.pi*(n - M/2))
        n += 1
    
    y = np.convolve(x, h)
    
    plt.figure
    plt.subplot(3, 1, 1) 
    plt.plot(x)
    plt.title("original signal")
    
    plt.subplot(3, 1, 2) 
    n = np.arange(0, 2000)
    x1 = np.cos(2*np.pi*4*n/fs)
    plt.plot(n, x1)
    plt.title("pure 4 Hz signal")
    
    plt.subplot(3, 1, 3) 
    plt.plot( np.arange(0, y.size), y)
    plt.title("application of lowpass filter")
    plt.tight_layout()
    plt.show()


def applyHighpass(x, fs, M) :
    fc = 280    # cut-off in Hertz
    ft = fc/fs  # normalized frequency
    
    # produce filter weights for highpass filter
    h = np.zeros( taps )
    
    n = 0
    while n <= M :
        #  from http://www.labbookpages.co.uk/audio/firWindowing.html
        if n == M/2 :
            h[n] = 1 - 2*ft
        else :
            h[n] = -np.sin(2*np.pi*ft*(n - M/2)) / (np.pi*(n - M/2))
    
        n += 1
    
    y = np.convolve(x, h)
    
    plt.figure(2)
    plt.subplot(3, 1, 1) 
    n = np.arange(0, 100)
    plt.plot(n, x[0:100])
    plt.title("original signal (zoomed in)")
    
    plt.subplot(3, 1, 2) 
    x3 = np.cos(2*np.pi*330*n/fs)
    plt.plot(n, x3[0:100])
    plt.title("pure 330 Hz signal")
    
    plt.subplot(3, 1, 3) 
    plt.plot( n, y[0:100])
    plt.title("application of highpass filter")
    plt.tight_layout()
    plt.show()


###################  main  ###################
fs = 2000
Ts = 1/fs
t = np.arange(0, 1, 1/Ts)
x = genData(fs)

# length of filter
taps = 21
M = taps - 1

applyLowpass(x, fs, M)
applyHighpass(x, fs, M)

