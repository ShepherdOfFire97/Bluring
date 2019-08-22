"""
This program first creates an nxn gaussian kernel, then blurs the image to be blurred using the convulution.
the final blurred image is saved as conv_blur.jpg
"""

__author__ = "Varun Nair"

import numpy as np
from scipy import signal
from scipy import stats as st
import cv2


def gausk(klen, r):
    """
    This function creates an nxn matrix that will be used to blur the image
    :param klen: n for an nxn kernel; klen = kernel length,
    :param r: range of spread used for creating kernel; r = symmetric range
    :return: returns an nxn gaussian kernel that can be directly deployed to blur images [numpy array]
    """
    x = np.linspace(-r, r, klen+1)
    k1d = np.diff(st.norm.cdf(x))  # creates col vec of random values; k1d = kernel1D
    k2d = np.outer(k1d, k1d)  # creates a matrix as an outer product of k1d; k2d = kernel2D
    return k2d/k2d.sum()  # creates gaussian kernel of nxn dimension


def conv_blur(img, klen, r):
    """
    This function uses scipy.signal.convolve2d to convolute image
    :param img: image to be blurred
    :param klen: length of edge of the gaussian kernel (n in nxn)
    :param r: symmetric range from line 14
    :return: blurred image [numpy array]
    """
    gk = gausk(klen, r)  # GK is the created gaussian kernel
    img_blur = signal.convolve2d(img, gk, mode='same')  # convolutes img and kernel w/o changing original img dim
    return img_blur


if __name__ == "__main__":
    image = cv2.imread("", 0)
    blur = conv_blur(image, 23, 3)
    cv2.imwrite("conv_blur.jpg", blur)


