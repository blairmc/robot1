import cv2
import numpy as np
import os
from datetime import datetime

print("Testing Robot1 Vision Stack...")
print(f"OpenCV Version: {cv2.__version__}")

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Global variable to track capture request
capture_requested = False
exit_requested = False

def mouse_callback(event, x, y, flags, param):
    global capture_requested, exit_requested
    # Capture button coordinates: 10, 10, 150, 50
    # Exit button coordinates: 160, 10, 270, 50
    if event == cv2.EVENT_LBUTTONDOWN:
        if 10 <= x <= 150 and 10 <= y <= 50:
            capture_requested = True
        elif 160 <= x <= 270 and 10 <= y <= 50:
            exit_requested = True

# Try to open the first USB camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not find a USB camera.")
else:
    print("Camera found! Click the 'Capture' button or press 'q' to exit.")
    
    # Set up mouse callback
    cv2.namedWindow('Robot1 Camera Feed')
    cv2.setMouseCallback('Robot1 Camera Feed', mouse_callback)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        # Draw capture button on frame
        cv2.rectangle(frame, (10, 10), (150, 50), (0, 200, 0), -1)
        cv2.rectangle(frame, (10, 10), (150, 50), (0, 255, 0), 2)
        cv2.putText(frame, 'Capture', (25, 35), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.7, (255, 255, 255), 2)
        
        # Draw exit button on frame
        cv2.rectangle(frame, (160, 10), (270, 50), (0, 0, 200), -1)
        cv2.rectangle(frame, (160, 10), (270, 50), (0, 0, 255), 2)
        cv2.putText(frame, 'Exit', (190, 35), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.7, (255, 255, 255), 2)
        
        # Draw timestamp in upper right corner
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text_size = cv2.getTextSize(current_time, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
        text_x = frame.shape[1] - text_size[0] - 10
        cv2.putText(frame, current_time, (text_x, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.6, (255, 255, 255), 2)
        
        cv2.imshow('Robot1 Camera Feed', frame)
        
        # Check if capture was requested
        if capture_requested:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"images/photo_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Photo saved: {filename}")
            capture_requested = False
        
        # Check if exit was requested
        if exit_requested or cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()