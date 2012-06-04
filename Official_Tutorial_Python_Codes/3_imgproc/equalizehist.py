''' file name : equalizehist.py

Description : This sample shows how to equalize histogram

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/histograms/histogram_equalization/histogram_equalization.html

Level : Beginner

Benefits : Learn to use cv2.equalizeHist()

Usage : python equalizehist.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(gray)    # Remember histogram equalization works only for grayscale images

cv2.imshow('src',gray)
cv2.imshow('equ',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
