''' file name : laplacian.py

Description : This sample shows how to find laplacian of an image

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/laplace_operator/laplace_operator.html

Level : Beginner

Benefits : Learn to find laplacian of an image

Usage : python laplacian.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

kernel_size = 3
scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('messi5.jpg')
img = cv2.GaussianBlur(img,(3,3),0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_lap = cv2.Laplacian(gray,ddepth,ksize = kernel_size,scale = scale,delta = delta)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow('laplacian',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
