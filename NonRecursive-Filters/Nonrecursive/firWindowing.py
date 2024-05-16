"""
    generate FIR coefficients for ideal lowpass filter
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def genFilter(fs, fc, taps) :
    w = 2*np.pi*fc/fs
    
    # centered at zero
    n = np.arange(-(taps-1)//2, (taps-1)//2 + 1, 1)
    h = np.zeros(taps)
    
    #  the impulse response will be symmetric, so only
    #  need to calculate first half
    print("filter coefficients, taps = %d" % taps)
    i = 0
    while i < taps//2 :
        h[i] = np.sin(n[i] * w)/(np.pi * n[i])
        end = taps - i - 1
        h[end] = h[i]
        print("h[%2d] = %9f, h[%2d] = %9f" % (i, h[i], end, h[end]))
        i += 1
    
    h[i] = w/np.pi
    print("h[%2d] = %9f\n" % (i, h[i]))
    
    plt.stem(h, use_line_collection=True)
    plt.title("filter coefficients, taps = %d" % taps)
    plt.show()
    
    return h

def plotFreqResponse(h, taps, fs) :
    freq, response = signal.freqz(h)
    #  https://stackoverflow.com/questions/29620694/matlab-freqz-function-in-python
    f = fs * freq / (2 * np.pi)

    plt.plot(f, np.abs(response))
    plt.title("frequency response, taps = %d" % taps)
    plt.grid()
    plt.show()

def applyWindows(h, taps, fs) :
    M = taps - 1

    # centered at zero
    n = np.arange(-M//2, M//2 + 1, 1)

    # von Hann
    w = 0.5 + 0.5*np.cos(2*np.pi*n/M)
    plt.plot(n, w)
    hann = h*w

    # Hamming
    w = 0.54 + 0.46*np.cos(2*np.pi*n/M)
    plt.plot(n, w, 'r')
    hamming = h*w
    plt.title("Windows, taps = %d" % taps)
    plt.legend(["von Hann", "Hamming"])
    plt.show()

    plt.stem(hamming, use_line_collection=True)
    plt.title("filter coefficients after Hamming, taps = %d" % taps)
    plt.show()

    #  plot frequency responses
    #  log scale
    freq, response = signal.freqz(hann)
    #  https://stackoverflow.com/questions/29620694/matlab-freqz-function-in-python
    f = fs * freq / (2 * np.pi)
    plt.plot(f, np.abs(response))

    freq, response = signal.freqz(hamming)
    plt.plot(f, np.abs(response))
    plt.title("frequency responses after apply window, taps = %d" % taps)
    plt.legend(["von Hann", "Hamming"])
    plt.grid()
    plt.show()

    #  plot frequency responses
    #  log scale
    freq, response = signal.freqz(hann)
    f = fs * freq / (2 * np.pi)
    #plt.plot(f, np.abs(response))
    plt.plot(f, 20 * np.log10(np.abs(response)) )

    freq, response = signal.freqz(hamming)
    f = fs * freq / (2 * np.pi)
    #plt.plot(f, np.abs(response))
    plt.plot(f, 20 * np.log10(np.abs(response)), 'r')

    plt.xlabel("Hertz")
    plt.ylabel("db")
    plt.title("frequency responses after apply window, taps = %d" % taps)
    plt.legend(["von Hann", "Hamming"])
    plt.grid()
    plt.show()



###################  main  ###################
#  trying to replicate values in example at 
#    http://www.labbookpages.co.uk/audio/firWindowing.html
fs = 2000
fc = 460
    
taps = 11
h = genFilter(fs, fc, taps)
plotFreqResponse(h, taps, fs)

taps = 99
h = genFilter(fs, fc, taps)
plotFreqResponse(h, taps, fs)

##########################################
#  apply windows to filter coefficients
taps = 21

h = genFilter(fs, fc, taps)
plotFreqResponse(h, taps, fs)
applyWindows(h, taps, fs)

