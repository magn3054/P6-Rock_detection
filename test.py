import cv2
import time
import os

Time = time.localtime()
dateNOW = time.strftime("%d-%m-%Y", Time)
timeNOW = time.strftime("%H;%M;%S", Time)
start_time = time.time()

if not os.path.exists(f"Images/{dateNOW}"):
    os.makedirs(f"Images/{dateNOW}")

cs = cv2.VideoCapture(1)
ts = cv2.VideoCapture(0)

# Define variables outside the loop
frameC = None
frameT = None

# Loop through the frames
while (time.time() - start_time) < 5:
    # Read the frame
    ret, frameC = cs.read()
    ret2, frameT = ts.read()

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
cs.release()
ts.release()
cv2.destroyAllWindows()
