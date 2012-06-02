''' file name : filter2d.py

Description : This sample shows how to filter/convolve an image with a kernel

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/core/mat-mask-operations/mat-mask-operations.html#the-filter2d-function

Level : Beginner

Benefits : Learn to convolve with cv2.filter2D function

Usage : python filter2d.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

img = cv2.imread('lena.jpg')

kernel = np.array([ [0,-1,0],
                    [-1,5,-1],
                    [0,-1,0] ],np.float32)   # kernel should be floating point type.

new_img = cv2.filter2D(img,-1,kernel)        # ddepth = -1, means destination image has depth same as input image.

cv2.imshow('img',img)
cv2.imshow('new',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
