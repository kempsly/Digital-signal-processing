"""
    convert text message to bits, then add noise and write to file

"""

import numpy as np


def addNoise(p, N) :
    sig = p + 0.2*np.random.randn(N)
    sig = np.round(sig, 2)

    return sig

def createSignal(message) :
    pulse0 = np.ones( 10 )
    pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )

    N = pulse1.size
    
    # for each character in string
    #   convert character to ASCII value in binary
    #   for each bit
    #     create pulse
    #     append to outSignal

    outSignal = np.array([])

    for letter in message :
        bitString = bin( ord(letter) )
        # https://stackoverflow.com/questions/1395356/how-can-i-make-bin30-return-00011110-instead-of-0b11110
        bitString = bitString[2:].zfill(8)

        for bit in bitString :
            if bit == '0' :
                outSignal = np.append( outSignal, addNoise(pulse0, N) )
            else :
                outSignal = np.append( outSignal, addNoise(pulse1, N) )

    return outSignal


#####  main  #####
message = "Want to see something cool?  Create and run a Python script with just the line 'import antigravity' without quotes."

out = createSignal(message)
# https://stackoverflow.com/questions/6081008/dump-a-numpy-array-into-a-csv-file
out.tofile("data-communications.csv", sep=',', format='%.2f')
