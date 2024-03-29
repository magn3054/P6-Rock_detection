import cv2
import time
import os

import RGB.MainRGB as cam


Time = time.localtime()
dateNOW = time.strftime("%d-%m-%Y", Time)
timeNOW = time.strftime("%H;%M;%S", Time)
start_time = time.time()

if not os.path.exists(f"Images/{dateNOW}"):
    os.makedirs(f"Images/{dateNOW}")

URL = "rtsp://root:kamera@169.254.104.184/axis-media/media.amp"

cs = cam.CamStream(camera_index=1, width=640, height=480)
ts = cam.CamStream(camera_index=URL, width=640, height=480)


# Loop through the frames
while (time.time() - start_time) < 10:
    # Read the frame
    ret, frameC = cs.cam.read()
    ret2, frameT = ts.cam.read()

    # Display the frame
    cv2.imshow('Camera Feed', frameC)
    cv2.imshow('Thermal Feed', frameT)
    cv2.waitKey(1)

# Save the image to a file
RGBfilename = os.path.join("Images", f"{dateNOW}", f"RGB_{timeNOW}.jpg")
cv2.imwrite(RGBfilename, frameC)
THERMALfilename = os.path.join("Images", f"{dateNOW}", f"Thermal_{timeNOW}.jpg")
cv2.imwrite(THERMALfilename, frameT)

# Cleanup
cs.cam.release()
ts.cam.release()
cv2.destroyAllWindows()