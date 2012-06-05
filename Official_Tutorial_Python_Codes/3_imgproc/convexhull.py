''' file name : convexhull.py

Description : This sample shows how to find the convex hull of contours

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/shapedescriptors/hull/hull.html

Level : Beginner

Benefits : Learn to use cv2.convexHull()

Usage : python convexhull.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials'''

import cv2
import numpy as np

def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)   # draw contours in green color
        cv2.drawContours(drawing,[hull],0,(0,0,255),2)  # draw contours in red color
        cv2.imshow('output',drawing)
        cv2.imshow('input',img)

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

cv2.namedWindow('input')

thresh = 100
max_thresh = 255

cv2.createTrackbar('canny thresh:','input',thresh,max_thresh,thresh_callback)

thresh_callback(0)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

### For more details & feature extraction on contours, visit : http://opencvpython.blogspot.com/2012/04/contour-features.html
