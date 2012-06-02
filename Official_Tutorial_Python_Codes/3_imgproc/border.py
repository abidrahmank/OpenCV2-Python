''' file name : border.py

Description : This sample shows how to add border to an image

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/copyMakeBorder/copyMakeBorder.html#copymakebordertutorial

Level : Beginner

Benefits : Learn to use cv2.copyMakeBorder()

Usage : python border.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

print " Press r to replicate the border with a random color "
print " Press c to replicate the border "
print " Press Esc to exit "

img = cv2.imread('home.jpg')
rows,cols = img.shape[:2]

dst = img.copy()

top = int (0.05*rows)
bottom = int (0.05*rows)

left = int (0.05*cols)
right = int (0.05*cols)

while(True):
    
    cv2.imshow('border',dst)
    k = cv2.waitKey(500)
    
    if k==27:
        break
    elif k == ord('c'):
        value = np.random.randint(0,255,(3,)).tolist()
        dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = value)
    elif k == ord('r'):
        dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_REPLICATE)

cv2.destroyAllWindows()    
