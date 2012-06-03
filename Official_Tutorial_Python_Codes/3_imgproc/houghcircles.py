''' file name : houghcircles.py

Description : This sample shows how to detect circles in image with Hough Transform

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/hough_circle/hough_circle.html

Level : Beginner

Benefits : Learn to find circles in the image and draw them

Usage : python houghcircles.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np
import sys

if len(sys.argv)>1:
    filename = sys.argv[1]
else:
    filename = 'board.jpg'

img = cv2.imread(filename,0)
if img==None:
    print "cannot open ",filename

else:
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=5,maxRadius=20)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
