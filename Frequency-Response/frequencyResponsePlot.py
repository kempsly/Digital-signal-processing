from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt


# filter coefficients
# y[n] = 2x[n] + 3x[n-1] + 2x[n-2]

# X(z) coefficients
b = np.array([2, 3, 2])
# Y(z) coefficients
a = np.array([1])

x, y = freqz(b, a) 

#  https://stackoverflow.com/questions/28216257/how-to-specify-the-size-of-a-figure-with-pweave-using-a-py-script

#' figure super wide
#+ fig = True, width = '1200'
plt.figure()
plt.plot(x, abs(y))
plt.xlabel("radians/sample")
plt.title("Frequency Response of y[n] = 2x[n] + 3x[n-1] + 2x[n-2]")
plt.xticks(np.arange(0, 3.3, .20))
plt.grid()
plt.show()

# generate values for hand plot
print("omega  H(omega)             |H(omega)|")
i = 0
while i < 5 :
    omega = i*np.pi/4
    f = 2 + 3*np.exp(-1j*omega) + 2*np.exp(-1j*2*omega)
    mag = np.sqrt(f.real**2 + f.imag**2)
    print("%.2f, %7.4f + j %7.4f,  mag = %.4f" % (omega, f.real, f.imag, mag))
    i += 1
