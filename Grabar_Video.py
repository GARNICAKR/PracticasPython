# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:05:38 2020

@author: dell
"""
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
cap2=cv.VideoCapture('C:\\Users\\dell\\Pictures\\iCloud Photos\\Downloads\\21.mp4')
imagenOriginal=cv.imread('C:\\Users\\dell\\Documents\\Semestre lV\\Seminario Algoritmia\\img\\yane_garcia.jpg')
imagenPlaya=cv.imread('C:\\Users\\dell\\Documents\\Semestre lV\\Seminario Algoritmia\\img\\playa.jpg')
bgr = [80, 200, 80]
thresh = 50
minBGR=[bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh]
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
cont =0
fgbg = cv.createBackgroundSubtractorMOG2()
while(True):
   
    ret,frame=cap.read()
    ret,frame2=cap2.read()
    
    fgmask = fgbg.apply(frame)
    #fgmask1 = fgbg.apply(frame2)
    mask_inv = cv.bitwise_not(fgmask)
    #maskBGR = cv.inRange(frame,minBGR,maxBGR)
    #mask_inv = cv.bitwise_not(maskBGR)
    
    resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)
   # result_inv = cv.bitwise_and(frame2, frame2, mask = fgmask1)

    #total=cv.add(resultBGR,frame2)
    #cv.imshow('definitivo',total)

    #cv.imshow('resultado inv',frame2)

    cv.imshow('resultBGR',resultBGR)

    cv.imshow('resultado total2',mask_inv)
    cv.imshow('resultado total',fgmask)
    if cv.waitKey(1) & 0xFF == ord ('q'):
        break
    
cap.release()
cv.destroyAllWindows()