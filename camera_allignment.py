import cv2
import numpy as np

# Load the images from the two cameras
img1 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/RGB_14;32;29.jpg")
img2 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/24-04-2023/Thermal_14;32;29.jpg")

cv2.imshow("1 Image", img1)
cv2.imshow("2 Image", img2)


if img1.shape != img2.shape:
    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# Find the keypoints and descriptors in the images
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Match the keypoints and descriptors using a Brute-Force Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort the matches by their distances
matches = sorted(matches, key=lambda x: x.distance)

# Compute the Homography matrix using the best matches
src_pts = np.float32([kp1[m.queryIdx].pt for m in matches[:10]]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches[:10]]).reshape(-1, 1, 2)
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Apply the Homography matrix to the first image
height, width, _ = img1.shape
img1_warped = cv2.warpPerspective(img1, M, (width, height))

# Combine the two images
img_aligned = cv2.addWeighted(img2, 0.5, img1_warped, 0.5, 0)

# Display the aligned image
cv2.imshow("Aligned Image", img_aligned)
cv2.waitKey(0)
cv2.destroyAllWindows()
