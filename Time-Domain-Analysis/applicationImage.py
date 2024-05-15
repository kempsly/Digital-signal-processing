"""
  This module is about applying filters to images

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def applyFilter(myFilter, data) :
    # how to append properly
    #   http://akuederle.com/create-numpy-array-with-for-loop
    filLength = myFilter.size
    rows, cols = data.shape

    out = np.empty((0, cols + filLength - 1))
    for line in data :
        result = np.convolve(line, myFilter)
        out = np.append(out, [result], axis=0)
    return out


def edgeDetection(name) :
    im = plt.imread(name)
    plt.gray()  # needed to get correct color map

    ## highpass filter for edge detection
    hpf = np.array([1, -1])

    # plot original
    plt.imshow(im)
    plt.title("original")
    plt.show()

    # apply convolution both directions
    outPicHorz = applyFilter(hpf, im)
    outPic = applyFilter(hpf, outPicHorz.T)
    plt.imshow(outPic.T)
    plt.title("highpass filter both directions")
    plt.show()

    # apply convolution horizontally
    outPic = applyFilter(hpf, im)
    plt.imshow(outPic)
    plt.title("highpass filter horizontally")
    plt.show()

    # apply convolution vertically
    outPic = applyFilter(hpf, im.T)
    plt.imshow(outPic.T)
    plt.title("highpass filter vertically")

    plt.show()


def noiseRemoval(name) :
    im = plt.imread(name)
    plt.gray()  # needed to get correct color map

    # plot original
    plt.imshow(im)
    plt.title("original")
    plt.show()

    ## lowpass filter for blurring (noise removal)
    length = 10
    lpf = np.ones(length)/length
    
    outPic = applyFilter(lpf, im)
    plt.imshow(outPic)
    plt.title("noise removal using LPF")
    plt.show()

    # median filter for noise removal
    #   https://blog.kyleingraham.com/2017/02/04/salt-pepper-noise-and-median-filters-part-ii-the-code/
    
    outMed = ndimage.median_filter(im, 5)
    plt.imshow(outMed)
    plt.title("noise removal using median filter")
    
    plt.show()


###########  main  #######################################
n = "darinGray.jpg"

edgeDetection(n)

n = "darinGrayNoise.jpg"
noiseRemoval(n)

