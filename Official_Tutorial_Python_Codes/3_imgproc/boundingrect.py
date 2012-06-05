''' file name : boundingrect.py

Description : This sample shows how to find the bounding rectangle and minimum enclosing circle of a contour

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/shapedescriptors/bounding_rects_circles/bounding_rects_circles.html
Level : Beginner

Benefits : Learn to use 1) cv2.boundingRect() and 2) cv2.minEnclosingCircle()

Usage : python boundingrect.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials'''

import cv2
import numpy as np

def thresh_callback(thresh):
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        bx,by,bw,bh = cv2.boundingRect(cnt)
        (cx,cy),radius = cv2.minEnclosingCircle(cnt)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),1)   # draw contours in green color
        cv2.circle(drawing,(int(cx),int(cy)),int(radius),(0,0,255),2)   # draw circle in red color
        cv2.rectangle(drawing,(bx,by),(bx+bw,by+bh),(255,0,0),3) # draw rectangle in blue color)
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
