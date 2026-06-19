import numpy as np
import cv2

img = cv2.imread('opencv_test_images/dog.JPG', cv2.IMREAD_COLOR)

img = cv2.resize(img, (800, 600))

cv2.line(img, (0,0), (150,150), (255, 255, 255), 15) #line start, line end, color of line (in BGR format), line width in pixels
cv2.rectangle(img, (15, 25), (200,150), (0,0,0), 5)

cv2.imshow('image_with_line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
