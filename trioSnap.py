import cv2
import time
import os
import numpy as np
import pyrealsense2 as rs
import RGB.MainRGB as cam


Time = time.localtime()
dateNOW = time.strftime("%d-%m-%Y", Time)
timeNOW = time.strftime("%H;%M;%S", Time)
start_time = time.time()

if not os.path.exists(f"Images/{dateNOW}"):
    os.makedirs(f"Images/{dateNOW}")

URL = "rtsp://root:kamera@169.254.104.185/axis-media/media.amp"
ts = cam.CamStream(camera_index=URL, width=640, height=480)

# Configure depth and color streams from the RealSense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming from the RealSense camera
pipeline.start(config)

# Loop through the frames
while (time.time() - start_time) < 10:
    # Read the frames from the cameras
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    ret2, frameT = ts.cam.read()

    # Capture a depth frame from the RealSense camera
    depth_frame = frames.get_depth_frame()

    # Convert the depth frame to a numpy array for processing
    depth_image = np.asanyarray(depth_frame.get_data())

    # Display the frames
    cv2.imshow('RGB Feed', np.asanyarray(color_frame.get_data()))
    cv2.imshow('Thermal Feed', frameT)

    # Convert the depth image to a color map for visualization
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    cv2.imshow('Depth Feed', depth_colormap)
    cv2.waitKey(1)

# Save the images to files
RGBfilename = os.path.join("Images", f"{dateNOW}", f"RGB_{timeNOW}.jpg")
cv2.imwrite(RGBfilename, np.asanyarray(color_frame.get_data()))
THERMALfilename = os.path.join("Images", f"{dateNOW}", f"Thermal_{timeNOW}.jpg")
cv2.imwrite(THERMALfilename, frameT)
DEPTHfilename = os.path.join("Images", f"{dateNOW}", f"Depth_{timeNOW}.jpg")
cv2.imwrite(DEPTHfilename, depth_colormap)

# Cleanup
pipeline.stop()
cv2.destroyAllWindows()
