import pyrealsense2 as rs
import numpy as np
import cv2

# Initialize the RealSense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)

try:
    while True:
        # Wait for a new frame
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        # Convert the depth frame to a numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Convert the color frame to a numpy array
        color_image = np.asanyarray(color_frame.get_data())

        # Convert depth image to distance in meters
        depth_sensor = pipeline.get_active_profile().get_device().first_depth_sensor()
        depth_scale = depth_sensor.get_depth_scale()
        distances = depth_image * depth_scale

        # Find the nearest rock in the image
        min_distance = np.min(distances[depth_image > 0])
        nearest_rock = np.where(distances == min_distance)

        # Draw a red box around the nearest rock in the color image
        x, y = nearest_rock[1][0], nearest_rock[0][0]
        cv2.rectangle(color_image, (x-10, y-10), (x+10, y+10), (0, 0, 255), 2)

        # Show the stereo image
        stereo_image = np.hstack((color_image, cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)))
        cv2.imshow("Stereo Image", stereo_image)

        if cv2.waitKey(1) == 27:
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
