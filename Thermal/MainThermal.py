import cv2

# rtsp://<username>:<password>@<ip-address>/axis-media/media.amp
rtsp_url = "rtsp://root:kamera@169.254.104.184/axis-media/media.amp"

# Open the video stream
cap = cv2.VideoCapture(rtsp_url)

# Loop over frames from the video stream
while True:
    ret, frame = cap.read()
    
    if ret:
        # Process the frame here
        cv2.imshow("Frame", frame)
        
        # Exit if the user presses 'q'
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
