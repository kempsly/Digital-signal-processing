"""
    show how lowpass and highpass filters work
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import os 


# Create the subfolder if it doesn't exist
subfolder = 'time_domain_plot_analysis'
os.makedirs(subfolder, exist_ok=True)


plt.figure(figsize=(12, 8))
showSubplots = True

t1 = np.arange(0, 1, 1/40)
t2 = np.arange(0, 1, 1/1000)

np.set_printoptions(precision=3, suppress=True)

###
if showSubplots :
    plt.subplot(5, 1, 1)

y1 = np.sin(2 * np.pi * t1)
plt.plot(t1, y1, 'o')

y2 = np.sin(2 * np.pi * t2)
plt.plot(t2, y2)
plt.title("1 Hz signal sampled 40 times/second")


###
if showSubplots :
    plt.subplot(5, 1, 2)
else :
    plt.figure()

y3 = np.sin(2 * np.pi * 10 * t1)
plt.plot(t1, y3, 'o')

y4 = np.sin(2 * np.pi * 10 * t2)
plt.plot(t2, y4)
plt.title("10 Hz signal sampled 40 times/second")


###
if showSubplots :
    plt.subplot(5, 1, 3)
else :
    plt.figure()

y5 = y1 + y3
plt.plot(t1, y5, 'o')

y6 = y2 + y4
plt.plot(t2, y6)
plt.title("1 Hz + 10 Hz signal")


###
if showSubplots :
    plt.subplot(5, 1, 4)
else :
    plt.figure()

lpf = np.ones(4)/4
out = np.convolve(y5, lpf)

t3 = np.arange(0, 1, 1/43)

plt.plot(t3, out, 'o')
plt.title("1 Hz + 10 Hz after 4-point moving avg filter")


###
if showSubplots :
    plt.subplot(5, 1, 5)
else :
    plt.figure()

hpf = np.array([1, -1])
out = np.convolve(y5, hpf)

t3 = np.arange(0, 1, 1/41)
plt.plot(t3, out, 'o')
plt.title("1 Hz + 10 Hz after highpass filter")


plt.tight_layout()
plt.show()

# Save the plot in the subfolder
filename = os.path.join(subfolder, 'plot_time_domain_anal_ex.png')
plt.savefig(filename)