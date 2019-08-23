"""This program uses for loops to create a blurred image using the box blur algorithm."""

import numpy as np
import cv2

def box_blur(img_path, n):
    """
    Method to blur image using box blur algorithm
    :param img_path: The image path
    :param n: The size of the kernel
    :return: Blurred image
    """
    img = cv2.imread(img_path,0)
    dim = img.shape
    x = (dim[0]-(n-1))
    y = (dim[1]-(n-1))
    dim_new = (x, y)
    img_copy = np.zeros(dim_new)
    for i in range(10, x):
        for j in range(10, y):
            for z in range(0, n):
                for k in range(0, n):
                    img_copy[i][j] += float(img[i+z][j+k])
            img_copy[i][j] = (img_copy[i][j])/(n**2)
    print (img)
    cv2.imwrite("box_blur.jpg", img_copy)
    return (img_copy)

if __name__ == "__main__":
    box_blur("orig.jpg",3)
