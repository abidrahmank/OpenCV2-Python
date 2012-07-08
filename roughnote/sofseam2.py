''' seam carving - http://en.wikipedia.org/wiki/Seam_carving '''
import cv2
import numpy as np
#import hist

img = cv2.imread('sofseam.jpg',0)
im = cv2.imread('sofseam.jpg')
rows,cols = img.shape

dx = cv2.Sobel(img,cv2.CV_32F,1,0)
dy = cv2.Sobel(img,cv2.CV_32F,0,1)
dz = np.zeros(img.shape,np.float32)
dx2 = cv2.accumulateSquare(dx,dz)
dy2 = cv2.accumulateSquare(dy,dz)

lap = cv2.sqrt(dz)
#lap = cv2.convertScaleAbs(lap)

t = np.zeros(img.shape,np.float32)
t[0,:] = lap[0,:]

for r in xrange(1,rows):
    for c in xrange(0,cols):
        i = lap.item(r,c)
        
        if c==0:
            j = min(t[r-1,c:c+2])
        elif c==cols-1:
            j = min(t[r-1,c-1:c+1])
        else:
            j = min(t[r-1,c-1:c+2])
        t.itemset(r,c,i+j)
#tt = cv2.convertScaleAbs(t)
#cv2.normalize(tt,tt,0,255,cv2.NORM_MINMAX)
##cv2.imshow('tt',t)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

for c in xrange(1,cols-1):
    temp = []
    #if t.item(rows-1,c) < 8200:
    temp.append([c,0])
    pc = c
    for r in xrange(1,rows-1):
        if pc == 0:
            j = np.argmin(t[r+1,pc:pc+2])
            if j == 0:pc = pc
            elif j == 1:pc = pc+1
            
        else:
            j = np.argmin(t[r+1,pc-1:pc+2])
            if j == 0:pc = pc-1
            elif j == 2:pc = pc+1
            else : pc = pc

        temp.append([pc,r])
    temp = np.array(temp,dtype = np.int32).reshape(len(temp),2)
    cv2.polylines(im,[temp],False,(0,0,255),2)
    
    cv2.imshow('t',im)

    cv2.waitKey(5)
#cv2.imshow('lap',lap)
cv2.waitKey(0)
cv2.destroyAllWindows()
