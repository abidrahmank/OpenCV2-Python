import cv2
import numpy as np

img = cv2.imread('home.jpg')

''' file name : pyramids.py

Description : This sample shows how to downsample and upsample images

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/pyramids/pyramids.html#pyramids

Level : Beginner

Benefits : Learn to use 1) cv2.pyrUp and 2) cv2.pyrDown

Usage : python pyramids.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''


print " Zoom In-Out demo "
print " Press u to zoom "
print " Press d to zoom "

img = cv2.imread('home.jpg')

while(1):
    h,w = img.shape[:2]
    
    cv2.imshow('image',img)
    k = cv2.waitKey(10)
    
    if k==27 :
        break

    elif k == ord('u'):  # Zoom in, make image double size
        img = cv2.pyrUp(img,dstsize = (2*w,2*h))

    elif k == ord('d'):  # Zoom down, make image half the size
        img = cv2.pyrDown(img,dstsize = (w/2,h/2))

cv2.destroyAllWindows()    
