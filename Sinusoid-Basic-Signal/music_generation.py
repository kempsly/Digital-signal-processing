"""
    Music generation
    play Twinkle, Twinkle, Little Star
"""

import numpy as np
import soundfile as sf

fs = 8000

t = np.arange(0, 0.5, 1/fs)

notes = np.array([52, 52, 59, 59, 61, 61, 59, 59, 57, 57, 56, 56, 
                  54, 54, 56, 52, 59, 59, 57, 57, 56, 56, 54, 54])

length = notes.size
f = 440 * ( 2**((notes[0] - 49)/12) )
print("number = %d, frequency = %f" % (notes[0], f))
output = np.cos(2*np.pi*f*t)

i = 1
while i < length :
    f = 440 * ( 2**((notes[i] - 49)/12) )
    print("number = %d, frequency = %f" % (notes[i], f))
    x = np.cos(2*np.pi*f*t)
    output = np.concatenate([output, x])

    i += 1

sf.write("twinkle.wav", output, fs)

