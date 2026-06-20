import numpy as np
import cv2

# Thresholding is used to simplify an image into only 0s or 1s (white or black pixels)
img = cv2.imread('opencv_test_images/bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) 
#image is very dark so we want any pixel value below 12 to become white
#for very bright images use 220

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY) 

#=======================GUASSIAN ADAPTIVE THRESHOLD====================
guas = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#applies to grayscaled version, max value, uses guassian threshold, converts it to binary



cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('guas', guas)

cv2.waitKey(0)
cv2.destroyAllWindows