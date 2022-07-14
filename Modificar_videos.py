# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:21:18 2020

@author: dell
"""

import cv2 as cv
import numpy as np
cap=cv.VideoCapture('C:\\Users\\dell\\Documents\\Semestre lV\\Seminario Algoritmia\\img\\yo_1.mp4')
cap2=cv.imread('C:\\Users\\dell\\Documents\\Semestre lV\\Seminario Algoritmia\\img\\playa.jpg')
dim = (480,848)
cap2 = cv.resize(cap2, dim, interpolation = cv.INTER_AREA)
bgr = [213, 193, 180]
thresh = 50
minBGR=[bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh]
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
cont =0
fgbg = cv.createBackgroundSubtractorMOG2()
print(cap2.shape)
while(True):
   
    ret,frame=cap.read()
    #print(frame.shape)    
    
    
    maskBGR = cv.inRange(frame,minBGR,maxBGR)
    mask_inv = cv.bitwise_not(maskBGR)
    
    resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)
    result_inv = cv.bitwise_and(cap2, cap2, mask = maskBGR)

    total=cv.add(resultBGR,result_inv)
    cv.imshow('definitivo',total)

    cv.imshow('resultBGR',resultBGR)

    cv.imshow('resultado total2',mask_inv)
    cv.imshow('resultado total',maskBGR)
    if cv.waitKey(1) & 0xFF == ord ('q'):
        break
    
cap.release()
cv.destroyAllWindows()