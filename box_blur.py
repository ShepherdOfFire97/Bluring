"""
This program uses the box blur algorithm to blur images. implemented using convolution. The blurred image is stored as
box_blur.jpg
"""

__author__ = "Varun Nair"

import numpy as np
from scipy import signal
import cv2


def box_blur(img_path, n):
    """
    Method to blur image using box blur algorithm by first creating and avg kernel
    :param img_path: The image path
    :param n: The size of the kernel
    :return: Blurred image
    """
    img = cv2.imread(img_path,0)
    K = np.ones((n, n))  # creates an nxn kernel with only 1's as entries
    Kb = K/(n**2)  # completes the averyaging in the box blur algo
    img_blur = signal.convolve2d(img,Kb,mode="same")  # convolves the avg kernel and the image
    cv2.imwrite("box_blur.jpg", img_blur)
    return img_blur

if __name__ == "__main__":
    box_blur("DSC7.JPG",11)
