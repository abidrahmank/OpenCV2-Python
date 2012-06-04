''' file name : geometric_transform.py

Description : This sample shows image transformation and rotation

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html

Level : Beginner

Benefits : Learn 1) Affine transformation 2) Image Rotation

Usage : python 

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
rows,cols = img.shape[:2]

# Source points
srcTri = np.array([(0,0),(cols-1,0),(0,rows-1)], np.float32)

# Corresponding Destination Points. Remember, both sets are of float32 type
dstTri = np.array([(cols*0.0,rows*0.33),(cols*0.85,rows*0.25), (cols*0.15,rows*0.7)],np.float32)

# Affine Transformation
warp_mat = cv2.getAffineTransform(srcTri,dstTri)   # Generating affine transform matrix of size 2x3
dst = cv2.warpAffine(img,warp_mat,(cols,rows))     # Now transform the image, notice dst_size=(cols,rows), not (rows,cols)

# Image Rotation
center = (cols/2,rows/2)                           # Center point about which image is transformed
angle = -50.0                                      # Angle, remember negative angle denotes clockwise rotation
scale = 0.6                                        # Isotropic scale factor.

rot_mat = cv2.getRotationMatrix2D(center,angle,scale) # Rotation matrix generated
dst_rot = cv2.warpAffine(dst,rot_mat,(cols,rows))     # Now transform the image wrt rotation matrix

cv2.imshow('dst_rt',dst_rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
