''' file name : smoothing.py

Description : This sample shows how to smooth image using various filters

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/gausian_median_blur_bilateral_filter/gausian_median_blur_bilateral_filter.html#smoothing

Level : Beginner

Benefits : Learn to use 1) Blur, 2) GaussianBlur, 3) MedianBlur, 4) BilateralFilter and differences between them

Usage : python smoothing.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

DELAY_CAPTION = 1500;
DELAY_BLUR = 500;

img = cv2.imread('lena.jpg')

for i in xrange(1,31,2):
    blur = cv2.blur(img,(i,i))
    string = 'blur : kernel size - '+str(i)
    cv2.putText(blur,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
    cv2.imshow('Blur',blur)
    cv2.waitKey(DELAY_BLUR)

for i in xrange(1,31,2):
    gaussian_blur = cv2.GaussianBlur(img,(i,i),0)
    string = 'guassian_blur : kernel size - '+str(i)
    cv2.putText(gaussian_blur,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
    cv2.imshow('Blur',gaussian_blur)
    cv2.waitKey(DELAY_BLUR)

cv2.waitKey(DELAY_CAPTION)

for i in xrange(1,31,2):
    median_blur = cv2.medianBlur(img,i)
    string = 'median_blur : kernel size - '+str(i)
    cv2.putText(median_blur,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
    cv2.imshow('Blur',median_blur)
    cv2.waitKey(DELAY_BLUR)

cv2.waitKey(DELAY_CAPTION)

for i in xrange(1,31,2):       # Remember, bilateral is a bit slow, so as value go higher, it takes long time 
    bilateral_blur = cv2.bilateralFilter(img,i, i*2,i/2)
    string = 'bilateral_blur : kernel size - '+str(i)
    cv2.putText(bilateral_blur,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
    cv2.imshow('Blur',bilateral_blur)
    cv2.waitKey(DELAY_BLUR)

cv2.waitKey(DELAY_CAPTION)
cv2.destroyAllWindows()

## For more info about this , visit: http://opencvpython.blogspot.com/2012/06/smoothing-techniques-in-opencv.html
