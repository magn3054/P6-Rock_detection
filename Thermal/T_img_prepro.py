import os
import cv2 

img = cv2.imread("Images/19-04-23/(13;45)thermal_img.jpg")
print(img.shape)

img = img[225:600, 0:800]

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold_value1 = 50
# max_value = 255
# ret, bw_img1 = cv2.threshold(gray_img, threshold_value1, max_value, cv2.THRESH_BINARY)

# threshold_value2 = 127
# max_value = 255
# ret, bw_img2 = cv2.threshold(gray_img, threshold_value2, max_value, cv2.THRESH_BINARY)

threshold_value3 = 90
max_value = 255
ret, bw_img3 = cv2.threshold(gray_img, threshold_value3, max_value, cv2.THRESH_BINARY)





cv2.imshow("img", img)
cv2.imshow("Grayscale", gray_img)
# cv2.imshow("Black/White 50", bw_img1)
# cv2.imshow("Black/White 127", bw_img2)
cv2.imshow("Black/White 200", bw_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()