import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_ is used as the returned value is going to be unused
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #hsv = hue, saturation value - used over RGB as hue is a single digit for color instead of 3, saturation is intensity
    
    
    lower_red = np.array([140,150,0]) #hue value, saturation value
    upper_red = np.array([180,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask) #where there is something in the frame and the mask is true (if the color is in the range of upper and lower red), where true it shows the color in the frame
    
    """
    #BLURRING TECHNIQUES- need to average out pixels (15 by 15 numpy array of 1s / 225(15x15)
    kernal = np.ones((15,15), np.float32) / 225
    smoothed = cv2.filter2D(result, -1, kernal)
    
    blur = cv2.GaussianBlur(result, (15,15), 0)
    median = cv2.medianBlur(result, 15)
    """
    
    # =======================MORPHOLOOGICAL TRANSFORMATIONS===================
    
    kernal = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernal, iterations=1)
    dilation = cv2.dilate(mask, kernal, iterations=1)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)


    
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', result)
    cv2.imshow('closing', closing)
    cv2.imshow('dilation', opening)


    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()