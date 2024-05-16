"""
    shelving filter using IIR

"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def comparePlots(x, fs, N, y) :
    ## plot frequencies of original song
    xfft = abs(np.fft.fft(x))
    yfft = abs(np.fft.fft(y))

    if max(xfft) > max(yfft) :
        maxAmp = max(xfft) + 100
    else :
        maxAmp = max(yfft) + 100

    frequencies = np.arange(N)*fs/N
    plt.subplot(1, 2, 1)
    plt.plot( frequencies[0:N//4], xfft[0:N//4] )
    plt.title('original signal')
    plt.xlabel('Hz')
    plt.ylim([0, maxAmp])
    
    ## plot frequencies of filtered song
    plt.subplot(1, 2, 2)
    plt.plot( frequencies[0:N//4], yfft[0:N//4] )
    plt.title('filtered signal')
    plt.xlabel('Hz')
    plt.ylim([0, maxAmp])
    plt.show()
    

def applyShelvingFilter(inName, outName, g, fc) :
    x, fs = sf.read(inName)
    N = x.size
    
    # code based on 
    #   based on book DSP Filters (Electronics Cookbook Series) by Lane et al.
    w = 2*np.pi*fc/fs
    mu = 10**(g/20)
    gamma = ( 1 - 4/(1 + mu)*np.tan(w/2) ) / ( 1 + 4/(1 + mu)*np.tan(w/2) )
    alpha = (1 - gamma)/2
    
    u = np.zeros(N)
    y = np.zeros(N)
    
    # deal with values where n < 0 (or 1 in MATLAB syntax)
    u[0] = alpha*(x[0] + 0) + gamma*0
    y[0] = x[0] + (mu - 1)*u[0]
    
    for n in np.arange(1, N) :
        u[n] = alpha*(x[n] + x[n-1]) + gamma*u[n-1]
        y[n] = x[n] + (mu - 1)*u[n]
    
    comparePlots(x, fs, N, y)

    sf.write(outName, y, fs)


##########################  main  ##########################
inName = "song-Hold on a Sec.wav"
gain = -20    # a small change here can cause a large difference
cutoff = 300
outName = "shelvingOutput.wav"

applyShelvingFilter(inName, outName, gain, cutoff)
