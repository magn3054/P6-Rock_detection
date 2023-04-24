# import MainRGB as cam
# import cv2
# import time

# cs = cam.CamStream(camera_index=0, width=640, height=480)


# # Capture an image
# while True:
#     ret, frameC = cs.cam.read()

#     if ret:
#         cv2.imshow("Normal", frameC)
#         # cv2.waitKey(5000):

#         if cv2.waitKey(1) == ord('q'):
#             break
#     else:
#         break 


# # cv2.imshow("Image", frameC)
# # cv2.waitKey(1)

# cs.cam.release()
# cv2.destroyAllWindows()


#############################################

import cv2
import time

# Open the camera
cap = cv2.VideoCapture(0)

# Start time
start_time = time.time()

# Loop through the frames
while (time.time() - start_time) < 2:
    # Read the frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera Feed', frame)
    cv2.waitKey(1)

# Save the last frame
cv2.imwrite('last_frame.jpg', frame)

# Release the camera
cap.release()
cv2.destroyAllWindows()
