"""
Read a video file, 
print its frame count, FPS, and resolution

Script: 
extract every 10th frame from a video 
save them as numbered JPEGs
"""
import numpy as np 
import cv2
import os 

video_path = 'opencv_test_images/arsenal.MOV'
output_folder = 'extracted_frames'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

codec = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('annotated_output.mp4', codec, fps, (width, height))

frame_id = 0       # Tracks the current frame position
saved_count = 0    # Tracks how many JPEGs we actually write out

font = cv2.FONT_HERSHEY_DUPLEX
while True:
    ret, frame = cap.read()

    if not ret:
        print("Reached the end of the video file.")
        break
    
    cv2.putText(frame, f'frame_id = {frame_id}', (150, 150), font, 1, (255,255,255), 3, cv2.LINE_AA)
        
    timestamp = round(frame_id / fps, 2)
    cv2.putText(frame, f"{timestamp}", ((width - 150), 150), font, 1, (255,255,255), 3, cv2.LINE_AA)
    
    out.write(frame)
    
    if frame_id % 10 == 0:
        # Generate a structured filename (e.g., extracted_frames/frame_0010.jpg)
        image_name = os.path.join(output_folder, f"frame_{frame_id:04d}.jpg")
        
        # Save the frame matrix as a JPEG file
        cv2.putText(frame, f'frame_id = {frame_id}', (150, 150), font, 1, (255,255,255), 3, cv2.LINE_AA)        
        cv2.imwrite(image_name, frame)
        saved_count += 1
    
    #cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    frame_id += 1 #move to next frame
    
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video description:\nResolution = {width} x {height}\nFPS = {fps}\nFrame Count = {length}")
print(f"Successfully saved {saved_count} frames to the '{output_folder}/' directory!")