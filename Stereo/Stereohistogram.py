import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load three images
img1 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/RGB_15;01;10.jpg")
img2 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/Thermal_15;01;10.jpg")
img3 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/Depth_15;01;10.jpg")

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# Compute histograms
hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([gray3], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(10, 4))

plt.subplot(131)
plt.plot(hist1)
plt.title("RGB")

plt.subplot(132)
plt.plot(hist2)
plt.title("Thermal")

plt.subplot(133)
plt.plot(hist3)
plt.title("Depth")

plt.show()
