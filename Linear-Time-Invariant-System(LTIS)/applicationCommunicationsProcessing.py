"""
    use matching filter to recognize pulses

"""

import numpy as np

pulse0 = np.ones( 10 )
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
N = pulse0.size

message = np.genfromtxt("data-communications.csv", delimiter=',')
cols = message.size

bits = ""
i = 0
while i < cols :
    sig = message[i:i+10]

    cos0 = abs( pulse0.dot(sig) )/( np.linalg.norm(pulse0)*np.linalg.norm(sig) )
    cos1 = abs( pulse1.dot(sig) )/( np.linalg.norm(pulse1)*np.linalg.norm(sig) )

    if cos0 > cos1 :
        bits += '0'
    else :
        bits += '1'
    i += 10

#print( bits )

bitsSize = len(bits)

outString = ""
bitCount = 1
i = 0
while i < bitsSize :
    bitPattern = bits[i:i+8]
    decAscii = int(bitPattern, 2)
    character = chr(decAscii)
    outString += character

    i += 8

print(outString)
