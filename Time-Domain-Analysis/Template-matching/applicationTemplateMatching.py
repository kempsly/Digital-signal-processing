"""
    read two images, one large and one small, and use normalized cross-correlation
    to find the location of the smaller image in the larger image
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from skimage.feature import match_template

def display(image, t) :
    plt.figure()
    plt.imshow(image)
    plt.title(t)
    plt.gray()
    plt.show()


def rgb2gray(rgb):
    # from https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
    #  ITU-R 601-2 luma transform
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def getIndex( x ) :
    # from https://stackoverflow.com/questions/11332205/find-row-or-column-containing-maximum-value-in-numpy-array
    index = np.argmax(x) 
    return np.unravel_index(index, x.shape)

def findImage(mainImage, template) :
    big = plt.imread(mainImage)
    bigGray  = rgb2gray(big)
    display(bigGray, "large image to search")
    
    small = plt.imread(template)
    smallGray  = rgb2gray(small)
    display(smallGray, "image to search for")
    
    c = match_template(bigGray, smallGray)
    ri, ci = getIndex(c)
    
    rdim, cdim = smallGray.shape
    mask = np.zeros( (rdim, cdim) )
    bigGray[ri:ri+rdim, ci:ci+cdim] = mask
    display(bigGray, "location of template")

    return (ri, ci)
    
#############  main  #############
if __name__ == "__main__":
    mainImage = "C:\\Users\\Kempsly\\Desktop\\Digital-signal-processing\\Time-Domain-Analysis\\Template-matching\\ERBwideColorSmall.jpg"
    # "ERBwideColorSmall.jpg"
    template = "C:\\Users\\Kempsly\\Desktop\\Digital-signal-processing\\Time-Domain-Analysis\\Template-matching\\ERBwideColorSmall.jpg"
    # "ERBwideTemplate.jpg"
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))
