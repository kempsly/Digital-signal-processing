import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


fs = 100
t = np.arange(0, 1, 1/fs)

y1 = np.cos(2 * np.pi * 4 * t)
y2 = np.cos(2 * np.pi * 7 * t)
y12 = y1 + y2

y = np.append(y1, y12)
y = np.append(y, y2)

# signal y consists of
#   4Hz for 1 sec, 4Hz and 7Hz for 1 sec, 7Hz for 1 sec

plt.plot(y)
plt.title("original signal")


dft = np.fft.fft(y)

N = 300
f0 = fs/N

n = np.arange(0, N) * f0

plt.figure()
plt.stem( n, abs(dft), use_line_collection=True )
plt.title("DFT")

plt.figure()
plt.stem( n[0:30], abs(dft[0:30]), use_line_collection=True )
plt.title("DFT (zoomed in)")


ws = 50
f, t, Sxx = signal.spectrogram(y, fs, nperseg=ws, noverlap=0)

plt.figure()
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (sec)')
plt.title("Spectrogram, window size = %d samples" % ws)

ws = 100
f, t, Sxx = signal.spectrogram(y, fs, nperseg=ws, noverlap=0)

plt.figure()
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (sec)')
plt.title("Spectrogram, window size = %d samples" % ws)

plt.show()
