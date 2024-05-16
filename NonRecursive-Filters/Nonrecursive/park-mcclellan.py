import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def filtCoeff(fs, numtaps, fpass, fstop) :
    #  example
    #    passband   = 0-300 Hz
    #    transition = 300-400Hz
    #    stopband   = 400-500 Hz
    #  bands = np.array([0, 300, 400, 500])
    bands = np.array([0, fpass, fstop, 500])

    # gain for the passband and stopband regions
    desired = np.array([1, 0])

    coeff = signal.remez(numtaps, bands, desired, Hz = fs)
    freq, response = signal.freqz(coeff)

    plt.plot(np.abs(response))
    plt.grid()
    plt.title("taps = %d, fpass = %d, fstop = %d" %(numtaps, fpass, fstop))
    plt.show()
    
    return coeff

 
def applyFilter(x, h) :
    y = np.convolve(x, h)
    
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(x)
    plt.title("original signal: 15Hz + 450Hz")
    
    plt.subplot(2, 1, 2)
    plt.plot(y[0: x.size])
    plt.title("filtered signal")
    
    plt.tight_layout()
    plt.show()
##################  main  ##################
fs = 1000

t = np.arange(0, 1, 1/fs)
x1 = np.cos(2*np.pi*15*t)
x2 = np.cos(2*np.pi*450*t)
x = x1 + x2

# input to function
#   sampling frequency
#   number of filter coefficients
#   cut-off for passband
#   cut-off for stopband
h = filtCoeff(fs, 5, 300, 400)
applyFilter(x, h)

h = filtCoeff(fs, 20, 300, 400)
applyFilter(x, h)

h = filtCoeff(fs, 100, 300, 400)
applyFilter(x, h)

h = filtCoeff(fs, 5, 300, 350)
applyFilter(x, h)

h = filtCoeff(fs, 20, 300, 350)
applyFilter(x, h)

h = filtCoeff(fs, 100, 300, 350)
applyFilter(x, h)

h = filtCoeff(fs, 5, 300, 325)
applyFilter(x, h)

h = filtCoeff(fs, 20, 300, 325)
applyFilter(x, h)

h = filtCoeff(fs, 100, 300, 325)
applyFilter(x, h)
