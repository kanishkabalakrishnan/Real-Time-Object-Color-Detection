import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convert the frame from BGR to HSV
    into_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Blue color range
    L_limit_blue = np.array([98, 50, 50])
    U_limit_blue = np.array([139, 255, 255])
    blue_mask = cv2.inRange(into_hsv, L_limit_blue, U_limit_blue)
    blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    # Red color range
    L_limit_red1 = np.array([0, 100, 100])
    U_limit_red1 = np.array([10, 255, 255])
    L_limit_red2 = np.array([160, 100, 100])
    U_limit_red2 = np.array([179, 255, 255])
    red_mask1 = cv2.inRange(into_hsv, L_limit_red1, U_limit_red1)
    red_mask2 = cv2.inRange(into_hsv, L_limit_red2, U_limit_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # Display the results
    cv2.imshow('Original', frame)
    cv2.imshow('Blue Detector', blue_result)
    cv2.imshow('Red Detector', red_result)
    
    # Break the loop on 'Esc' key press
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
