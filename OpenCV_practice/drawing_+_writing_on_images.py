import numpy as np
import cv2

img = cv2.imread('opencv_test_images/dog.JPG', cv2.IMREAD_COLOR)

#===============Drawing Shapes on an images=================
img = cv2.resize(img, (800, 600)) #resizing for lesson purposes

cv2.line(img, (0,0), (150,150), (255, 255, 255), 15) #line start, line end, color of line (in BGR format), line width in pixels
cv2.rectangle(img, (15, 25), (200,150), (0,0,0), 5) #top left co-ord, bottom right co-ord, color, width
cv2.circle(img, (100, 63), 55, (0,0,255), -1) #centre of circle, radius, color, -1=fills in circle

points = np.array([[10, 5],[20,30],[70,20],[50,10]], np.int32)
points = points.reshape((-1,1,2)) # reshapes array to 1 by 2
cv2.polylines(img, [points], True, (0,255,255), 3) #points of polygon, True=connect last lines, color, line width

#==============Writing on an image==========================
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OPENCV TUTORIAL', (0, 130), font, 1, (100,255,255), 2, cv2.LINE_AA) 
# script for image, where writing starts, font, size, color, thickness, linetype


cv2.imshow('image_with_line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
