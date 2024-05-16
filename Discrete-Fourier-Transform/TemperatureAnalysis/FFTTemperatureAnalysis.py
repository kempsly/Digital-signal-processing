"""
    Analysis of Temperature Data using the FFT

    instead of thinking of things in terms of seconds,
    think of them in terms of days

    one sample/hour, so
    fs = 24 samples/day
"""

import numpy as np
import matplotlib.pyplot as plt

def getData(fn) :
    data = np.genfromtxt(fn, dtype=str, delimiter=',', skip_header=1, usecols=[13])
    
    temps = []
    for t in data :
        t = t.replace('"', '')
        temps.append( float(t) )
    temps = np.asarray(temps)

    N = len(temps)
    return temps, N


def analysis(temps, tfft, N) :
    fs = 24      # samples per day
    print("fs = %d samples/day" % fs)
    
    f0 = fs/N
    print("f0 = %.4f cycles/day" % f0)
    
    # get the indices of the 3 largest magnitudes
    # https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
    top = 3
    mags = abs(tfft)
    idx = (-mags[0:N//2]).argsort()[:top]

    print()

    print("the top %d FFT values are at indices " % top, end = "")
    for i in range(top-1) :
        print("%d, " % idx[i], end = "")

    print("and %d\n" % (idx[top-1]))

    print("T[%4d] = the average temperature of %.3f degrees" % (idx[0], mags[0]/N) )
    print("average temperature calculated directly = %.3f" % (np.sum(temps)/N))
    print()

    print("T[%4d] = %.5f cycles/day" % (idx[1], f0*idx[1]) , end="")
    # cycles/day * 365 days/year = cycles/year
    print(" = %.5f cycles/year" % (f0*idx[1]*365) )
    print("          This is the seasonal trend." % (f0*idx[1]) )

    print("T[%4d] = %.5f cycles/day" % (idx[2], f0*idx[2]) , end="")
    print(" = %.5f cycles/year" % (f0*idx[2]*365) )
    print("          This is the daily trend." % (f0*idx[2]/365) )


def plotTemps(t, tfft, N) :
    plt.plot(t[0:24], '.-')
    plt.xlabel("hours")
    plt.title("first day")

    plt.figure()
    plt.plot(7*np.arange(0, 1, 1/(24*7)), t[0:24*7], '.-')
    plt.xlabel("days")
    plt.title("first week")

    plt.figure()
    r = 365*np.arange(0, 1, 1/(24*365))
    plt.plot(r[0:-1], t)
    plt.xlabel("days")
    plt.title("first 365 days")

    plt.figure()
    plt.plot( abs(tfft[0:N//2]) )
    plt.title("FFT")
    
    plt.figure()
    plt.plot( np.log(abs(tfft[0:N//2])) )
    plt.title("FFT (log scale)")
    
    plt.figure()
    numDays = 366
    plt.stem(abs(tfft[0:numDays]), use_line_collection=True)
    plt.title("FFT (first %d values)" % numDays)

    plt.show()


##################  main  ##################
# data from https://www.ncdc.noaa.gov/cdo-web/datatools/findstation
fn = "C:\\Users\\Kempsly\\Desktop\\Digital-signal-processing\\Discrete-Fourier-Transform\\TemperatureAnalysis\\weather.csv"
# "weather.csv"
temps, N = getData(fn)

tfft = np.fft.fft(temps)

analysis(temps, tfft, N)
plotTemps(temps, tfft, N)
