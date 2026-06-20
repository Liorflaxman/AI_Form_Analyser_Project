import numpy as np
import cv2

"""
USUAL DATA OPERATIONS ON IMAGES - EG, FACE DETECTION
- submit a colored version
- immediately convert to greyscale to do operations, find faces and co ordinates of faces on grayed version
- draw rectangles on those co ordinates on the colored version
"""


img = cv2.imread('opencv_test_images/dog.JPG', cv2.IMREAD_COLOR)

#px = img[55,55] #location of pixel
#print(px) - will print the color value of the pixel, in this case [207 209 209]
#img[55,55] = [255,255,255] - can use this to modify color of pixel

#=============================================
#ROI = region of image (image within an image)
#=============================================

#roi = img[100:150, 100:150]
#img[100:150, 100:150] = [255,255,255] - will make the area a white square
#print(roi) - prints numpy array of pixel values in the region

"""
#================COPY AND PASTING================
copy_paste = img[37:111, 107:194]
img[0:74, 0:87] = copy_paste
#this copy and pastes the cells in the img region 37:111... on top of the img region below it
"""
#===============OVERLAYING IMAGES ON TOP OF EACHOTHER=============
img1 = cv2.imread('opencv_test_images/bird.JPG')
img2 = cv2.imread('opencv_test_images/deer.JPG')

img1 = cv2.resize(img1, (1600, 1200))
img2 = cv2.resize(img2, (800, 600)) # - addition must be with 2 images the same dimensions

#add = img1 + img2
#add = cv2.add(img1, img2) # adds all pixel values together

#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #first image weight, second image weight, gamma value

#=================================================================================
#Removing white backgrounds from an image and adding that image onto another image
#=================================================================================

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols] #defining region of image one we want to use to overlay the image 2 based of its size
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Threshold image to get a black background and foreground is white
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #filters out any pixel value above 220 and converts to 255, if below, converted to black. binary.inv inverts this

#inversing background to be white and foreground to be black
mask_inv = cv2.bitwise_not(mask) #not mask = black area of mask (NOT 255), bitwise is essentially like the python operators

#ask opencv to only use the original value of the image
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

#adding the cropped image to match the background of the other image to give effect of transparent background
dst = cv2.add(img1_bg, img2_fg) #add image 1 background and img2 foreground
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
