"""
    Blind source separation refers to the process of separating mixed audio signals 
    into their original source components without any prior knowledge about the sources
    or the mixing process. In simpler terms, it's like unmixing a cocktail of sounds to 
    identify and isolate each individual sound source.

    Imagine you have two audio files, each containing a mix of different sounds. 
    Blind source separation would involve analyzing these mixed audio files to 
    identify the distinct sources contributing to the mixture and then separating 
    them to reconstruct the original, individual sounds.
"""


import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA


def plotSignal(s, title) :
    N = s.size
    plt.subplot(1,2,1)
    plt.plot(s)
    plt.title("time domain: %s" % title)
    plt.xticks(np.arange(0, N+1, 20000))
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

    plt.subplot(1,2,2)
    dft = np.fft.fft(s)
    plt.plot(abs(dft))
    plt.title("FFT: %s" % title)
    plt.xticks(np.arange(0, N+1, 20000))
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.show()


def unmixAudio(leftName, rightName) :
    x0, fs = sf.read(leftName)
    x1, fs = sf.read(rightName)
    
    #  separate with ICA
    unmixed = applyICA(x0, x1)

    # volume is low, so increase magnitude of signal values
    unmixed0 = 10*unmixed[:, 0]
    unmixed1 = 10*unmixed[:, 1]

    sf.write("unmixed0.wav", unmixed0, fs)
    sf.write("unmixed1.wav", unmixed1, fs)

    plotSignal(x0, "original x0")
    plotSignal(x1, "original x1")
    plotSignal(unmixed0, "unmixed x0")
    plotSignal(unmixed1, "unmixed x1")
    

def applyICA(x0, x1) :
    #  uses FastICA library
    #  https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html
    #
    # for ICA
    #   https://stats.stackexchange.com/questions/183890/why-are-we-using-ica

    #  create matrix with each column a source
    X = np.c_[x0, x1]
    ica = FastICA(n_components=2)

    return ica.fit_transform(X)  


###################  main  ###################
#  linear combination of signals
leftName = "darinSiren0.wav"
rightName = "darinSiren1.wav"
unmixAudio(leftName, rightName)
