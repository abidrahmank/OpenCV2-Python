''' file name : comparehist.py

Description : This sample shows how to determine how well two histograms match each other.

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/histograms/histogram_comparison/histogram_comparison.html

Level : Beginner

Benefits : Learn to use cv2.compareHist and create 2D histograms

Usage : python comparehist.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np

base = cv2.imread('base.png')
test1 = cv2.imread('test1.jpg')
test2 = cv2.imread('test2.jpg')

rows,cols = base.shape[:2]

basehsv = cv2.cvtColor(base,cv2.COLOR_BGR2HSV)
test1hsv = cv2.cvtColor(test1,cv2.COLOR_BGR2HSV)
test2hsv = cv2.cvtColor(test2,cv2.COLOR_BGR2HSV)

halfhsv = basehsv[rows/2:rows-1,cols/2:cols-1].copy()  # Take lower half of the base image for testing

hbins = 180
sbins = 255
hrange = [0,180]
srange = [0,256]
ranges = hrange+srange                                  # ranges = [0,180,0,256]


histbase = cv2.calcHist(basehsv,[0,1],None,[180,256],ranges)
cv2.normalize(histbase,histbase,0,255,cv2.NORM_MINMAX)

histhalf = cv2.calcHist(halfhsv,[0,1],None,[180,256],ranges)
cv2.normalize(histhalf,histhalf,0,255,cv2.NORM_MINMAX)

histtest1 = cv2.calcHist(test1hsv,[0,1],None,[180,256],ranges)
cv2.normalize(histtest1,histtest1,0,255,cv2.NORM_MINMAX)

histtest2 = cv2.calcHist(test2hsv,[0,1],None,[180,256],ranges)
cv2.normalize(histtest2,histtest2,0,255,cv2.NORM_MINMAX)

for i in xrange(4):
    base_base = cv2.compareHist(histbase,histbase,i)
    base_half = cv2.compareHist(histbase,histhalf,i)
    base_test1 = cv2.compareHist(histbase,histtest1,i)
    base_test2 = cv2.compareHist(histbase,histtest2,i)
    print "Method: {0} -- base-base: {1} , base-half: {2} , base-test1: {3}, base_test2: {4}".format(i,base_base,base_half,base_test1,base_test2)

    
