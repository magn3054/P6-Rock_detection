import cv2

# rtsp://<username>:<password>@<ip-address>/axis-media/media.amp
rtsp_url = "rtsp://root:kamera@169.254.104.184/axis-media/media.amp"

# Open the video stream
thermal = cv2.VideoCapture(rtsp_url)
thermal.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
thermal.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Loop over frames from the video stream
while True:
    ret1, Tframe = thermal.read()
    ret2, Cframe = cam.read()
    
    if ret1 and ret2:
        
        # Tframe = cv2.resize(Tframe, (320, 240))
        # Cframe = cv2.resize(Cframe, (320, 240))

        # Process the frame here
        cv2.imshow("Thermal", Tframe)
        cv2.imshow("Normal", Cframe)
        
        # Exit if the user presses 'q'
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

# Cleanup
thermal.release()
cam.release()
cv2.destroyAllWindows()
