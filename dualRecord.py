#records from both cameras for 2 min or until operator presses 'q'

import cv2
import time
import os


Time = time.localtime()
dateNOW = time.strftime("%d-%m-%Y", Time)
timeNOW = time.strftime("%H;%M;%S", Time)

if not os.path.exists(f"Recordings/{dateNOW}"):
    os.makedirs(f"Recordings/{dateNOW}")


# Open the first camera
cam1 = cv2.VideoCapture(1)
cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Open the second camera
cam2 = cv2.VideoCapture('rtsp://root:kamera@169.254.104.184/axis-media/media.amp')
cam2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a VideoWriter object to save the output
RGBfilename = os.path.join("Recordings", f"{dateNOW}", f"RGB_{timeNOW}.mp4")
THERMALfilename = os.path.join("Recordings", f"{dateNOW}", f"Thermal_{timeNOW}.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out1 = cv2.VideoWriter(RGBfilename,     fourcc, 30.0, (640, 480))
out2 = cv2.VideoWriter(THERMALfilename, fourcc, 30.0, (640, 480))

# Loop over frames from the cameras
while True:
    # Capture a frame from each camera
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    # Check if both frames were captured successfully
    if ret1 and ret2:
        # Resize the frames
        frame1 = cv2.resize(frame1, (640, 480))
        frame2 = cv2.resize(frame2, (640, 480))

        # Display the frames
        cv2.imshow('Camera 1', frame1)
        cv2.imshow('Camera 2', frame2)

        # Write the frames to the output
        out1.write(frame1)
        out2.write(frame2)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Cleanup
cam1.release()
cam2.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
