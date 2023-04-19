import cv2

# Open the camera
cam = cv2.VideoCapture('rtsp://root:kamera@169.254.104.184/axis-media/media.amp')

# Wait for camera to warm up
cv2.waitKey(1000)

# Capture an image
ret, frame = cam.read()

# Display the image
cv2.imshow("Image", frame)

# Save the image to a file
cv2.imwrite("thermal_img1.jpg", frame)

# Cleanup
cam.release()
cv2.destroyAllWindows()