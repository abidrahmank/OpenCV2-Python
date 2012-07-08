''' seam carving - http://en.wikipedia.org/wiki/Seam_carving '''

import cv2
import numpy as np
#import hist

img = cv2.imread('sofseam.jpg',0)
im = cv2.imread('sofseam.jpg')
im2 = im.copy()
rows,cols = img.shape

dx = cv2.Sobel(img,cv2.CV_32F,1,0)
dy = cv2.Sobel(img,cv2.CV_32F,0,1)
dz = np.zeros(img.shape,np.float32)
dx2 = cv2.accumulateSquare(dx,dz)
dy2 = cv2.accumulateSquare(dy,dz)

lap = cv2.sqrt(dz)

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
maxt = t.max()
mask = np.zeros(img.shape,np.uint8)
for c in xrange(1,cols-1):
    temp = []
    if t.item(rows-1,c) < 1000000:
        temp.append([c,rows-1])
        pc = c
        for r in xrange(rows-1,0,-1):
            if pc == 0:
                j = np.argmin(t[r-1,pc:pc+2])
                if j == 0:pc = pc
                elif j == 1:pc = pc+1
                
            else:
                j = np.argmin(t[r-1,pc-1:pc+2])
                if j == 0:pc = pc-1
                elif j == 2:pc = pc+1
                else : pc = pc

            temp.append([pc,r])
        temp = np.array(temp,dtype = np.int32).reshape(len(temp),2)
        cv2.polylines(im,[temp],False,(0,0,255),2)
        cv2.polylines(mask,[temp],False,255,1)
        
    cv2.imshow('t',im)
    cv2.imshow('mask',mask)

    cv2.waitKey(1)

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
    cv2.polylines(mask,[temp],False,255,1)

    cv2.imshow('t',im)
    cv2.imshow('mask',mask)

    cv2.waitKey(1)

    
############################################################################################333

tt = np.zeros(img.shape,np.float32)
tt[:,0] = lap[:,0]

for c in xrange(1,cols):
    for r in xrange(0,rows):
        i = lap.item(r,c)
        
        if r==0:
            j = min(tt[r:r+2,c-1])
        elif r==rows-1:
            j = min(tt[r-1:r+1,c-1])
        else:
            j = min(tt[r-1:r+2,c-1])
        tt.itemset(r,c,i+j)

#mask = np.zeros(img.shape,np.uint8)
for r in xrange(1,rows-1):
    temp = []
    #if tt.item(rows-1,c) < 1000000:
    temp.append([cols-1,r])
    pr = r
    for c in xrange(cols-1,0,-1):
        if pr == 0:
            j = np.argmin(tt[pr:pr+2,c-1])
            if j == 0:pr = pr
            elif j == 1:pr = pr+1
            
        else:
            j = np.argmin(tt[pr-1:pr+2,c-1])
            if j == 0:pr = pr-1
            elif j == 2:pr = pr+1
            else : pr = pr

        temp.append([c,pr])
    temp = np.array(temp,dtype = np.int32).reshape(len(temp),2)
    cv2.polylines(im,[temp],False,(0,0,255),2)
    cv2.polylines(mask,[temp],False,255,1)
        
    cv2.imshow('t',im)
    cv2.imshow('mask',mask)
#
    cv2.waitKey(1)

for r in xrange(1,rows-1):
    temp = []
    #if tt.item(rows-1,c) < 1000000:
    temp.append([0,r])
    pr = r
    for c in xrange(0,cols-1):
        if pr == 0:
            j = np.argmin(tt[pr:pr+2,c+1])
            if j == 0:pr = pr
            elif j == 1:pr = pr+1
            
        else:
            j = np.argmin(tt[pr-1:pr+2,c+1])
            if j == 0:pr = pr-1
            elif j == 2:pr = pr+1
            else : pr = pr

        temp.append([c,pr])
    temp = np.array(temp,dtype = np.int32).reshape(len(temp),2)
    cv2.polylines(im,[temp],False,(0,0,255),2)
    cv2.polylines(mask,[temp],False,255,1)
        
    cv2.imshow('t',im)
    cv2.imshow('mask',mask)
#
    cv2.waitKey(1)

#######################################################################################################
mask[0,:] = mask[rows-1:0] = mask[:,0] = mask[:,cols-1] = 255

##rowarg = np.argmin(np.sum(mask,0))
##colarg = np.argmin(np.sum(mask,1))
##
##cv2.circle(im2,(rowarg,colarg),5,(0,255,0),-1)
##sumx = np.sum(mask,0)
##sumy = np.sum(mask,1)
##col = np.where(sumx == sumx.min())[0]
##row = np.where(sumy == sumy.min())[0]
##
##im2[:,col-1:col+1] = [255,0,0]
##im2[row-1:row+1,:] = [255,0,0]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
mask2 = cv2.morphologyEx(mask,cv2.MORPH_DILATE,kernel)


cv2.imshow('tt',mask2)
#cv2.imshow('lap',lap)
cv2.waitKey(0)
cv2.destroyAllWindows()
