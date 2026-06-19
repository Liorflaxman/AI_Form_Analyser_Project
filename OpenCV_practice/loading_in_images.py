import numpy as np
import matplotlib.pyplot as plt
import cv2

"""
=============Loading in images================
- Using IMREAD_GRAYSCALE (0 - shortcut) makes everything one color making the image easier for the computer to analyse
**Other options**
- IMREAD_COLOR - 1 (shortcut)
- IMREAD_UNCHANGED = -1 (shortcut)
"""

img = cv2.imread('opencv_test_images/dog.JPG', cv2.IMREAD_GRAYSCALE)

#======MAIN METHOD TO DISPLAY AN IMAGE UNTIL A USER CLICKS USING CV======
cv2.imshow('image.JPG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('image_gray.png', img) # Method to save the image




#======METHOD TO DISPLAY AN IMAGE UNTIL A USER CLICKS USING PLT======
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()

