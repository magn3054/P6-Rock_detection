import cv2 

img = cv2.imread("C:/Users/magnu_wr887wi/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;11.jpg")


# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the original and HSV images side by side
cv2.imshow("Original Image", img)
cv2.imshow("HSV Image", hsv_img)

# Wait for key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()