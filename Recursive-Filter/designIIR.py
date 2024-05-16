
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def myFilter(x, N) :
    # y[n] =  -0.81y[n-2] + 0.1x[n] - 0.1x[n-2]
    y = np.zeros(N)
    
    y[0] = 0 + 0.1*x[0] - 0  # y[-2] = x[-2] = 0
    y[1] = 0 + 0.1*x[1] - 0  # y[-1] = x[-1] = 0
    
    n = 2
    while n < fs :
        y[n] = -0.81*y[n-2] + 0.1*x[n] - 0.1*x[n-2]
        n += 1

    return y

def findY(x, N, title, printRange) :
    y = myFilter(x, N)
    
    plt.figure()
    plt.plot(y[0:printRange])
    plt.title("output of filter, input = %s" % title)
    plt.show()

###########  main  ###########
fs = 1000
t = np.arange(0, 1, 1/fs)
N = t.size


# H(z) = B(z)/A(z)
b = np.array([1, 0, -1])
a = np.array([1, 0,  0.81])

plt.figure()
#                   X, Y
x, y = signal.freqz(b, a)
n = fs*x/(2*np.pi)
plt.plot(n, abs(y))
plt.title("Original Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.show()

b = np.array([0.1, 0, -0.1])
a = np.array([1, 0,  0.81])

plt.figure()
#                   X, Y
x, y = signal.freqz(b, a)
n = fs*x/(2*np.pi)
plt.plot(n, abs(y))
plt.title("Original Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.show()


f1 = 7
x1 = np.cos(2 * np.pi * f1 * t)

printRange = 1000
plt.figure()
plt.plot(x1[0:printRange])
plt.title("input: x1 = %d Hz" % f1)
plt.show()

findY(x1, N, "%d Hz" % (f1), printRange) 

printRange = 200
f2 = 250
x2 = np.cos(2 * np.pi * f2 * t)
plt.figure()
plt.plot(x2[0:printRange])
plt.xlim([0, printRange])
plt.title("input: x2 = %d Hz" % f2)
plt.show()

findY(x2, N, "%d Hz" % (f2), printRange) 

