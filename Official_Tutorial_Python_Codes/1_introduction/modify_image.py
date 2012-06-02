''' file name : modify_image.py

Description : This sample shows how to convert a color image to grayscale and save it into disk

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/introduction/load_save_image/load_save_image.html

Level : Beginner

Benefits : Learn 1) to convert RGB image to grayscale, 2) save image to disk

Usage : python modify_image.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np
import sys

image = cv2.imread('lena.jpg') # change image name as you need or give sys.argv[1] to read from command line
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert image to gray

cv2.imwrite('gray_image.jpg',gray_image)   # saves gray image to disk

cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
