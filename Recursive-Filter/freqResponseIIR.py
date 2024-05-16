"""
    design IIR filter and plot its frequency response
"""

from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

def getOutput(x, N) :
    #  y[n] = sqrt(2)/2*y[n-1] - 0.25*y[n-2] + x[n] + sqrt(2)*x[n-1] + x[n-2]
    y = np.zeros(N + 2)
    i = 0
    y[i] = x[i]
    i += 1
    y[i] = np.sqrt(2)/2*y[i-1] + x[i] + np.sqrt(2)*x[i-1]
    
    i = 2
    while i < N :
        y[i] = np.sqrt(2)/2*y[i-1] - 0.25*y[i-2] + x[i] + np.sqrt(2)*x[i-1] + x[i-2]
        i += 1

    return y


def plotOutput(y, f) :
    plt.plot(y)
    plt.title("output for f = %.1fHz" % f)
    plt.show()


##########  main  ##########
# filter coefficients
# X(z) coefficients
b = np.array([1, np.sqrt(2), 1])
# Y(z) coefficients
a = np.array([1, -2*np.cos(np.pi/4), 0.25])

x, y = freqz(b, a) 

plt.figure()
plt.plot(x, abs(y))
plt.xlabel("radians/sample")
plt.title("frequency response")
plt.grid()
plt.show()

# generate test signals
N  = 1000
fs = N

n = np.arange(N)
f1 = 4
x1 = np.cos(2*np.pi*f1*n/N)
y = getOutput(x1, N)
plotOutput(y, f1)


f2 = 3*fs/8 
x2 = np.cos(2*np.pi*f2*n/N)
y = getOutput(x2, N)
plotOutput(y, f2)

