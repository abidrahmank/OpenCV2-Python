''' file name : houghlines.py

Description : This sample shows how to detect lines using Hough Transform

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/hough_lines/hough_lines.html

Level : Beginner

Benefits : Learn to find lines in an image and draw them

Usage : python houghlines.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

print " Hough Lines demo "
print " Press h to draw lines using cv2.HoughLines()"
print " Press p to draw lines using cv2.HoughLinesP()"
print " All the parameter values selected at random, Change it the way you like"

im = cv2.imread('building.jpg')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,150,200,apertureSize = 3)

cv2.imshow('houghlines',im)

while(True):
    img = im.copy()
    k = cv2.waitKey(0)

    if k == ord('h'):   # Press 'h' to enable cv2.HoughLines()
        lines = cv2.HoughLines(edges,1,np.pi/180,275)
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))   # Here i have used int() instead of rounding the decimal value, so 3.8 --> 3
            y1 = int(y0 + 1000*(a))    # But if you want to round the number, then use np.around() function, then 3.8 --> 4.0
            x2 = int(x0 - 1000*(-b))   # But we need integers, so use int() function after that, ie int(np.around(x))
            y2 = int(y0 - 1000*(a))
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imshow('houghlines',img)

    elif k == ord('p'): # Press 'p' to enable cv2.HoughLinesP()
        lines = cv2.HoughLinesP(edges,1,np.pi/180,150, minLineLength = 100, maxLineGap = 10)
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imshow('houghlines',img)

    elif k == 27:    # Press 'ESC' to exit
        break

cv2.destroyAllWindows()
