''' file name : findcontours.py

Description : This sample shows how to find and draw contours

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/shapedescriptors/find_contours/find_contours.html#find-contours

Level : Beginner

Benefits : Learn to use 1) cv2.findContours() and 2)cv2.drawContours()

Usage : python findcontours.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials'''

import cv2
import numpy as np

def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        color = np.random.randint(0,255,(3)).tolist()  # Select a random color
        cv2.drawContours(drawing,[cnt],0,color,2)
        cv2.imshow('output',drawing)
    cv2.imshow('input',img)

img = cv2.imread('jonty2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

cv2.namedWindow('input',cv2.WINDOW_AUTOSIZE)

thresh = 100
max_thresh = 255

cv2.createTrackbar('canny thresh:','input',thresh,max_thresh,thresh_callback)

thresh_callback(thresh)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

### For more details & feature extraction on contours, visit : http://opencvpython.blogspot.com/2012/04/contour-features.html
