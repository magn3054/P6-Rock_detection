import cv2
import numpy as np

# Load imageThermal_13;23;45.jpg
img = cv2.imread("./Images/20-04-2023/Thermal_13;23;45.jpg")
# img = img[225:600, 0:800]

# Reshape image into a 2D array of pixels
pixels = img.reshape((-1, 3))

# Convert pixel values to float32 for k-means clustering
pixels = np.float32(pixels)

# Define k-means parameters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 3  # number of clusters

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
