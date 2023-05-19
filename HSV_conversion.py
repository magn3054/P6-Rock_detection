import cv2
import numpy as np
import matplotlib.pyplot as plt

therm_path = "./Images/10-05-2023/Thermal_09;32;22.jpg" 

# Load image
img = cv2.imread(therm_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


### mask for orange and yellow ###
kernel = np.ones((5,5),np.uint8)
radius = 7
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*radius+1, 2*radius+1))
lower = np.array([14, 182, 241])  
upper = np.array([34, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel2)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel2)

# Apply mask to original image
merged = cv2.bitwise_and(img, img, mask=mask)
merged2 = merged.copy()


### BLOB ###
# Reshapes 3 channel image into a list of pixels 
pixels = merged2.reshape((-1, 3))

# Convert pixel values to float32 for the k-means clustering command
pixels = np.float32(pixels)

# Define k-means parameters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Cluster size
k = 3

# Run k-means clustering
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers back to uint8 and reshape to match image shape
centers = np.uint8(centers)
res = centers[labels.flatten()]
res2 = res.reshape((merged2.shape))


cv2.imwrite("zBLOBd_full.jpg", res2)


# Use connected component analysis to separate the individual blobs
components, labels, stats, centroids= cv2.connectedComponentsWithStats(mask) 
# stats return the xpos[0], ypos[1], width[2], height[3] and area[4] of the different blobs
rois=[]
for i in range(1, len(stats)): 
    x = stats[i][0]
    y = stats[i][1]
    w = stats[i][2]
    h = stats[i][3]
    roi = (x, y, w, h)
    rois.append(roi)

new_value = 0  # black pixel

for i, (x, y, w, h) in enumerate(rois):
    # Extract region of interest
    roi = res2[y:y+h, x:x+w]
    
    # Compute color histogram
    hist = cv2.calcHist([res2], [0, 1], None, [180, 256], [0, 180, 0, 256])
    
    # find colors present in region 
    color_threshold = 50 # filters out color with low saturation/brightness such as black 
    colors = []
    for row in roi: 
        for pixel in row:
            hue,sat,val = pixel
            if sat > color_threshold and val > color_threshold:
                hue_bin = int(hue)
                colors.append(hue_bin) 
    
    color_counts = np.bincount(colors)
    color_counts = np.concatenate([color_counts, np.zeros(180-len(color_counts), dtype=int)])
    

    if color_counts[3] > color_counts[18]:
        for row in range(roi.shape[0]):
            for col in range(roi.shape[1]):
                roi[row, col] = new_value        

    # Display color histogram
    big_roi = cv2.resize(roi, (250,250))
    cv2.imshow("image", big_roi)
    plt.plot(range(0,180), color_counts)
    plt.title(f"Colors in ROI {i+1}")
    plt.xlabel("Hue bins")
    plt.ylabel("Pixel count")
    plt.show()



# ### mask for only yellow ###
# lower_yellow = np.array([4, 0, 0])
# upper_yellow = np.array([255, 255, 255])
# lower_orange = np.array([0, 0, 0])
# upper_orange = np.array([250, 250, 250])

# # Create a mask for the yellow color range
# yellow_mask = cv2.inRange(res2, lower_yellow, upper_yellow)
# orange_mask = cv2.inRange(res2, lower_orange, upper_orange)


# # Apply the mask to the original image to isolate the yellow blobs
# yellow_blobs = cv2.bitwise_and(res2, res2, mask=yellow_mask)
# orange_blobs = cv2.bitwise_and(res2, res2, mask=orange_mask)

gray = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)


### Find contours ###
contours, hierarchy = cv2.findContours(binary_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours = sorted(contours, key=lambda c: cv2.contourArea(c), reverse=True) # Shows only the biggest bounding box
for cnt in contours:
    # Approximate contour with a circle
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)

    arclenght = cv2.arcLength(cnt, True)**2
    if arclenght == 0:  
        arclenght =+ 0.01 # makes sure arclenght doesn't become zero

    # Check if the contour is round
    circularity = 4*3.15*cv2.contourArea(cnt)/arclenght
    if circularity >= 0.5: # adjust this threshold to preference size of rocks needed to be discovered
        if radius >= 7:
            cv2.putText(img, "rock", (int(x-radius), int(y-radius-10)), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
            cv2.circle(img,center,radius,(0,255,0),2)



### Display output image ###
cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('blobbed merge', res2)
# cv2.imshow('yellow_blobs', yellow_blobs)
# cv2.imshow('orange_blobs', orange_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
