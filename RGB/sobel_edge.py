import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/RGB/pebbles1.png')
img = cv.resize(img, (400,800))

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv.GaussianBlur(gray, (5, 5), 0)

# Apply Sobel edge detection in the x and y direction
sobelx = cv.Sobel(blurred, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(blurred, cv.CV_64F, 0, 1, ksize=5)

# Compute the magnitude of the gradient
magnitude = np.sqrt(sobelx**2 + sobely**2)

# Normalize the magnitude image
magnitude = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)

# Threshold the magnitude image to create a binary image
thresh = cv.threshold(magnitude, 50, 255, cv.THRESH_BINARY)[1]

# Find contours in the binary image
contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv.drawContours(img, contours, -1, (0, 0, 255), 2)

# Display the result
cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()
