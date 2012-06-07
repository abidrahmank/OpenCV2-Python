''' file name : pointpolygontest.py

Description : This sample shows how to find distance from a point to a contour

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/shapedescriptors/point_polygon_test/point_polygon_test.html

Level : Beginner

Benefits : Learn to use cv2.pointPolygonTest()

Usage : python pointpolygontest.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

r = 100

src = np.zeros((4*r,4*r),np.uint8)
rows,cols = src.shape

# draw an polygon on image src
points = [ [1.5*r,1.34*r], [r,2*r], [1.5*r,2.866*r], [2.5*r,2.866*r],[3*r,2*r],[2.5*r,1.34*r] ]
points = np.array(points,np.int0)
cv2.polylines(src,[points],True,255,3)

contours,hierarchy = cv2.findContours(src,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

res = np.zeros(src.shape,np.float32)                # array to store distances
drawing = np.zeros((rows,cols,3),np.uint8)          # image to draw the distance
cnt = contours[0]                                   # We take only one contour for testing

# Calculate distance from each point
for i in xrange(rows):
    for j in xrange(cols):
        res.itemset((i,j),cv2.pointPolygonTest(cnt,(j,i),True))


mini,maxi = np.abs(cv2.minMaxLoc(res)[:2])          # Find minimum and maximum to adjust colors
mini = 255.0/mini
maxi = 255.0/maxi

for i in xrange(rows):                              # Now we colorise as per distance
    for j in xrange(cols):
        if res.item((i,j))<0:
            drawing.itemset((i,j,0),255-int(abs(res.item(i,j))*mini))   # If outside, blue color
        elif res.item((i,j))>0:
            drawing.itemset((i,j,2),255-int(res.item(i,j)*maxi))        # If inside, red color
        else:
            drawing[i,j]=[255,255,255]                                  # If on the contour, white color.

cv2.imshow('point',drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()

### For more details & feature extraction on contours, visit : http://opencvpython.blogspot.com/2012/04/contour-features.html
### For much more better and faster (50X) method, visit:http://opencvpython.blogspot.com/2012/06/fast-array-manipulation-in-numpy.html
