''' file name : minarearect.py

Description : This sample shows how to find minimum area rectangle and fit an ellipse to a contour

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/shapedescriptors/bounding_rotated_ellipses/bounding_rotated_ellipses.html

Level : Beginner

Benefits : Learn to use 1)cv2.minAreaRect() and 2) cv2.fitEllipse()

Usage : python minarearect.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials'''

import cv2
import numpy as np

def thresh_callback(thresh):
    global contours
    edges = cv2.Canny(blur,thresh,thresh*2)
    drawing = np.zeros(img.shape,np.uint8)      # Image to draw the contours
    contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)             # rect = ((center_x,center_y),(width,height),angle)
        points = cv2.cv.BoxPoints(rect)         # Find four vertices of rectangle from above rect
        points = np.int0(np.around(points))     # Round the values and make it integers

        ellipse = cv2.fitEllipse(cnt)           # ellipse = ((center),(width,height of bounding rect), angle)
        
        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)   # draw contours in green color
        cv2.ellipse(drawing,ellipse,(0,0,255),2)        # draw ellipse in red color
        cv2.polylines(drawing,[points],True,(255,0,0),2)# draw rectangle in blue color

        cv2.imshow('output',drawing)
        cv2.imshow('input',img)

img = cv2.imread('new.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

cv2.namedWindow('input')

thresh = 200
max_thresh = 255

cv2.createTrackbar('canny thresh:','input',thresh,max_thresh,thresh_callback)

thresh_callback(200)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

### For more details & feature extraction on contours, visit : http://opencvpython.blogspot.com/2012/04/contour-features.html
