import numpy as np
import matplotlib.pyplot as plt
import os    
import time

# Create the subfolder if it doesn't exist
subfolder = 'sinusoid_plot'
os.makedirs(subfolder, exist_ok=True)

x = np.arange(0, 1, 0.001)
plt.figure()

plt.subplot(4, 1, 1)
y1 = 3 + 2*np.cos(2 * np.pi * x * 4)
plt.plot(x, y1)
plt.title("Sinusoidal Component 1")

plt.subplot(4, 1, 2)
y2 = 0 + 1*np.cos(2 * np.pi * 5 * x + np.pi/6)
plt.plot(x, y2)
plt.title("Sinusoidal Component 2")

plt.subplot(4, 1, 3)
y3 = -1 + 5*np.cos(2 * np.pi * 7 * x - np.pi/4)
plt.plot(x, y3)
plt.title("Sinusoidal Component 3")

plt.subplot(4, 1, 4)
y = y1 + y2 + y3 
plt.plot(x, y) 
plt.title("Combined Sinusoidal Plot")  # Title for the combined plot
plt.tight_layout()

plt.grid()
plt.show()

# Add a delay before saving the image
time.sleep(3)

# Save the plot in the subfolder
filename = os.path.join(subfolder, 'plot_sinusoid_1.png')
plt.savefig(filename)
