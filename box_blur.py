import numpy as np
import cv2
import datetime

n = 3
img = cv2.imread("/Users/varunvasudevan/Desktop/Purdue/5_Fin/Research/Wavelet Denoising/DSC6.JPG",0)
dim = img.shape
x = (dim[0]-(n-1))
y = (dim[1]-(n-1))
dim_new=(x,y)
img_copy = np.zeros(dim_new)
now = datetime.datetime.now()
for i in range(x):
    for j in range(y):
        for z in range (0, n):
            for k in range (0, n):
                img_copy[i][j] += float(img[i+z][j+k])
        #img_copy[i][j] = (float(img[i][j])+float(img[i][j+1])+float(img[i][j+2])+float(img[i][j+3])+float(img[i][j+4])+float(img[i+1][j])+float(img[i+1][j+1])+float(img[i+1][j+2])+float(img[i+1][j+3])+float(img[i+1][j+4])+float(img[i+2][j])+float(img[i+2][j+1])+float(img[i+2][j+2])+float(img[i+2][j+3])+float(img[i+2][j+4])+float(img[i+3][j])+float(img[i+3][j+1])+float(img[i+3][j+2])+float(img[i+3][j+3])+float(img[i+3][j+3])+float(img[i+3][j+4])+float(img[i+4][j])+float(img[i+4][j+1])+float(img[i+4][j+2])+float(img[i+4][j+3])+float(img[i+4][j+4]))
        img_copy[i][j] = (img_copy[i][j])/(n**2)
later = datetime.datetime.now()
print(img)
print(img_copy)
# print(im_dif)
cv2.imwrite("orig.jpg", img)
cv2.imwrite("blurred.jpg", img_copy)
print(x*y*(n**2))
print(c)
print(later-now)
print("done")

