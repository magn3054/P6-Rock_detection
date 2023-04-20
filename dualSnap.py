import cv2
import time
import os

import RGB.MainRGB as cam


Time = time.localtime()
dateNOW = time.strftime("%d-%m-%Y", Time)
timeNOW = time.strftime("%H;%M;%S", Time)

if not os.path.exists(f"Images/{dateNOW}"):
    os.makedirs(f"Images/{dateNOW}")

URL = "rtsp://root:kamera@169.254.104.184/axis-media/media.amp"

cs = cam.CamStream(camera_index=1, width=640, height=480)
ts = cam.CamStream(camera_index=URL, width=640, height=480)

# Wait for camera to warm up
cv2.waitKey(5000)

# Capture an image
ret, frameC = cs.cam.read()
ret2, frameT = ts.cam.read()


# Display the image
cv2.imshow("Image", frameC)
cv2.imshow("Image2", frameT)

# Save the image to a file
RGBfilename = os.path.join("Images", f"{dateNOW}", f"RGB_{timeNOW}.jpg")
cv2.imwrite(RGBfilename, frameC)
THERMALfilename = os.path.join("Images", f"{dateNOW}", f"Thermal_{timeNOW}.jpg")
cv2.imwrite(THERMALfilename, frameT)

# Cleanup
cs.cam.release()
ts.cam.release()
cv2.destroyAllWindows()