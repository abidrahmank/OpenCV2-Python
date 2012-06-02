''' file name : linear_filter.py

Description : This sample shows how to create a linear filter and apply convolution

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/filter_2d/filter_2d.html#filter-2d

Level : Beginner

Benefits : Learn to 1) create a kernel and 2) apply convolution

Usage : python linear_filter.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

img = cv2.imread('home.jpg')

anchor = (-1,-1)
delta = 0
ddepth = -1

ind = 0

while(True):
    
    cv2.imshow('image',img)
    k = cv2.waitKey(500)

    if k==27:
        break

    kernel_size = 3 + 2*( ind%5 )   # trying for kernel sizes [3,5,7,9,11]
    kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)

    cv2.filter2D(img,ddepth,kernel,img,anchor,delta,cv2.BORDER_DEFAULT)
    
    ind = ind+1

cv2.destroyAllWindows()
