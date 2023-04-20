import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/thermal_img1.jpg')
# img = cv.resize(img, (400,800))

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv.Canny(blurred, 50, 150)

# Find contours in the edges image
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv.drawContours(img, contours, -1, (0, 0, 255), 2)

# Display the result
cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()

