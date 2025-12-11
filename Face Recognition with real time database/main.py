import cv2

# Initialize the camera using the DirectShow backend for better Windows compatibility
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) # <-- Changed line

print(cap)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream or file")
    print("Check OS permissions, antivirus settings, or if another app is using the camera.")
else:
    print("Camera initialized successfully. Attempting to start video feed...")
    
    # Loop indefinitely to capture frames
    while True:
        # Read a frame: 'ret' is a boolean (True/False), 'frame' is the image data
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame. Exiting loop.")
            # If ret is False, the stream stopped or failed to grab
            break

        # Display the resulting frame in a window named 'Face Recognition'
        cv2.imshow('Face Recognition', frame)

        # Press 'q' key to exit the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture object
cap.release()
# Close all the frames/windows
cv2.destroyAllWindows()

