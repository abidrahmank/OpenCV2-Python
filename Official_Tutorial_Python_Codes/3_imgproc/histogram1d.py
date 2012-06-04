''' file name : histogram1d.py

Description : This sample shows how to draw histogram for RGB color images

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/histograms/histogram_calculation/histogram_calculation.html

Level : Beginner

Benefits : Learn to use 1)cv2.calcHist(), 2)cv2.normalize and 3)cv2.polylines()

Usage : python histogram1d.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
h = np.zeros((300,256,3))                                    # image to draw histogram

bins = np.arange(256).reshape(256,1)                         # Number of bins, since 256 colors, we need 256 bins
color = [ (255,0,0),(0,255,0),(0,0,255) ]

for ch,col in enumerate(color):
    hist_item = cv2.calcHist([img],[ch],None,[256],[0,256])  # Calculates the histogram
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) # Normalize the value to fall below 255, to fit in image 'h'
    hist=np.int32(np.around(hist_item))                      
    pts = np.column_stack((bins,hist))                       # stack bins and hist, ie [[0,h0],[1,h1]....,[255,h255]]
    cv2.polylines(h,[pts],False,col)

h=np.flipud(h)                                               # You will need to flip the image vertically

cv2.imshow('colorhist',h)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Here, there is no need of splitting the image to color planes,since calcHist will do it itself.
# For more details, visit : http://opencvpython.blogspot.com/2012/04/drawing-histogram-in-opencv-python.html
