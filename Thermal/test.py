import cv2
import numpy as np

# Load image
img = cv2.imread("Images/19-04-23/(13;45)thermal_img.jpg")

# Define blue color range to exclude from segmentation
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Create a mask of blue color areas to exclude
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Invert the mask to exclude blue color areas
mask = cv2.bitwise_not(mask)

# Apply the mask to the original image
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Reshape image into a 2D array of pixels
pixels = masked_img.reshape((-1, 3))

# Convert pixel values to float32 for k-means clustering
pixels = np.float32(pixels)

# Define k-means parameters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 2  # number of clusters

# Run k-means clustering
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers back to uint8 and reshape to match image shape
centers = np.uint8(centers)
res = centers[labels.flatten()]
res2 = res.reshape((img.shape))

# Display segmented image
cv2.imshow('segmented image', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
