''' file name : remap.py

Description : This sample shows how to remap images

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/remap/remap.html#remap

Level : Beginner

Benefits : Learn to use remap function

Usage : python remap.py 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

def update():
    global ind
    ind = ind%4
    for j in xrange(rows):
        for i in xrange(cols):
            if ind == 0:   # Resize and center the image
                if 0.25*cols< i <0.75*cols and 0.25*rows< j <0.75*rows:
                    map_x.itemset((j,i),2*( i - cols*0.25 ) + 0.5)
                    map_y.itemset((j,i),2*( j - rows*0.25 ) + 0.5)
                else:     # Other pixel values set to zero
                    map_x.itemset((j,i),0)
                    map_y.itemset((j,i),0)

            elif ind == 1: # Flip image in vertical direction, alternatively you can use np.flipud or cv2.flip
                map_x.itemset((j,i),i)
                map_y.itemset((j,i),rows-j)

            elif ind == 2: # Flip image in horizontal direction, you can use np.fliplr or cv2.flip
                map_x.itemset((j,i),cols-i)
                map_y.itemset((j,i),j)

            elif ind == 3: # Flip image in both the directions, you can use cv2.flip(flag = -1)
                map_x.itemset((j,i),cols-i)
                map_y.itemset((j,i),rows-j)
    ind = ind+1

img = cv2.imread('messi5.jpg')
ind = 0
map_x = np.zeros(img.shape[:2],np.float32)
map_y = np.zeros(img.shape[:2],np.float32)
rows,cols = img.shape[:2]
while(True):
    update()
    dst = cv2.remap(img,map_x,map_y,cv2.INTER_LINEAR)
    cv2.imshow('dst',dst)
    if cv2.waitKey(1000)==27:
        break
cv2.destroyAllWindows()
