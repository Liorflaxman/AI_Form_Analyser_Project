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
"""
======MAIN METHOD TO DISPLAY AN IMAGE UNTIL A USER CLICKS USING CV======
cv2.imshow('image.JPG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('image_gray.png', img) - Method to save the image
"""


"""
======METHOD TO DISPLAY AN IMAGE UNTIL A USER CLICKS USING PLT======
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()
"""


#=============CREATING VIDEOS FROM WEBCAM AND SAVING THEM AS MP4================
cap = cv2.VideoCapture(0) # captures video of webcam

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', codec, 20.0, (width, height))

while True:
    ret, frame = cap.read() #ret will give true or false if there is a feed to read, then will give a frame if true
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts to gray
    
    out.write(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('Gray', gray) #Able to open to frames at the same time 
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
