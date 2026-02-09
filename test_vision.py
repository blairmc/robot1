import cv2
import numpy as np

print("Testing Robot1 Vision Stack...")
print(f"OpenCV Version: {cv2.__version__}")

# Try to open the first USB camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not find a USB camera.")
else:
    print("Camera found! Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        cv2.imshow('Robot1 Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()