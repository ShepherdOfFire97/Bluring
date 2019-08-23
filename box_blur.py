"""This program uses for loops to create a blurred image using the box blur algorithm."""

import numpy as np
import cv2
from scipy import signal


def box_blur(img_path, n):
    """
    Method to blur image using box blur algorithm
    :param img_path: The image path
    :param n: The size of the kernel
    :return: Blurred image
    """
    img = cv2.imread(img_path,0)
    K = np.ones((n, n))
    Kb = K/(n**2)
    img_blur = signal.convolve2d(img,Kb)
    cv2.imwrite("box_blur.jpg", img_blur)
    return img_blur

if __name__ == "__main__":
    box_blur("orig.jpg",17)
