import cv2
import numpy as np

# Load the images
img =cv2.imread('messi4.jpg')

# Convert them to grayscale
imgg =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# SURF extraction
surf = cv2.SURF()
kp, descritors = surf.detect(imgg,None,useProvidedKeypoints = False)

# Setting up samples and responses for kNN
samples = np.array(descritors)
responses = np.arange(len(kp),dtype = np.float32)

# kNN training
knn = cv2.KNearest()
knn.train(samples,responses)

# Now loading a template image and searching for similar keypoints
template = cv2.imread('tm.jpg')
templateg= cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
keys,desc = surf.detect(templateg,None,useProvidedKeypoints = False)

for h,des in enumerate(desc):
    des = np.array(des,np.float32).reshape((1,128))
    retval, results, neigh_resp, dists = knn.find_nearest(des,1)
    res,dist =  int(results[0][0]),dists[0][0]
    if dist<0.1: # draw matched keypoints in red color
        color = (0,0,255)
    else:  # draw unmatched in blue color
        print dist
        color = (255,0,0)

    #Draw matched key points on original image
    x,y = kp[res].pt
    center = (int(x),int(y))
    cv2.circle(img,center,4,color,-1)

    #Draw matched key points on template image
    x,y = keys[h].pt
    center = (int(x),int(y))
    cv2.circle(template,center,4,color,-1)

cv2.imshow('img',img)
cv2.imshow('tm',template)
cv2.imwrite('surfimg2.jpg',img)
cv2.imwrite('surftmp2.jpg',template)
cv2.waitKey(0)
cv2.destroyAllWindows()
