import os 
import cv2

# import Thermal.MainThermal as MT
import RGB.MainRGB as MRGB

cs = MRGB.CamStream(camera_index=1, width=640, height=480)
# ts = MRGB.CamStream(camera_index="rtsp://root:kamera@169.254.104.184/axis-media/media.amp", width=640, height=480)
cs.run()
# ts.run()
