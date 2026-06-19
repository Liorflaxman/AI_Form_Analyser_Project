import numpy as np
import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(0) # captures video of webcam - can alternatively put in .mp4 file into parenthesis here

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