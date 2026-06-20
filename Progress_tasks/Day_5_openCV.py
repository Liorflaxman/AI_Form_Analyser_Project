"""
Script: 
-resize an image to 640x480, 
-apply a Gaussian blur, 
-detect edges, 
-display all three side by side
"""

import cv2
import numpy as np

img = cv2.imread('opencv_test_images/deer.JPG')

#====================RESIZING THE IMAGE==================
resized_img = cv2.resize(img, (640, 480))
#========================================================

#====================APPLY GUASSIAN BLUR=================
blur = cv2.GaussianBlur(img, (15,15), 0)
gaussian_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
#========================================================

#====================DETECT EDGES========================
edges = cv2.Canny(img, 100, 100)
#========================================================

cv2.imshow('original', img)
cv2.imshow('resized', resized_img)
cv2.imshow('blur', gaussian_rgb)
cv2.imshow('edge', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()