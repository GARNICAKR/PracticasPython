# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:08:37 2020

@author: dell
"""

import cv2 as cv
import numpy as np

imagenOriginal=cv.imread('C:\\Users\\dell\\Documents\\Semestre lV\\Seminario Algoritmia\\img\\yane_garcia.jpg')
imagenPlaya=cv.imread('C:\\Users\\dell\\Documents\\Semestre lV\\Seminario Algoritmia\\img\\playa.jpg')
#imagenPlaya = cv.VideoCapture("C:\\Users\\dell\\Pictures\\iCloud Photos\\Downloads\\21.mp4")


bgr = [80, 200, 80]
thresh = 50
minBGR=[bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh]
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
 
maskBGR = cv.inRange(imagenOriginal,minBGR,maxBGR)
mask_inv = cv.bitwise_not(maskBGR)
cv.imshow('mascara',maskBGR)
cv.imshow('mascara_inv',mask_inv)

resultBGR = cv.bitwise_and(imagenOriginal, imagenOriginal, mask = mask_inv)
result_inv = cv.bitwise_and(imagenPlaya, imagenPlaya, mask = maskBGR)


cv.imshow('resultado',resultBGR)
cv.imshow('resultado_inv',result_inv)

total=cv.add(resultBGR,result_inv)
cv.imshow('resultado total',total)

cv.imwrite('resultado.mp4',total)
cv.waitKey()
cv.destroyAllWindows()