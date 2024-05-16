"""
    use FFT to remove noise from audio file
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def displaySignal(signal, fs, N, f0, s) :
    plt.plot(signal)
    plt.title("%s, fs = %d" % (s, fs))
    
    xfft = np.fft.fft(signal)

    #n = np.arange(0, N)* f0  # use if we want the frequencies
    n = np.arange(N)  # use if we want the array indices
    plt.figure()
    plt.plot( n, abs(xfft) )
    plt.title("fft of %s, $f_0$ = %.3f" % (s, f0))
    #plt.ylim([0, 5])  # use to see that there are many small amplitude frequencies
    plt.xlabel("indices, not frequencies")
    plt.xticks(np.arange(0, N+1, 20000))
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

    plt.show()

def removeNoise(signal, fs, N, f0) :
    offset = 73000
    mid = N/2
    lowerBound = int(mid)-offset
    upperBound = int(mid)+offset + 1
    print("midpoint = %.1f, lower = %d, upper = %d" % (mid, lowerBound, upperBound))

    xfft = np.fft.fft(signal)
    xfft[lowerBound : upperBound] = 0

    cleaned = np.fft.ifft(xfft)

    return cleaned


##############  main  ##############
filename = "C:\\Users\\Kempsly\\Desktop\\Digital-signal-processing\\Discrete-Fourier-Transform\\FFT-Noise-Removal\\count12345Noise.wav"
# "count12345Noise.wav"
signal, fs = sf.read(filename)

N = signal.size
f0 = fs/N

# before removing noise
displaySignal(signal, fs, N, f0, "signal with noise") 

cleaned = removeNoise(signal, fs, N, f0) 
cleaned = cleaned.real
sf.write("C:\\Users\\Kempsly\\Desktop\\Digital-signal-processing\\Discrete-Fourier-Transform\\FFT-Noise-Removal\\count12345WithoutNoise.wav", cleaned, fs)
# sf.write("count12345WithoutNoise.wav", cleaned, fs)

# after removing noise
displaySignal(cleaned, fs, N, f0, "after noise removed") 

############
# let's look at the original audio before noise was added
filename = "C:\\Users\\Kempsly\\Desktop\\Digital-signal-processing\\Discrete-Fourier-Transform\\FFT-Noise-Removal\\count12345.wav"
# "count12345.wav"
signal, fs = sf.read(filename)

displaySignal(signal, fs, N, f0, "original signal") 

