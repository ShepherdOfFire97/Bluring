"""
This program first creates an nxn gaussian kernel, then blurs the image to be blurred using the convulution.
the final blurred image is saved as conv_blur.jpg
"""

__author__ = "Varun Nair"

import numpy as np
from scipy import signal
from scipy import stats as st
import cv2
import datetime


def gausk(Kl, r):
    """
    This fucntion creates an nxn matrix that will be used to blur the image
    :param Kl: n for an nxn kernel
    :param r: range of spread used for creating kernel
    :return: returns an nxn gaussian kernel that can be directly deployed to blur images
    """
    X = np.linspace(-r, r, Kl+1)
    k1d = np.diff(st.norm.cdf(X))  # creates col vec of random values; k1d = kernel1D
    k2d = np.outer(k1d, k1d)  # creates a matrix as an outer product of k1d; k2d = kernel2D
    return k2d/k2d.sum()


def conv_blur(img,Kl,sig):
    """
    This function uses scipy.signal.convolve to convolute image
    :param img: image to be blurred
    :param Kl: length of edge of the gaussian kernel (n in nxn)
    :param sig: (standard deviation)
    :return:
    """
    GK = gausk(Kl, sig)
    img_blur = signal.convolve2d(img, GK, mode='same')
    return img_blur



if __name__ == "__main__":
    img = cv2.imread("/Users/varunvasudevan/Desktop/Purdue/5_Fin/Research/Wavelet Denoising/DSC7.JPG", 0)
    blur = conv_blur(img,23,3)
    cv2.imwrite("conv_blur.jpg", blur)


