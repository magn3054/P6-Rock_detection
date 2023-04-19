import cv2

# Set up video capture
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set up video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('RGBFieldRecord.mp4', fourcc, 30.0, (640, 480))

# Record for 10 minutes
start_time = cv2.getTickCount()
while True:
    # Read frame from camera
    ret, frame = cam.read()
    
    if ret:
        # Write frame to video file
        out.write(frame)
        
        # Display frame
        cv2.imshow("Recording", frame)
        
        # Exit if user presses 'q' or after 10 minutes
        if cv2.waitKey(1) == ord('q') or ((cv2.getTickCount() - start_time) / cv2.getTickFrequency()) >= 600:
            break

# Clean up
cam.release()
out.release()
cv2.destroyAllWindows()
