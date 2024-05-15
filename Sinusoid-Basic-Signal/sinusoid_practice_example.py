# Import statements 
import numpy as np          
import matplotlib.pyplot as plt 
import os 

"""Creating a plot to determine the underline signal
"""

# Create the subfolder if it doesn't exist
subfolder = 'sinusoid_plot'
os.makedirs(subfolder, exist_ok=True)

X = np.arange(0, 0.5, 0.001)

A0 = 1
A1 = 3
# Setting the Frequency
f = 5
peakTime = 0.3
# Defining phase shift 
phase = 2 * np.pi * f * peakTime

y = A0 + A1 * np.cos(2 * np.pi * f * X- phase)

plt.plot(X, y)
plt.grid()

plt.xticks(np.arange(0, 0.55, 0.05))
plt.xlabel("Times(seconds)")

plt.show()

# Save the plot in the subfolder
filename = os.path.join(subfolder, 'plot_sinusoid_practice.png')
plt.savefig(filename)