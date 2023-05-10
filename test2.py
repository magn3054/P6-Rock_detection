import cv2
import numpy as np

kernel = 99
kernel2 = np.ones((5,5), np.uint8)
kernel3 = np.array([[0,0,1,0,0],
                    [0,1,1,1,0],
                    [1,1,1,1,1],
                    [0,1,1,1,0],
                    [0,0,1,0,0]])
# Define paths for input and template images
input_folder = [
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;44;35.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;45;44.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;46;21.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;11.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;47;38.jpg",
    "C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/26-04-2023/RGB_13;48;05.jpg"
    ]

# Load the three template images
template1 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;47;11.jpg")
template2 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;47;38.jpg")
template3 = cv2.imread("C:/Users/magnu/OneDrive - Aalborg Universitet/6. semester/P6 Project/Code/P6-AGCO/Images/templates/template_13;48;05.jpg")

# Calculate the histogram of each template image
hist1 = cv2.calcHist([cv2.cvtColor(template1, cv2.COLOR_BGR2HSV)], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist2 = cv2.calcHist([cv2.cvtColor(template2, cv2.COLOR_BGR2HSV)], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist3 = cv2.calcHist([cv2.cvtColor(template3, cv2.COLOR_BGR2HSV)], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Normalize the histograms
cv2.normalize(hist1, hist1, 0, 255, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 255, cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, 255, cv2.NORM_MINMAX)

# Loop through input images
for input_file in input_folder:
    # Load the input image
    img = cv2.imread(input_file)

    # Create a mask for each template based on the color space
    mask1 = cv2.calcBackProject([cv2.cvtColor(img, cv2.COLOR_BGR2HSV)], [0, 1], hist1, [0, 180, 0, 256], 1)
    mask1 = cv2.medianBlur(mask1, kernel)
    # mask1 = cv2.dilate(mask1,kernel2, iterations=1)
    # mask1 = cv2.erode(mask1,kernel2, iterations=1)

    mask2 = cv2.calcBackProject([cv2.cvtColor(img, cv2.COLOR_BGR2HSV)], [0, 1], hist2, [0, 180, 0, 256], 1)
    mask2 = cv2.medianBlur(mask2, kernel)
    # mask2 = cv2.dilate(mask2,kernel2, iterations=1)
    # mask2 = cv2.erode(mask2,kernel2, iterations=1)

    mask3 = cv2.calcBackProject([cv2.cvtColor(img, cv2.COLOR_BGR2HSV)], [0, 1], hist3, [0, 180, 0, 256], 1)
    mask3 = cv2.medianBlur(mask3, kernel)
    # mask3 = cv2.dilate(mask3,kernel2, iterations=1)
    # mask3 = cv2.erode(mask3,kernel2, iterations=1)

    # Apply each mask to the input image
    res1 = cv2.bitwise_and(img, img, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    res3 = cv2.bitwise_and(img, img, mask=mask3)

    # Display the results
    cv2.imshow('Template 1 Result', res1)
    cv2.imshow('Template 2 Result', res2)
    cv2.imshow('Template 3 Result', res3)
    cv2.waitKey(0)

cv2.destroyAllWindows()